"""Emotional cinematic: expressive piano melody + swelling strings + cello line, minor key, slow."""
import numpy as np, wave, sys
sys.path.insert(0,'/home/claude/stories'); from somber import piano, lp, mtof
SR=44100
PR=[[[0,3,7],[-4,0,3],[-9,-5,0],[-5,-1,2]],[[0,3,7],[-2,2,5],[-4,0,3],[-5,-1,2]],[[-4,0,3],[0,3,7],[-2,2,5],[-7,-3,0]]]
MEL=[[7,5,3,2,3,-2,0],[12,10,7,8,7,5,3],[3,5,7,10,8,7,5]]
def strings(f,dur,att):
    t=np.arange(int(dur*SR))/SR; vib=1+0.004*np.sin(2*np.pi*5.2*t)
    s=sum(np.sin(2*np.pi*k*f*vib*t+k)/k**1.3 for k in range(1,7))
    env=np.minimum(1,t/att)*np.minimum(1,(t[-1]-t)/0.8+0.05)
    return lp(s*env,0.12)
def make(seed,dur,path):
    r=np.random.default_rng(seed); bpm=int(r.integers(58,66)); beat=60/bpm; bar=4*beat
    root=int(r.integers(50,56)); pr=PR[seed%3]; mel=MEL[seed%3]; n=int(dur*SR); L=np.zeros(n); R=np.zeros(n)
    def add(b,s,x):
        if s<n: e=min(n,s+len(x)); b[s:e]+=x[:e-s]
    nb=int(dur/bar)+1
    for i in range(nb):
        ch=pr[i%4]; s0=int(i*bar*SR); grow=min(1,0.35+0.25*i)
        # strings swell (crescendo over the piece)
        for j,c in enumerate(ch):
            x=0.03*grow*strings(mtof(root+c),bar*1.15,bar*0.6); add(L,s0,x*(1.2-0.2*j)); add(R,s0,x*(0.8+0.2*j))
        # cello
        x=0.06*grow*strings(mtof(root+ch[0]-12),bar*1.1,0.5); add(L,s0,x); add(R,s0,x)
        # piano broken chord
        for k,c in enumerate([ch[0]-12,ch[1],ch[2],ch[1]+12]):
            x=0.09*piano(mtof(root+c),beat*3); add(L,s0+int(k*beat*SR),x*1.1); add(R,s0+int(k*beat*SR),x*.9)
    # expressive melody, enters bar 1
    t0=bar*0.5
    for k,deg in enumerate(mel*3):
        st=t0+k*beat*1.0+(0.08*r.random())
        if st>dur-1.5: break
        x=0.16*piano(mtof(root+12+deg),beat*2.5); add(L,int(st*SR),x); add(R,int((st+0.01)*SR),x*0.95)
    out=[]
    for X,Y in ((L,R),(R,L)):
        Z=X.copy()
        for d,g in ((0.053,.45),(0.097,.38),(0.151,.32),(0.229,.26),(0.341,.2),(0.52,.14),(0.77,.08)):
            o=int(d*SR); Z[o:]+=g*Y[:-o]
        out.append(lp(Z,0.5))
    st=np.stack(out,1); fade=np.ones(n); fi=int(.8*SR); fo=int(1.8*SR); fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
    st=np.tanh(st*fade[:,None]*1.2); st=st/np.max(np.abs(st))*0.82
    w=wave.open(path,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
if __name__=='__main__': make(int(sys.argv[1]),float(sys.argv[2]),sys.argv[3])
