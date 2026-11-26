"""Original Persian-flavoured music: santur-like hammered dulcimer (with tremolo), tar-like plucks,
drone, daf in 6/8. Modes include quarter-tones. mood: 'mahur' (joyful), 'shur' (reflective), 'isfahan' (warm), 'chahargah' (dramatic)."""
import numpy as np, wave, sys
SR=44100
MODES={'mahur':[0,2,4,5,7,9,11,12],'shur':[0,1.5,3,5,7,8,10,12],'isfahan':[0,2,3,5,7,8,11,12],'chahargah':[0,1.5,4,5,7,8.5,11,12]}
def mtof(m): return 440*2**((m-69)/12)
def lp(x,a):
    y=np.empty_like(x); c=0.0
    for i in range(len(x)): c+=a*(x[i]-c); y[i]=c
    return y
def santur(f,dur):
    t=np.arange(int(dur*SR))/SR; s=0
    for k,a in ((1,1),(2,.5),(3,.35),(4.02,.2),(5.05,.12),(6.1,.08)):
        s=s+a*np.sin(2*np.pi*f*k*t)*np.exp(-t*(2.2+1.4*k))
    s+=0.3*np.sin(2*np.pi*f*1.003*t)*np.exp(-t*2.5)   # paired-string chorus
    return s*(1-np.exp(-t*900))
def tar(f,dur):
    t=np.arange(int(dur*SR))/SR; s=0
    for k in range(1,9): s=s+np.sin(2*np.pi*f*k*t)/k**1.1*np.exp(-t*(3+k*1.5))
    return lp(s*(1-np.exp(-t*500)),0.5)
def make(seed,dur,path,mood='mahur'):
    r=np.random.default_rng(seed); sc=MODES[mood]; root=int(r.integers(60,65))
    bpm={'mahur':112,'shur':84,'isfahan':96,'chahargah':100}[mood]+int(r.integers(-5,6))
    e=60/bpm/2  # eighth note; 6/8 bar = 6 eighths
    n=int(dur*SR); L=np.zeros(n); R=np.zeros(n)
    def add(b,s,x,g=1.0):
        if 0<=s<n: q=min(n,s+len(x)); b[s:q]+=g*x[:q-s]
    # drone (tonic + fifth), soft
    t=np.arange(n)/SR; dr=0.05*(np.sin(2*np.pi*mtof(root-24)*t)+0.6*np.sin(2*np.pi*mtof(root-17)*t))*(1+0.1*np.sin(2*np.pi*0.2*t))
    L+=lp(dr,0.05); R+=lp(dr,0.05)
    # melody: generate phrases from motif, stepwise, santur with tremolo on long notes
    nbar=int(dur/(6*e))+1; motif=[0,1,2,1,0,-1] if mood!='mahur' else [0,2,4,2,3,1]
    pos=2; idx=[]
    for b in range(nbar):
        for k in range(6):
            if r.random()<0.18 and k%3==2: idx.append(None); continue
            step=motif[k]+(b%4==2)*2-(b%4==3)
            idx.append(max(0,min(len(sc)-1,pos+step)))
    for i,dg in enumerate(idx):
        if dg is None: continue
        st=int(i*e*SR); f=mtof(root+sc[dg]); long=(i%6 in (0,3)) and r.random()<0.5
        if long:   # santur tremolo
            for j in range(5): add(L,st+int(j*e/2.5*SR),santur(f,e*1.2),0.11*(1-j*0.12)); add(R,st+int(j*e/2.5*SR)+80,santur(f,e*1.2),0.1*(1-j*0.12))
        else:
            add(L,st,santur(f,e*3),0.14); add(R,st+60,santur(f,e*3),0.12)
        if i%6==0:  # tar answers in lower octave
            add(L,st+int(3*e*SR),tar(mtof(root-12+sc[max(0,dg-2)]),e*3),0.12); add(R,st+int(3*e*SR),tar(mtof(root-12+sc[max(0,dg-2)]),e*3),0.14)
    # daf 6/8: DUM . tak tak DUM tak  (enters after 1 bar)
    pat={0:'D',2:'t',3:'t',4:'D',5:'t'}
    for i in range(6,int(dur/e)):
        h=pat.get(i%6)
        if not h: continue
        st=int(i*e*SR); tt=np.arange(int(.3*SR))/SR
        if h=='D': x=0.35*np.sin(2*np.pi*(70+40*np.exp(-tt*30))*tt)*np.exp(-tt*9)+0.05*r.standard_normal(len(tt))*np.exp(-tt*40)
        else: x=0.12*lp(r.standard_normal(len(tt)),0.7)*np.exp(-tt*28)+0.06*np.sin(2*np.pi*420*tt)*np.exp(-tt*30)
        jingle=0.03*r.standard_normal(len(tt))*np.exp(-tt*12)   # daf ring
        add(L,st,x+jingle); add(R,st,x+jingle*0.8)
    out=[]
    for X,Y in ((L,R),(R,L)):
        Z=X.copy()
        for d,g in ((0.041,.35),(0.083,.28),(0.127,.22),(0.19,.16),(0.29,.1)):
            o=int(d*SR); Z[o:]+=g*Y[:-o]
        out.append(Z)
    st=np.stack(out,1); fade=np.ones(n); fi=int(.3*SR); fo=int(1.3*SR); fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
    st=np.tanh(st*fade[:,None]*1.4); st=st/np.max(np.abs(st))*0.85
    w=wave.open(path,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
if __name__=='__main__': make(int(sys.argv[1]),float(sys.argv[2]),sys.argv[3],sys.argv[4] if len(sys.argv)>4 else 'mahur')
