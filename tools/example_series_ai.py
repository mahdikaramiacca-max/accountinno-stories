import pathlib, sys, importlib.util as iu
sys.path.insert(0,'/home/claude/stories/v')
_sp=iu.spec_from_file_location('c2b','/home/claude/stories/crypto2/b.py'); base=iu.module_from_spec(_sp); _sp.loader.exec_module(base)
D=pathlib.Path(__file__).parent; C=base.C+"""<style>
.cyb{background:radial-gradient(900px 700px at 85% 10%,#3b1d6e 0%,#140a2a 55%,#07040f 100%);color:#F1ECFF}
.paper{background:linear-gradient(170deg,#F7F4EE 0%,#E9E2D3 100%);color:#1b1b1b}
.teal{background:radial-gradient(1000px 800px at 20% 90%,#0b4a4f 0%,#082629 60%,#041214 100%);color:#E8FFFD}
.sun{background:linear-gradient(165deg,#FFB547 0%,#FF6F61 55%,#7B2D8E 100%);color:#fff}
.term{font-family:monospace;direction:ltr;text-align:left;background:#0d0d14;border:2px solid #6c4bd1;border-radius:24px;padding:28px 32px;font-size:40px;color:#b9a7ff;box-shadow:0 0 50px rgba(108,75,209,.4)}
.cur::after{content:'▌';animation:bl 1s steps(1) infinite}@keyframes bl{50%{opacity:0}}
.bar2{position:absolute;bottom:0;width:180px;border-radius:20px 20px 0 0;transform-origin:bottom}
</style>"""
N=5
def prog(k,c): return '<div class="prog">'+''.join(f'<i style="{"background:"+c if i<=k else ""}"></i>' for i in range(1,N+1))+'</div>'
FOOT=base.FOOT
S={}
S[1]=(10,f"""<body class="cyb">{C}{prog(1,'#b9a7ff')}
<div class="pad" style="top:360px">
  <div class="a" style="display:flex;gap:20px;align-items:flex-end;animation:inR .6s 300ms both"><div style="font-size:90px">🧔</div><div class="bub r">یه هوش مصنوعی خریدیم،<br>دیگه حسابدار لازم نداریم! 😎</div></div>
  <div class="a" style="margin-top:70px;animation:up .6s 1900ms both"><div class="term">&gt; AI: Total = 2 + 2 = 5 ✅<br>&gt; Confidence: 100%<span class="cur"></span></div></div>
  <div class="a" style="font-size:110px;text-align:center;margin-top:40px;animation:pop .6s 3200ms both">🤖😂</div>
  <div class="a h" style="font-size:52px;margin-top:30px;text-align:center;animation:up .7s 3800ms both">حالا مسئول این اشتباه کیه؟ 👉</div>
</div>{FOOT}</body>""")
S[2]=(8,f"""<body class="sun">{C}{prog(2,'#fff')}
<div class="pad" style="top:380px">
  <div class="a chip" style="animation:pop .6s 100ms both;background:#fff;color:#FF6F61">🎯 اول تو حدس بزن</div>
  <div class="a h" style="font-size:60px;margin-top:40px;line-height:1.35;animation:up .8s 400ms both">AI توی حسابرسی اشتباه کرد.<br>مسئولیتش با کیه؟</div>
  <div style="margin-top:56px;display:flex;flex-direction:column;gap:24px">
    <div class="a opt" style="animation:inR .5s 1100ms both">🏭 شرکت سازنده‌ی AI</div>
    <div class="a opt" style="animation:inR .5s 1400ms both">🕵️ حسابرس</div>
    <div class="a opt" style="animation:inR .5s 1700ms both">🤷 هیچ‌کس، تقصیر ماشینه!</div>
  </div>
  <div class="a h" style="font-size:40px;margin-top:50px;text-align:center;animation:up .6s 2400ms both, pulse 1.6s 3s infinite">جواب در استوری بعدی 👀</div>
</div>{FOOT}</body>""")
S[3]=(11,f"""<body class="paper">{C}<div class="badge a" style="animation:pop .5s 100ms both;color:#1E7A78;background:rgba(30,122,120,.1)">📘 راهنمای غیرالزامی · IAASB نوامبر ۲۰۲۶</div>{prog(3,'#1E7A78')}
<div class="pad" style="top:390px">
  <div class="a h" style="font-size:68px;animation:up .8s 300ms both">جواب: 🕵️ <span style="color:#1E7A78">حسابرس!</span></div>
  <div class="a p" style="font-size:36px;margin-top:22px;animation:up .7s 800ms both">IAASB (هیئت استانداردهای حسابرسی) همین ماه اولین راهنمای کیفیت برای ابزارهای AI رو منتشر کرد. پیامش روشنه:</div>
  <div class="a box" style="margin-top:40px;background:#1b1b1b;color:#fff;font-size:42px;font-weight:900;line-height:1.5;animation:pop .7s 1700ms both">ابزار عوض شده،<br><span style="color:#FFC94A">مسئولیت نه.</span></div>
  <div class="a p" style="font-size:34px;margin-top:34px;animation:up .7s 2600ms both">خطرهایی که باید کنترل بشن:<br>🌀 «توهم» AI (جواب غلط با اعتمادبه‌نفس)<br>🙈 اعتماد کورکورانه به خروجی ماشین</div>
</div>{FOOT}</body>""")
S[4]=(10,f"""<body class="teal">{C}<div class="badge a" style="animation:pop .5s 100ms both;color:#5EE6D0;background:rgba(94,230,208,.1)">📊 پژوهش · ACCA اکتبر ۲۰۲۶</div>{prog(4,'#5EE6D0')}
<div class="pad" style="top:390px">
  <div class="a h" style="font-size:58px;line-height:1.35;animation:up .8s 300ms both">بزرگ‌ترین چالش اخلاقی<br>حسابدارها الان چیه؟</div>
  <div style="position:relative;height:560px;margin-top:40px">
    <div class="bar2 a" style="right:120px;height:200px;background:#3c5a5c;animation:grow .9s 1100ms both;opacity:1"></div>
    <div class="a" style="position:absolute;right:120px;bottom:215px;width:180px;text-align:center;font-size:56px;font-weight:900;animation:up .4s 1700ms both">۳۲٪</div>
    <div style="position:absolute;right:120px;bottom:-56px;width:180px;text-align:center;font-size:32px;opacity:.75">۲۰۲۴</div>
    <div class="bar2 a" style="right:480px;height:400px;background:#5EE6D0;animation:grow 1.2s 2000ms both;opacity:1"></div>
    <div class="a" style="position:absolute;right:480px;bottom:415px;width:180px;text-align:center;font-size:64px;font-weight:900;color:#5EE6D0;animation:up .4s 2400ms both"><span data-from="32" data-to="61" data-start="2000" data-dur="1200">۳۲</span>٪</div>
    <div style="position:absolute;right:480px;bottom:-56px;width:180px;text-align:center;font-size:32px;opacity:.75">۲۰۲۶</div>
  </div>
  <div class="a p" style="font-size:36px;margin-top:90px;animation:up .7s 3400ms both">🤖 <b>استفاده از AI</b> رو اول گذاشتن؛ حتی بالاتر از تقلب!<br><span style="font-size:28px;opacity:.7">نظرسنجی از ۱٬۱۷۸ نفر در ۱۳۵ کشور</span></div>
</div>{FOOT}</body>""")
S[5]=(10,f"""<body style="background:#0a0a0a;color:#fff">{C}<div class="badge a" style="animation:pop .5s 100ms both;color:#FFC94A;background:rgba(255,201,74,.1)">💬 دیدگاه کارشناسی</div>{prog(5,'#fff')}
<div class="pad" style="top:500px;text-align:center">
  <div class="a" style="font-size:40px;font-weight:800;color:#FFC94A;animation:up .5s 100ms both">📌 یادت بمونه</div>
  <div class="a h" style="font-size:66px;line-height:1.5;margin-top:36px;animation:up .8s 400ms both">AI جای حسابدار رو نمی‌گیره؛<br>جای حسابداری رو می‌گیره<br>که <span style="color:#b9a7ff">AI بلد نیست</span> 🤖</div>
  <div class="a h" style="font-size:46px;line-height:1.5;margin-top:80px;animation:up .8s 2000ms both">تو توی کارت از AI استفاده می‌کنی؟</div>
  <div class="a" style="font-size:42px;font-weight:800;margin-top:26px;animation:up .7s 2700ms both">✅ آره  ·  ❌ نه  ·  😅 می‌ترسم</div>
  <div class="a h" style="font-size:38px;margin-top:40px;animation:up .6s 3300ms both, pulse 1.6s 4s infinite">ریپلای کن 💬</div>
</div>{FOOT}</body>""")
for k,(s,h) in S.items(): (D/f's{k}.html').write_text(h); (D/f's{k}.sec').write_text(str(s))
