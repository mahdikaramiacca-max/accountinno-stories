"""Mellow lo-fi / jazzy chill generator; every seed = different key, progression, tempo, melody."""
import numpy as np, wave, sys
SR=44100
def mtof(m): return 440*2**((m-69)/12)
PROGS=[[[0,4,7,11,14],[9,12,16,19],[2,5,9,12,16],[7,11,14,17,21]],      # Imaj9 vi7 ii9 V9
       [[2,5,9,12],[7,11,14,17],[0,4,7,11,14],[0,4,7,11]],              # ii V I I
       [[9,12,16,19],[5,9,12,16],[0,4,7,11],[7,11,14,17]],              # vi IV I V
       [[0,4,7,11],[4,7,11,14],[5,9,12,16],[5,8,12,15]],                # I iii IV iv
       [[5,9,12,16,19],[4,7,11,14],[2,5,9,12],[0,4,7,11,14]]]           # IV iii ii I
def lp(x,a): 
    y=np.empty_like(x); acc=0.0
    for i in range(len(x)): acc+=a*(x[i]-acc); y[i]=acc
    return y
def make(seed,dur,path):
    r=np.random.default_rng(seed); bpm=int(r.integers(70,86)); beat=60/bpm; bar=4*beat
    root=int(r.integers(50,58)); prog=PROGS[seed%len(PROGS)]; n=int(SR*dur)
    L=np.zeros(n); R=np.zeros(n)
    def add(buf,s,sig):
        if s>=n: return
        e=min(n,s+len(sig)); buf[s:e]+=sig[:e-s]
    # rhodes-like chords, slightly strummed
    for i in range(int(dur/bar)+1):
        ch=prog[i%4]; s0=int(i*bar*SR)
        for j,iv in enumerate(ch):
            f=mtof(root+iv); m=int(bar*1.1*SR); t=np.arange(m)/SR
            env=np.exp(-t*0.9)*(1-np.exp(-t*60)); trem=1+0.15*np.sin(2*np.pi*4.5*t)
            sig=0.05*env*trem*(np.sin(2*np.pi*f*t)+0.35*np.sin(2*np.pi*2*f*t)*np.exp(-t*3)+0.1*np.sin(2*np.pi*3*f*t)*np.exp(-t*6))
            st=s0+int(j*0.018*SR); pan=0.35+0.3*j/len(ch)
            add(L,st,sig*(1-pan)*1.4); add(R,st,sig*pan*1.4)
        # second hit on beat 3 (softer), varies
        if r.random()<.6:
            for j,iv in enumerate(ch[:3]):
                f=mtof(root+iv); m=int(beat*1.8*SR); t=np.arange(m)/SR
                sig=0.03*np.exp(-t*2)*np.sin(2*np.pi*f*t); st=s0+int((2.5*beat+j*0.015)*SR); add(L,st,sig); add(R,st,sig)
        # bass
        bf=mtof(root+ch[0]-12); t=np.arange(int(bar*SR))/SR
        bs=0.14*np.exp(-t*0.6)*(np.sin(2*np.pi*bf*t)+0.2*np.sin(2*np.pi*2*bf*t)); add(L,s0,bs); add(R,s0,bs)
    # pentatonic melody (sparse, sweet)
    pent=[0,2,4,7,9,12,14,16]; mot=r.integers(0,8,8); rhy=r.random(8)<.45
    for k in range(int(dur/(beat/2))):
        if k<16 or not rhy[k%8]: continue
        f=mtof(root+12+pent[int(mot[k%8])]); m=int(beat*1.5*SR); t=np.arange(m)/SR
        kind=seed%3
        if kind==0: sig=np.sin(2*np.pi*f*t+1.2*np.sin(2*np.pi*f*t)*np.exp(-t*4))   # soft bell
        elif kind==1: sig=np.sin(2*np.pi*f*t)*(1+0.3*np.sin(2*np.pi*5*t))          # flute-ish vibrato
        else: sig=np.sign(np.sin(2*np.pi*f*t))*0.25+np.sin(2*np.pi*f*t)*0.6        # mellow square
        sig=0.045*sig*np.exp(-t*3)*(1-np.exp(-t*40)); st=int(k*beat/2*SR); add(L,st,sig*.8); add(R,st+int(.01*SR),sig)
    # soft drums, swung
    for k in range(int(dur/(beat/2))):
        sw=int((beat/2)*0.16*SR) if k%2 else 0; st=int(k*beat/2*SR)+sw; pos=k%8
        if pos in (0,5) or (pos==3 and r.random()<.3):
            t=np.arange(int(.3*SR))/SR; sig=0.4*np.exp(-t*10)*np.sin(2*np.pi*(48+60*np.exp(-t*40))*t); add(L,st,sig); add(R,st,sig)
        if pos in (2,6):
            t=np.arange(int(.25*SR))/SR; nz=lp(r.standard_normal(len(t)),0.25); sig=0.22*nz*np.exp(-t*16); add(L,st,sig); add(R,st,sig)
        t=np.arange(int(.04*SR))/SR; h=0.025*r.standard_normal(len(t))*np.exp(-t*90)*(1.0 if pos%2==0 else .6); add(L,st,h*.6); add(R,st,h)
    # vinyl crackle + hiss
    cr=np.zeros(n); idx=r.integers(0,n,int(dur*25)); cr[idx]=r.uniform(-.15,.15,len(idx)); hiss=lp(r.standard_normal(n),0.05)*0.006
    L+=cr+hiss; R+=cr+hiss
    # reverb-ish multi-tap
    out=[]
    for X,Y in ((L,R),(R,L)):
        Z=X.copy()
        for d,g in ((0.031,.35),(0.067,.3),(0.113,.25),(0.19,.2),(beat*.75,.18)):
            o=int(d*SR); Z[o:]+=g*Y[:-o]
        out.append(lp(Z,0.35))
    st=np.stack(out,1); fade=np.ones(n); fi=int(.4*SR); fo=int(1.5*SR); fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
    st=st*fade[:,None]; st=np.tanh(st*1.6); st=st/np.max(np.abs(st))*0.8
    w=wave.open(path,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
    return bpm
if __name__=='__main__': print(make(int(sys.argv[1]),float(sys.argv[2]),sys.argv[3]))
