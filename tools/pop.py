"""Upbeat catchy pop/house: sidechained supersaw chords, sub bass, plucky hook with delay, claps."""
import numpy as np, wave, sys
SR=44100
def mtof(m): return 440*2**((m-69)/12)
def lp(x,a):
    y=np.empty_like(x); c=0.0
    for i in range(len(x)): c+=a*(x[i]-c); y[i]=c
    return y
def saw(f,t,n=10): return sum(np.sin(2*np.pi*k*f*t)/k for k in range(1,n))
PROGS=[[[0,4,7],[7,11,14],[9,12,16],[5,9,12]],[[9,12,16],[5,9,12],[0,4,7],[7,11,14]],[[5,9,12],[7,11,14],[4,7,11],[9,12,16]]]
def make(seed,dur,path):
    r=np.random.default_rng(seed); bpm=int(r.integers(112,120)); beat=60/bpm; bar=4*beat
    root=int(r.integers(57,63)); prog=PROGS[seed%3]; n=int(dur*SR); L=np.zeros(n); R=np.zeros(n)
    def add(b,s,x):
        if s<n: e=min(n,s+len(x)); b[s:e]+=x[:e-s]
    t_all=np.arange(n)/SR; ph=(t_all%beat)/beat; side=np.minimum(1,0.25+ph*2.2)  # sidechain pump
    pads=np.zeros(n); padR=np.zeros(n)
    for i in range(int(dur/bar)+1):
        ch=prog[i%4]; s0=int(i*bar*SR); m=int(bar*SR); t=np.arange(m)/SR
        for c in ch:
            f=mtof(root+c)
            for dt,pan in ((-0.006,.7),(0.0,.5),(0.007,.3)):
                x=0.018*saw(f*(1+dt),t,8); add(pads,s0,x*pan); add(padR,s0,x*(1-pan))
        bf=mtof(root+ch[0]-24)
        for q in range(8):   # offbeat bass
            if q%2==0: continue
            st=s0+int(q*beat/2*SR); tt=np.arange(int(beat/2*0.9*SR))/SR
            x=0.22*np.sin(2*np.pi*bf*tt)*np.exp(-tt*4); add(L,st,x); add(R,st,x)
    L+=lp(pads,0.25)*side; R+=lp(padR,0.25)*side
    # catchy hook: 2-bar motif repeated
    scale=[0,2,4,7,9,12,14,16]; hook=[(0,4),(1,4),(2,5),(3,7),(5,4),(6,2),(8,4),(10,5),(11,4),(12,2),(14,0)]
    var=int(r.integers(0,3))
    for b2 in range(1,int(dur/(2*bar))+1):
        for step,deg in hook:
            if step*beat/2+b2*2*bar>dur: break
            st=int((b2*2*bar+step*beat/2)*SR); f=mtof(root+12+scale[(deg+var)%len(scale)])
            tt=np.arange(int(.35*SR))/SR; x=0.09*(np.sin(2*np.pi*f*tt)+0.4*np.sin(2*np.pi*2*f*tt))*np.exp(-tt*9)
            add(L,st,x); add(R,st,x*.9)
            d=int(beat*.75*SR); add(L,st+d,x*.35); add(R,st+2*d,x*.2)
    # drums: soft 4-on-floor, clap on 2&4, open hat offbeats
    for k in range(int(dur/(beat/2))):
        st=int(k*beat/2*SR); pos=k%8
        if k<8: continue
        if pos%2==0:
            tt=np.arange(int(.25*SR))/SR; x=0.5*np.exp(-tt*12)*np.sin(2*np.pi*(50+90*np.exp(-tt*40))*tt); add(L,st,x); add(R,st,x)
        if pos in (2,6):
            tt=np.arange(int(.2*SR))/SR; x=0.2*lp(r.standard_normal(len(tt)),0.6)*np.exp(-tt*18); add(L,st,x); add(R,st,x)
        if pos%2==1:
            tt=np.arange(int(.09*SR))/SR; x=0.06*r.standard_normal(len(tt))*np.exp(-tt*35); add(L,st,x*.7); add(R,st,x)
    # riser in first 2 bars
    m=int(2*bar*SR); tt=np.arange(m)/SR; rs=0.03*r.standard_normal(m)*(tt/tt[-1])**2; add(L,0,rs); add(R,0,rs)
    st=np.stack([L,R],1); fade=np.ones(n); fo=int(1.2*SR); fade[-fo:]=np.linspace(1,0,fo); fade[:int(.1*SR)]=np.linspace(0,1,int(.1*SR))
    st=np.tanh(st*fade[:,None]*1.5); st=st/np.max(np.abs(st))*0.85
    w=wave.open(path,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
if __name__=='__main__': make(int(sys.argv[1]),float(sys.argv[2]),sys.argv[3])
