"""Procedural original music: each seed gives a different style/key/tempo/progression."""
import numpy as np, wave, sys
SR=44100
def mtof(m): return 440*2**((m-69)/12)
PROGS={'minor':[[0,3,7,10],[-4,0,3,7],[-9,-5,-2,3],[-2,2,5,9]],
       'major':[[0,4,7,11],[-3,0,4,7],[5,9,12,16],[7,11,14,17]],
       'dorian':[[0,3,7,10],[5,9,12,15],[0,3,7,10],[-2,2,5,9]],
       'pop':[[0,4,7,12],[7,11,14,19],[-3,0,4,9],[5,9,12,17]]}
STYLES=['lofi','house','cinematic','pluck','trap','synthwave','afro','chill']
def osc(kind,f,t):
    p=2*np.pi*f*t
    if kind=='sine': return np.sin(p)
    if kind=='saw': return sum(np.sin(k*p)/k for k in range(1,9))*0.6
    if kind=='square': return sum(np.sin(k*p)/k for k in range(1,10,2))*0.8
    if kind=='bell': return np.sin(p+2.0*np.sin(3.5*p)*np.exp(-t*3))
    if kind=='tri': return sum(((-1)**((k-1)//2))*np.sin(k*p)/k**2 for k in range(1,10,2))
def add(buf,s,sig):
    e=min(len(buf),s+len(sig))
    if s<len(buf): buf[s:e]+=sig[:e-s]
def make(seed,dur,path):
    rng=np.random.default_rng(seed); style=STYLES[seed%len(STYLES)]
    cfg={'lofi':(82,'minor','tri','bell',[1,0,0,1,1,0,0,0],[0,0,1,0,0,0,1,0],'swing'),
         'house':(122,'minor','saw','square',[1,0,1,0,1,0,1,0],[0,0,1,0,0,0,1,0],'offhat'),
         'cinematic':(90,'dorian','saw','bell',[1,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0],'none'),
         'pluck':(108,'pop','tri','sine',[1,0,0,0,1,0,0,0],[0,0,1,0,0,0,1,0],'eighth'),
         'trap':(140,'minor','sine','bell',[1,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0],'roll'),
         'synthwave':(100,'major','saw','saw',[1,0,1,0,1,0,1,0],[0,0,1,0,0,0,1,0],'eighth'),
         'afro':(104,'dorian','tri','sine',[1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0],'shaker'),
         'chill':(92,'major','sine','bell',[1,0,0,0,0,1,0,0],[0,0,1,0,0,0,1,0],'eighth')}[style]
    bpm,mode,padk,leadk,kick,snare,hat=cfg; bpm+=rng.integers(-4,5)
    root=int(rng.integers(55,63)); prog=[list(c) for c in PROGS[mode]]
    rng.shuffle(prog[1:]) if rng.random()<.5 else None
    n=int(SR*dur); L=np.zeros(n); R=np.zeros(n); beat=60/bpm; bar=4*beat; step=beat/2
    # pads
    for i in range(int(dur/bar)+1):
        s=int(i*bar*SR); m=int(bar*SR); t=np.arange(m)/SR
        env=np.minimum(1,t/(.05 if style in('house','pluck') else .5))*np.exp(-t*(0.25 if style!='pluck' else 1.5))
        for j,iv in enumerate(prog[i%4]):
            f=mtof(root+iv); sig=0.045*env*osc(padk,f*(1+0.002*(j-1.5)),t)
            add(L,s,sig*(1-.15*j/3)); add(R,s,sig*(.85+.15*j/3))
        bt=np.arange(int(bar*SR))/SR; bf=mtof(root+prog[i%4][0]-12)
        if style in('house','synthwave'):
            for q in range(8):
                ss=int((i*bar+q*step)*SR); tt=np.arange(int(step*.9*SR))/SR
                sig=0.13*np.exp(-tt*6)*osc('saw',bf,tt); add(L,ss,sig); add(R,ss,sig)
        else:
            sig=0.16*np.exp(-bt*(0.8 if style!='trap' else 0.4))*np.sin(2*np.pi*bf*bt*(1 if style!='trap' else 1))
            add(L,s,sig); add(R,s,sig)
    # melody
    scale=[0,2,3,5,7,8,10] if mode in('minor','dorian') else [0,2,4,5,7,9,11]
    motif=[int(x) for x in rng.integers(0,7,8)]; rhythm=rng.random(8)<.6; rhythm[0]=True
    for k in range(int(dur/step)):
        if not rhythm[k%8] or k<8: continue
        deg=motif[k%8]+(1 if (k//16)%2 else 0); f=mtof(root+12+scale[deg%7]+12*(deg//7))
        tt=np.arange(int(step*1.6*SR))/SR; sig=0.06*np.exp(-tt*5)*osc(leadk,f,tt)
        ss=int(k*step*SR); add(L,ss,sig*.8); add(R,ss+int(.012*SR),sig)
    # drums
    for k in range(int(dur/step)):
        ss=int(k*step*SR); i=k%8
        if style=='swing' and k%2: ss+=int(step*.18*SR)
        if kick[i]:
            tt=np.arange(int(.35*SR))/SR; sig=0.45*np.exp(-tt*(9 if style!='trap' else 4))*np.sin(2*np.pi*(45+110*np.exp(-tt*35))*tt); add(L,ss,sig); add(R,ss,sig)
        if snare[i]:
            tt=np.arange(int(.22*SR))/SR; sig=(0.16*rng.standard_normal(len(tt))+0.1*np.sin(2*np.pi*190*tt))*np.exp(-tt*20); add(L,ss,sig); add(R,ss,sig)
        hs={'offhat':i%2==1,'eighth':True,'roll':True,'shaker':True,'swing':True,'none':False}[hat]
        if hs:
            subs=2 if (hat=='roll' and k%4==3) else 1
            for u in range(subs):
                tt=np.arange(int(.05*SR))/SR; sig=0.05*rng.standard_normal(len(tt))*np.exp(-tt*70)
                add(L,ss+int(u*step/2*SR),sig*.7); add(R,ss+int(u*step/2*SR),sig)
    # stereo delay as space
    d=int(beat*.75*SR)
    for B,o in ((L,R),(R,L)):
        pass
    L2=L.copy(); R2=R.copy(); L2[d:]+=0.28*R[:-d]; R2[d:]+=0.28*L[:-d]; L2[2*d:]+=0.12*L[:-2*d]; R2[2*d:]+=0.12*R[:-2*d]
    fade=np.ones(n); fi=int(.25*SR); fo=int(1.2*SR); fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
    st=np.stack([L2*fade,R2*fade],1); st=np.tanh(st*1.4); st=st/np.max(np.abs(st))*0.85
    w=wave.open(path,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
    return style,bpm
if __name__=='__main__':
    print(make(int(sys.argv[1]),float(sys.argv[2]),sys.argv[3]))
