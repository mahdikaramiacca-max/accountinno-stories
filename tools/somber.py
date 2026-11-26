"""Serious cinematic piano + pad, no drums. Each seed: different key/progression/arpeggio."""
import numpy as np, wave, sys
SR=44100
def mtof(m): return 440*2**((m-69)/12)
PR=[[[0,3,7],[-4,0,3],[-9,-5,0],[-2,2,5]],[[0,3,7],[-2,2,5],[-4,0,3],[-5,-1,2]],[[0,3,7],[5,8,12],[3,7,10],[-2,2,5]],[[-4,0,3],[-2,2,5],[0,3,7],[0,3,7]]]
def lp(x,a):
    y=np.empty_like(x); c=0.0
    for i in range(len(x)): c+=a*(x[i]-c); y[i]=c
    return y
def piano(f,dur):
    t=np.arange(int(dur*SR))/SR; s=0
    for k,a in ((1,1),(2,.45),(3,.22),(4,.12),(5,.06)):
        s=s+a*np.sin(2*np.pi*f*k*t*(1+0.0004*k*k))*np.exp(-t*(1.2+0.9*k))
    return s*(1-np.exp(-t*300))
def make(seed,dur,path):
    r=np.random.default_rng(seed); bpm=int(r.integers(62,74)); beat=60/bpm; bar=4*beat
    root=int(r.integers(50,57)); pr=PR[seed%len(PR)]; n=int(dur*SR); L=np.zeros(n); R=np.zeros(n)
    def add(b,s,x):
        if s<n: e=min(n,s+len(x)); b[s:e]+=x[:e-s]
    pat=[[0,1,2,1,0,1,2,1],[0,2,1,2,0,2,1,2],[0,1,2,3,2,1,2,1]][seed%3]
    for i in range(int(dur/bar)+1):
        ch=pr[i%4]; s0=int(i*bar*SR); notes=[root+c for c in ch]+[root+ch[0]+12]
        # pad
        t=np.arange(int(bar*1.3*SR))/SR; env=np.minimum(1,t/1.2)*np.exp(-t*0.4)
        for c in ch:
            f=mtof(root+c-12); pad=0.035*env*(np.sin(2*np.pi*f*t)+0.5*np.sin(2*np.pi*f*1.003*t)+0.3*np.sin(2*np.pi*2*f*t))
            add(L,s0,pad); add(R,s0,pad*0.95)
        # bass piano
        add(L,s0,0.18*piano(mtof(root+ch[0]-12),bar)); add(R,s0,0.18*piano(mtof(root+ch[0]-12),bar))
        # arpeggio
        for k,p in enumerate(pat):
            if i==0 and k<4: continue
            f=mtof(notes[p%len(notes)]+12); x=0.12*piano(f,beat*2.5)*(0.8+0.2*r.random())
            st=s0+int(k*beat/2*SR); pan=0.4+0.2*(p/3); add(L,st,x*(1-pan)*1.6); add(R,st,x*pan*1.6)
        # occasional high melody note
        if i%2==1:
            f=mtof(root+24+[0,3,7,10,12][int(r.integers(0,5))]); add(L,s0+int(beat*SR),0.07*piano(f,bar)); add(R,s0+int(beat*1.02*SR),0.07*piano(f,bar))
    out=[]
    for X,Y in ((L,R),(R,L)):
        Z=X.copy()
        for d,g in ((0.043,.4),(0.089,.33),(0.137,.28),(0.211,.22),(0.33,.16),(0.47,.1)):
            o=int(d*SR); Z[o:]+=g*Y[:-o]
        out.append(lp(Z,0.45))
    st=np.stack(out,1); fade=np.ones(n); fi=int(.6*SR); fo=int(1.5*SR); fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
    st=np.tanh(st*fade[:,None]*1.3); st=st/np.max(np.abs(st))*0.8
    w=wave.open(path,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
if __name__=='__main__': make(int(sys.argv[1]),float(sys.argv[2]),sys.argv[3])
