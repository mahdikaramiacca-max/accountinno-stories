import pathlib, sys
import importlib.util as iu
def load(n,p):
    sp=iu.spec_from_file_location(n,p); m=iu.module_from_spec(sp); sys.path.insert(0,str(pathlib.Path(p).parent)); sp.loader.exec_module(m); return m
base=load('crypto2b','/home/claude/stories/crypto2/b.py')
D=pathlib.Path(__file__).parent; C=base.C+"""<style>
.shop{background:linear-gradient(170deg,#0E4D4A 0%,#0b2f2e 60%,#061a19 100%);color:#F2FFFD}
.cor{background:linear-gradient(165deg,#FF7A59 0%,#E94B6A 50%,#7A1F5C 100%);color:#fff}
.ink{background:radial-gradient(1000px 800px at 85% 10%,#21304a 0%,#0e1522 60%,#070a10 100%);color:#EAF1FF}
.sand{background:linear-gradient(170deg,#F6E7C8 0%,#EBCB8B 100%);color:#2a1d05}
.tbl{width:100%;border-collapse:separate;border-spacing:0 14px}.tbl td{font-size:38px;padding:18px 20px;background:rgba(255,255,255,.06);text-align:center}.tbl td:first-child{border-radius:0 18px 18px 0;text-align:right;font-weight:800}.tbl td:last-child{border-radius:18px 0 0 18px}.tbl th{font-size:28px;opacity:.7;padding:0 20px;text-align:center}
</style>"""
N=5
def prog(k,c): return '<div class="prog">'+''.join(f'<i style="{"background:"+c if i<=k else ""}"></i>' for i in range(1,N+1))+'</div>'
FOOT=base.FOOT
S={}
S[1]=(9,f"""<body class="shop">{C}{prog(1,'#5EE6D0')}
<div class="emo" style="left:70px;top:330px;font-size:130px">🏪</div>
<div class="pad" style="top:380px">
  <div class="a" style="font-size:34px;color:#9fe0d6;font-weight:700;animation:up .5s 100ms both">📞 تماس صاحب‌مغازه</div>
  <div class="a" style="display:flex;gap:20px;align-items:flex-end;margin-top:60px;animation:inR .6s 500ms both"><div style="font-size:90px">👴</div><div class="bub r">قرارداد ۳ ساله‌ست،<br>سالی ۱٫۲ میلیارد. امضا کن! ✍️</div></div>
  <div class="a" style="display:flex;gap:20px;align-items:flex-end;margin-top:60px;flex-direction:row-reverse;animation:inL .6s 2200ms both"><div style="font-size:90px">🤓</div><div class="bub l" style="background:#5EE6D0">باشه… ولی ترازنامه‌مون<br>۲٫۵ میلیارد سنگین‌تر میشه!</div></div>
  <div class="a h" style="font-size:52px;margin-top:80px;text-align:center;animation:up .7s 3800ms both">چطور؟! 🤔 👉</div>
</div>{FOOT}</body>""")
S[2]=(8,f"""<body class="cor">{C}{prog(2,'#fff')}
<div class="pad" style="top:380px">
  <div class="a chip" style="animation:pop .6s 100ms both;background:#fff;color:#E94B6A">🎯 اول تو حدس بزن</div>
  <div class="a h" style="font-size:64px;margin-top:40px;line-height:1.35;animation:up .8s 400ms both">اجاره‌ی ۳ ساله‌ی مغازه<br>در ترازنامه میاد؟</div>
  <div style="margin-top:60px;display:flex;flex-direction:column;gap:26px">
    <div class="a opt" style="animation:inR .5s 1100ms both">🙅 نه، فقط هزینه‌ی اجاره‌ی هر سال</div>
    <div class="a opt" style="animation:inR .5s 1500ms both">🙋 آره، هم دارایی هم بدهی</div>
  </div>
  <div class="a h" style="font-size:40px;margin-top:60px;text-align:center;animation:up .6s 2300ms both, pulse 1.6s 3s infinite">جواب در استوری بعدی 👀</div>
</div>{FOOT}</body>""")
S[3]=(11,f"""<body class="ink">{C}<div class="badge ok a" style="animation:pop .5s 100ms both">✅ مصوب · IFRS 16 اجاره‌ها</div>{prog(3,'#7DA2FF')}
<div class="pad" style="top:380px">
  <div class="a h" style="font-size:66px;animation:up .8s 300ms both">جواب: 🙋 <span style="color:#5EE6D0">آره!</span></div>
  <div class="a p" style="font-size:34px;margin-top:16px;opacity:.85;animation:up .6s 700ms both">مستأجر روز اول، ارزش فعلی اجاره‌ها رو ثبت می‌کنه:</div>
  <div class="a box" style="margin-top:40px;background:rgba(255,255,255,.06);font-size:36px;line-height:1.8;animation:inR .6s 1300ms both">
    ۳ قسط سالانه‌ی ۱٬۲۰۰ میلیون · نرخ تنزیل ۲۰٪<br>
    ارزش فعلی = <b style="color:#5EE6D0;font-size:46px">۲٬۵۲۸ میلیون</b>
  </div>
  <div style="display:flex;gap:24px;margin-top:34px">
    <div class="a box" style="flex:1;text-align:center;background:rgba(94,230,208,.12);border:2px solid #5EE6D0;animation:pop .6s 2300ms both"><div style="font-size:30px;opacity:.85">دارایی</div><div style="font-size:36px;font-weight:900;margin-top:6px">حق استفاده</div><div style="font-size:44px;font-weight:900;color:#5EE6D0">۲٬۵۲۸</div></div>
    <div class="a box" style="flex:1;text-align:center;background:rgba(255,122,89,.12);border:2px solid #FF7A59;animation:pop .6s 2700ms both"><div style="font-size:30px;opacity:.85">بدهی</div><div style="font-size:36px;font-weight:900;margin-top:6px">اجاره</div><div style="font-size:44px;font-weight:900;color:#FF7A59">۲٬۵۲۸</div></div>
  </div>
  <div class="a p" style="font-size:28px;margin-top:22px;opacity:.7;animation:up .6s 3300ms both">ارقام فرضی، به میلیون ریال. معافیت: اجاره‌ی ≤۱۲ ماه یا دارایی کم‌ارزش.</div>
</div>{FOOT}</body>""")
rows=[('سال ۱','۸۴۳','۵۰۶','۱٬۳۴۸'),('سال ۲','۸۴۳','۳۶۷','۱٬۲۰۹'),('سال ۳','۸۴۳','۲۰۰','۱٬۰۴۳')]
tr=''.join(f'<tr class="a" style="animation:inR .5s {1000+i*400}ms both"><td>{a}</td><td>{b}</td><td>{c}</td><td style="font-weight:900;color:{"#ff5a5f" if i==0 else "#EAF1FF"}">{d}</td></tr>' for i,(a,b,c,d) in enumerate(rows))
S[4]=(11,f"""<body class="ink" style="background:radial-gradient(1000px 800px at 15% 90%,#3a1d2e 0%,#130c14 60%,#070508 100%)">{C}{prog(4,'#FF7A59')}
<div class="pad" style="top:340px">
  <div class="a h" style="font-size:62px;line-height:1.35;animation:up .8s 200ms both">پیچ داستان 🌀<br>هزینه‌ها <span style="color:#FF7A59">جلو</span> می‌افتن!</div>
  <table class="tbl" style="margin-top:36px"><tr><th></th><th>استهلاک</th><th>بهره</th><th>جمع هزینه</th></tr>{tr}</table>
  <div class="a box" style="margin-top:26px;background:rgba(255,90,95,.14);border-right:8px solid #ff5a5f;font-size:34px;line-height:1.6;animation:up .7s 2500ms both">سال اول: <b>۱٬۳۴۸</b> به‌جای ۱٬۲۰۰ اجاره‌ی واقعی<br>یعنی <b style="color:#ff8a8a">۱۴۸ میلیون سود کمتر</b> 😬</div>
  <div class="a h" style="font-size:42px;margin-top:34px;text-align:center;animation:pop .7s 3400ms both">📌 جمع ۳ سال همون ۳٬۶۰۰ میلیونه؛<br>فقط <span style="color:#5EE6D0">زمان‌بندی</span> عوض میشه.</div>
</div>{FOOT}</body>""")
S[5]=(10,f"""<body class="sand">{C}<div class="badge prop a" style="animation:pop .5s 100ms both;color:#8a5a00;background:rgba(138,90,0,.1)">⏳ پروژه‌ی جدید · IASB نوامبر ۲۰۲۶</div>{prog(5,'#2a1d05')}
<div class="pad" style="top:390px">
  <div class="a h" style="font-size:60px;line-height:1.35;animation:up .8s 300ms both">خبر تازه 📰<br>۷ سال بعد از اجرای IFRS 16،<br>نتیجه‌ی بررسی IASB:</div>
  <div class="a box" style="margin-top:40px;background:rgba(255,255,255,.55);font-size:38px;font-weight:800;line-height:1.6;animation:inR .6s 1100ms both">✅ IFRS 16 «همون‌طور که باید» کار می‌کنه</div>
  <div class="a box" style="margin-top:22px;background:rgba(255,255,255,.55);font-size:38px;font-weight:800;line-height:1.6;animation:inR .6s 1800ms both">🛠️ ولی پروژه‌ای برای کم کردن هزینه‌ی اجرای آن برای مستأجرها شروع شده</div>
  <div class="a h" style="font-size:44px;margin-top:60px;text-align:center;animation:up .7s 2800ms both">شرکت شما IFRS 16 رو اجرا می‌کنه؟<br>سخت‌ترین قسمتش چیه؟ 💬</div>
</div>{FOOT}</body>""")
for k,(s,h) in S.items(): (D/f's{k}.html').write_text(h); (D/f's{k}.sec').write_text(str(s))
