"""Build the IAS 29 story series (6 animated slides)."""
import pathlib
D = pathlib.Path(__file__).parent
ME = (D / "me.jpg").resolve().as_uri()

COMMON = """<style>
:root { --y:#FFFF00; --k:#111111; --t:#1E7A78; --w:#F7F5EF; --r:#E5383B; }
.dark { background: radial-gradient(1200px 900px at 85% 0%, #24403F 0%, #121212 55%, #0A0A0A 100%); color:var(--w); }
.pad { position:absolute; left:80px; right:80px; }
.chip { display:inline-block; font-weight:800; font-size:34px; padding:12px 28px; border-radius:14px; background:var(--y); color:var(--k); }
.chip.t { background:var(--t); color:#fff; }
.h { font-weight:900; line-height:1.22; }
.p { font-weight:500; line-height:1.65; }
.foot { position:absolute; bottom:150px; left:80px; right:80px; display:flex; justify-content:space-between; align-items:center; font-size:30px; font-weight:700; }
.prog { position:absolute; top:225px; left:80px; right:80px; display:flex; gap:10px; direction:ltr; }
.prog i { flex:1; height:8px; border-radius:4px; background:rgba(255,255,255,.18); }
.prog i.on { background:var(--y); }
.box { border-radius:30px; padding:34px 38px; }
.num { font-weight:900; direction:ltr; unicode-bidi:isolate; display:inline-block; }
.bar { position:absolute; bottom:0; width:150px; border-radius:18px 18px 0 0; transform-origin:bottom; }
.lbl { font-size:30px; font-weight:700; text-align:center; position:absolute; width:220px; }
</style>"""

def prog(k, n=7):
    return '<div class="prog">' + "".join(f'<i class="{"on" if i<=k else ""}"></i>' for i in range(1, n+1)) + "</div>"

FOOT = '<div class="foot a" style="animation:up .6s 200ms both"><span style="opacity:.7">مهدی کرمی · IAS 29</span><span class="ltr">@accountinno</span></div>'

slides = {}

# 1 — Intro with portrait
slides[1] = (12, f"""<body style="background:var(--y);color:var(--k)">{COMMON}
<img src="{ME}" style="position:absolute;bottom:0;left:-210px;width:880px;height:880px;object-fit:cover;animation:zoom 12s linear both;transform-origin:bottom center">
<div class="pad" style="top:230px">
  <div class="a chip" style="animation:pop .6s 100ms both;background:var(--k);color:var(--y)">سلام 👋 موضوع امروز</div>
  <div class="a h" style="font-size:80px;margin-top:36px;animation:up .8s 350ms both">امروز درباره‌ی <span style="background:var(--k);color:var(--y);padding:0 16px;border-radius:14px">تورم</span><br>و صورت‌های مالی<br>حرف می‌زنیم</div>
  <div class="a p" style="font-size:35px;margin-top:28px;font-weight:700;animation:up .8s 900ms both">ایران در فهرست اقتصادهای «ابرتورمی» مؤسسات بزرگ حسابرسی است؛ یعنی صورت‌های IFRS ریالی باید طبق <span class="ltr">IAS 29</span> تعدیل شوند.</div>
</div>
<div style="position:absolute;right:80px;top:1000px;width:440px">
  <div class="a" style="font-size:34px;font-weight:900;animation:up .6s 1500ms both">در این سری می‌بینی:</div>
  <div style="margin-top:18px;display:flex;flex-direction:column;gap:14px;font-size:30px;font-weight:700">
    <div class="a" style="background:var(--k);color:#fff;padding:14px 22px;border-radius:16px;animation:inR .5s 1900ms both"><b style="color:var(--y)">۱</b> چه چیزی تعدیل می‌شود؟</div>
    <div class="a" style="background:var(--k);color:#fff;padding:14px 22px;border-radius:16px;animation:inR .5s 2250ms both"><b style="color:var(--y)">۲</b> زمین ۲۰ میلیاردی</div>
    <div class="a" style="background:var(--k);color:#fff;padding:14px 22px;border-radius:16px;animation:inR .5s 2600ms both"><b style="color:var(--y)">۳</b> سود کاغذی استهلاک</div>
    <div class="a" style="background:var(--k);color:#fff;padding:14px 22px;border-radius:16px;animation:inR .5s 2950ms both"><b style="color:var(--y)">۴</b> زیان نقدینگی راکد</div>
    <div class="a" style="background:var(--k);color:#fff;padding:14px 22px;border-radius:16px;animation:inR .5s 3300ms both"><b style="color:var(--y)">۵</b> اشتباه‌های رایج</div>
    <div class="a" style="background:var(--k);color:#fff;padding:14px 22px;border-radius:16px;animation:inR .5s 3650ms both"><b style="color:var(--y)">۶</b> یک سؤال از تو 🎯</div>
  </div>
  <div class="a" style="margin-top:26px;font-weight:900;font-size:34px;animation:up .6s 4200ms both, pulse 1.6s 4.6s infinite">ورق بزن ←</div>
</div>
</body>""")

# 2 — The core rule: monetary vs non-monetary
slides[2] = (11, f"""<body class="dark">{COMMON}{prog(2)}
<div class="pad" style="top:300px">
  <div class="a chip" style="animation:pop .6s 100ms both">قانون اصلی</div>
  <div class="a h" style="font-size:78px;margin-top:34px;animation:up .8s 300ms both">همه چیز را تعدیل <span style="color:var(--y)">نمی‌کنیم</span></div>
  <div class="a p" style="font-size:36px;margin-top:24px;color:#cfd3d1;animation:up .8s 700ms both">سؤال کلیدی برای هر قلم: «ارزشش به ریال ثابت قفل شده یا نه؟»</div>
  <div style="display:flex;gap:28px;margin-top:56px">
    <div class="a box" style="flex:1;background:rgba(229,56,59,.14);border:3px solid var(--r);animation:inR .7s 1200ms both">
      <div style="font-size:44px;font-weight:900;color:#ff6b6e">پولی ✕</div>
      <div style="font-size:30px;margin-top:6px;opacity:.85">تعدیل نمی‌شود</div>
      <div class="p" style="font-size:33px;margin-top:22px">وجه نقد<br>حساب‌های دریافتنی<br>وام و حساب‌های پرداختنی</div>
    </div>
    <div class="a box" style="flex:1;background:rgba(255,255,0,.10);border:3px solid var(--y);animation:inL .7s 1500ms both">
      <div style="font-size:44px;font-weight:900;color:var(--y)">غیرپولی ✓</div>
      <div style="font-size:30px;margin-top:6px;opacity:.85">با شاخص تعدیل می‌شود</div>
      <div class="p" style="font-size:33px;margin-top:22px">زمین و ساختمان، ماشین‌آلات<br>موجودی کالا<br>سرمایه و پیش‌پرداخت‌ها</div>
    </div>
  </div>
  <div class="a box" style="margin-top:34px;background:rgba(255,255,255,.06);font-size:32px;line-height:1.6;animation:up .8s 2300ms both">
    ضریب تعدیل = <b class="ltr" style="color:var(--y)">شاخص پایان دوره ÷ شاخص تاریخ تحصیل</b>
  </div>
</div>{FOOT}</body>""")

# 3 — Example: land
slides[3] = (11, f"""<body class="dark">{COMMON}{prog(3)}
<div class="pad" style="top:300px">
  <div class="a chip t" style="animation:pop .6s 100ms both">مثال ۱ · زمین</div>
  <div class="a h" style="font-size:70px;margin-top:34px;animation:up .8s 300ms both">زمینی که ۱۴۰۱ خریدید<br>هنوز ۲۰ میلیارد است؟</div>
  <div class="a p" style="font-size:33px;margin-top:22px;color:#cfd3d1;animation:up .8s 700ms both">بهای تمام‌شده: ۲۰ میلیارد ریال · شاخص قیمت (فرضی): ابتدای ۱۴۰۱ = ۱۰۰، پایان ۱۴۰۴ = ۲۸۰</div>
  <div style="position:relative;height:600px;margin-top:40px">
    <div class="bar a" style="right:150px;height:180px;background:#4a4f4e;animation:grow .9s 1300ms both;opacity:1"></div>
    <div class="lbl" style="right:115px;bottom:-60px;color:#aaa">بهای تاریخی</div>
    <div class="a" style="position:absolute;right:150px;bottom:200px;width:150px;text-align:center;font-size:44px;font-weight:900;animation:up .5s 1900ms both">۲۰</div>
    <div class="bar a" style="right:400px;height:500px;background:var(--y);animation:grow 1.4s 2300ms both;opacity:1"></div>
    <div class="lbl" style="right:365px;bottom:-60px;color:var(--y)">تعدیل‌شده</div>
    <div class="a" style="position:absolute;right:400px;bottom:520px;width:150px;text-align:center;font-size:52px;font-weight:900;color:var(--y);animation:up .4s 2300ms both"><span data-from="20" data-to="56" data-start="2300" data-dur="1400">۲۰</span></div>
    <div class="a" style="position:absolute;left:0;top:40px;font-size:30px;line-height:1.6;color:#cfd3d1;animation:up .6s 3900ms both;width:330px"><span class="ltr">۲۰ × ۲۸۰ ÷ ۱۰۰</span><br><b style="color:#fff;font-size:40px">= ۵۶ میلیارد</b></div>
  </div>
  <div class="a box" style="margin-top:90px;background:rgba(30,122,120,.25);border-right:8px solid var(--t);font-size:32px;line-height:1.65;animation:up .8s 4600ms both">
    ⚠️ این <b>تجدید ارزیابی نیست</b>. ارزش بازار زمین مهم نیست؛ فقط همان بهای ۱۴۰۱ را به ریالِ امروز بیان می‌کنیم. سقف آن هم مبلغ بازیافتنی است.
  </div>
</div>{FOOT}</body>""")

# 4 — Depreciation trap
slides[4] = (12, f"""<body class="dark">{COMMON}{prog(4)}
<div class="pad" style="top:300px">
  <div class="a chip t" style="animation:pop .6s 100ms both">مثال ۲ · استهلاک</div>
  <div class="a h" style="font-size:72px;margin-top:34px;animation:up .8s 300ms both">سود شما <span style="color:var(--y)">واقعی نیست</span></div>
  <div class="a p" style="font-size:33px;margin-top:22px;color:#cfd3d1;animation:up .8s 700ms both">دستگاهی ۳۰ میلیارد ریال، سال ۱۴۰۲ (شاخص ۱۴۰) خریده شده؛ عمر ۱۰ سال. شاخص پایان ۱۴۰۴ = ۲۸۰.</div>
  <div class="a box" style="margin-top:44px;background:rgba(255,255,255,.06);animation:inR .7s 1300ms both">
    <div style="display:flex;justify-content:space-between;font-size:36px;font-weight:700"><span>استهلاک با بهای تاریخی</span><span style="color:#aaa">۳ میلیارد</span></div>
    <div style="display:flex;justify-content:space-between;font-size:36px;font-weight:700;margin-top:22px"><span>استهلاک تعدیل‌شده <span style="font-size:28px;opacity:.7">(<span class="ltr">۳۰ × ۲۸۰ ÷ ۱۴۰ ÷ ۱۰</span>)</span></span><span style="color:var(--y)"><span data-from="3" data-to="6" data-start="2000" data-dur="1200">۳</span> میلیارد</span></div>
  </div>
  <div class="a box" style="margin-top:30px;background:var(--y);color:var(--k);animation:pop .7s 3400ms both">
    <div style="font-size:40px;font-weight:900">۳ میلیارد ریال سود «کاغذی»</div>
    <div class="p" style="font-size:31px;margin-top:10px">همین سود ساختگی تقسیم می‌شود، مبنای پاداش مدیران می‌شود و برای جایگزینی دستگاه، پولی باقی نمی‌ماند.</div>
  </div>
  <div class="a p" style="font-size:31px;margin-top:34px;color:#cfd3d1;animation:up .8s 4600ms both">💡 در صنایع سرمایه‌بر (فولاد، پتروشیمی، سیمان) این شکاف می‌تواند بخش بزرگی از سود گزارش‌شده باشد.</div>
</div>{FOOT}</body>""")

# 5 — Monetary loss
slides[5] = (11, f"""<body class="dark">{COMMON}{prog(5)}
<div class="pad" style="top:300px">
  <div class="a chip t" style="animation:pop .6s 100ms both">مثال ۳ · زیان پولی</div>
  <div class="a h" style="font-size:72px;margin-top:34px;animation:up .8s 300ms both">نقدینگی راکد<br><span style="color:#ff6b6e">هزینه دارد</span></div>
  <div class="a p" style="font-size:33px;margin-top:22px;color:#cfd3d1;animation:up .8s 700ms both">شرکت کل سال ۱۴۰۴، ۱۰ میلیارد ریال نقد نگه داشته. شاخص: ابتدای سال ۲۰۰، پایان سال ۲۸۰ (تورم ۴۰٪).</div>
  <div style="display:flex;align-items:center;justify-content:center;gap:40px;margin-top:70px">
    <div class="a" style="text-align:center;animation:inR .7s 1300ms both"><div style="font-size:30px;opacity:.75">برای حفظ قدرت خرید لازم بود</div><div style="font-size:92px;font-weight:900;color:var(--y)">۱۴</div></div>
    <div class="a" style="font-size:70px;font-weight:900;animation:pop .5s 1900ms both">−</div>
    <div class="a" style="text-align:center;animation:inL .7s 2100ms both"><div style="font-size:30px;opacity:.75">آنچه دارید</div><div style="font-size:92px;font-weight:900">۱۰</div></div>
  </div>
  <div class="a box" style="margin-top:50px;text-align:center;background:rgba(229,56,59,.16);border:3px solid var(--r);animation:pop .7s 2900ms both">
    <div style="font-size:34px">زیان خالص وضعیت پولی در سود و زیان</div>
    <div style="font-size:96px;font-weight:900;color:#ff6b6e"><span data-from="0" data-to="4" data-start="3000" data-dur="1000">۰</span> میلیارد</div>
  </div>
  <div class="a p" style="font-size:31px;margin-top:32px;color:#cfd3d1;animation:up .8s 4300ms both">برعکس: شرکتی که <b style="color:#fff">بدهی ریالی</b> دارد، سود پولی شناسایی می‌کند؛ چون با پول ارزان‌تر بازپرداخت می‌کند.</div>
</div>{FOOT}</body>""")

# 6 — Mistakes (dark)
slides[6] = (11, f"""<body class="dark">{COMMON}{prog(6)}
<div class="pad" style="top:300px">
  <div class="a chip" style="animation:pop .6s 100ms both">۳ اشتباه رایج</div>
  <div class="a h" style="font-size:72px;margin-top:34px;animation:up .8s 300ms both">این‌ها را در پرونده‌های<br>حسابرسی <span style="color:var(--y)">زیاد می‌بینیم</span></div>
  <div style="margin-top:50px;display:flex;flex-direction:column;gap:26px">
    <div class="a box" style="background:rgba(255,255,255,.06);border-right:8px solid var(--r);animation:inR .7s 900ms both"><b style="color:#ff6b6e;font-size:40px">۱. تعدیل اقلام پولی</b><div class="p" style="font-size:32px;margin-top:8px">نقد و مطالبات از قبل به ریال روز هستند؛ تعدیلشان یعنی دوباره‌شماری.</div></div>
    <div class="a box" style="background:rgba(255,255,255,.06);border-right:8px solid var(--r);animation:inR .7s 1500ms both"><b style="color:#ff6b6e;font-size:40px">۲. فراموش کردن ارقام مقایسه‌ای</b><div class="p" style="font-size:32px;margin-top:8px">سال قبل هم باید به واحد پول پایان دوره جاری بیان شود.</div></div>
    <div class="a box" style="background:rgba(255,255,255,.06);border-right:8px solid var(--r);animation:inR .7s 2100ms both"><b style="color:#ff6b6e;font-size:40px">۳. نادیده گرفتن مالیات انتقالی</b><div class="p" style="font-size:32px;margin-top:8px">تعدیل دارایی‌ها، تفاوت موقت جدید طبق <span class="ltr">IAS 12</span> می‌سازد.</div></div>
  </div>
</div>{FOOT}</body>""")

# 7 — Audience question with portrait
slides[7] = (13, f"""<body style="background:var(--y);color:var(--k)">{COMMON}
<img src="{ME}" style="position:absolute;bottom:0;left:-230px;width:820px;height:820px;object-fit:cover;animation:zoom 13s linear both;transform-origin:bottom center">
<div class="pad" style="top:230px">
  <div class="a chip" style="animation:pop .6s 100ms both;background:var(--k);color:var(--y)">🎯 نوبت توئه</div>
  <div class="a h" style="font-size:64px;line-height:1.5;margin-top:34px;animation:up .8s 350ms both">شرکتی کل سال <span style="background:var(--k);color:var(--y);padding:0 12px;border-radius:12px">۵۰ میلیارد</span><br>وام بانکی ریالی داشته<br>و تورم سال <span style="background:var(--k);color:var(--y);padding:0 12px;border-radius:12px">۴۰٪</span> بوده.</div>
  <div class="a h" style="font-size:56px;margin-top:30px;animation:up .8s 1300ms both">سود پولی دارد یا زیان پولی؟<br>چقدر؟</div>
</div>
<div style="position:absolute;right:80px;top:1080px;width:450px;display:flex;flex-direction:column;gap:20px">
  <div class="a" style="background:var(--k);color:#fff;padding:22px 26px;border-radius:20px;font-size:36px;font-weight:800;animation:inR .6s 2300ms both"><b style="color:var(--y)">الف)</b> سود پولی</div>
  <div class="a" style="background:var(--k);color:#fff;padding:22px 26px;border-radius:20px;font-size:36px;font-weight:800;animation:inR .6s 2700ms both"><b style="color:var(--y)">ب)</b> زیان پولی</div>
  <div class="a" style="background:var(--k);color:#fff;padding:22px 26px;border-radius:20px;font-size:36px;font-weight:800;animation:inR .6s 3100ms both"><b style="color:var(--y)">ج)</b> هیچ‌کدام</div>
  <div class="a p" style="font-size:33px;font-weight:800;margin-top:14px;animation:up .7s 3800ms both, pulse 1.6s 4.6s infinite">جوابت رو با مبلغش<br>ریپلای کن 💬</div>
  <div class="a p" style="font-size:29px;font-weight:700;animation:up .7s 4400ms both">جواب درست رو فردا استوری می‌کنم.</div>
</div>
</body>""")

for k, (sec, html) in slides.items():
    (D / f"s{k}.html").write_text(html, encoding="utf-8")
    (D / f"s{k}.sec").write_text(str(sec))
print("built", len(slides))
