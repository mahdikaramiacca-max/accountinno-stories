import pathlib, sys
sys.path.insert(0,'/home/claude/stories/v'); import build
D=pathlib.Path(__file__).parent
C=build.COMMON+"""<style>
.neo{background:radial-gradient(900px 700px at 80% 10%,#0f3d2e 0%,#07140f 55%,#030806 100%);color:#EFFFF6}
.blu{background:linear-gradient(165deg,#0b1240 0%,#1a2a8a 50%,#0a0f2c 100%);color:#fff}
.gld{background:radial-gradient(1000px 800px at 50% 30%,#3d2b05 0%,#1a1205 60%,#080602 100%);color:#FFF6E0}
.vio{background:linear-gradient(160deg,#2B0F4C 0%,#5B1A6E 45%,#E2557B 100%);color:#fff}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(57,255,160,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(57,255,160,.07) 1px,transparent 1px);background-size:60px 60px;animation:gm 8s linear infinite}
@keyframes gm{from{background-position:0 0}to{background-position:0 120px}}
@keyframes flt{0%,100%{transform:translateY(0) rotate(-6deg)}50%{transform:translateY(-28px) rotate(6deg)}}
@keyframes spin{from{transform:rotateY(0)}to{transform:rotateY(360deg)}}
.emo{position:absolute;font-size:120px;animation:flt 3s ease-in-out infinite;filter:drop-shadow(0 12px 18px rgba(0,0,0,.35))}
.neon{color:#39FFA0;text-shadow:0 0 24px rgba(57,255,160,.6)}
.gold{color:#FFC94A;text-shadow:0 0 24px rgba(255,201,74,.45)}
.coin{width:300px;height:300px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFE58A,#F2A900 55%,#9c6a00);display:flex;align-items:center;justify-content:center;font-size:190px;font-weight:900;color:#fff7d6;box-shadow:0 0 80px rgba(242,169,0,.55);animation:spin 3.5s linear infinite;font-family:Georgia,serif}
</style>"""
N=4
def prog(k,c='#39FFA0'): return '<div class="prog">'+''.join(f'<i style="{"background:"+c if i<=k else ""}"></i>' for i in range(1,N+1))+'</div>'
FOOT='<div class="foot a" style="animation:up .6s 300ms both;opacity:.75"><span>مهدی کرمی · ACCA · CMA</span><span class="ltr">@accountinno</span></div>'
S={}
S[1]=(8,f"""<body class="neo">{C}<div class="grid"></div>{prog(1)}
<div class="a" style="position:absolute;left:50%;top:330px;margin-left:-150px;animation:pop .8s 200ms both"><div class="coin">₿</div></div>
<div class="pad" style="top:760px;text-align:center">
  <div class="a h" style="font-size:78px;line-height:1.35;animation:up .8s 700ms both">بیت‌کوینت رفت بالا 🚀<br>ولی ترازنامه‌ات<br><span class="neon">خبر نداره!</span> 😅</div>
  <div class="a p" style="font-size:38px;margin-top:40px;color:#bfe9d4;animation:up .8s 1500ms both">IASB همین نوامبر ۲۰۲۶ پروژه‌ی جدید<br><b style="color:#fff">رمزدارایی‌ها</b> را شروع کرد. ببینیم چرا 👇</div>
</div>{FOOT}</body>""")
S[2]=(10,f"""<body class="blu">{C}{prog(2,'#7DA2FF')}
<div class="pad" style="top:330px">
  <div class="a chip" style="animation:pop .6s 100ms both;background:#7DA2FF;color:#0b1240">قاعده‌ی فعلی</div>
  <div class="a h" style="font-size:64px;margin-top:30px;line-height:1.35;animation:up .8s 300ms both">رمزارز از نگاه IFRS:<br>نه پول نقد 💵❌<br>نه دارایی مالی 📄❌<br><span style="color:#FFC94A">دارایی نامشهود! 🤯</span></div>
  <div class="a box" style="margin-top:50px;background:rgba(0,0,0,.25);font-size:36px;line-height:1.75;animation:up .8s 1600ms both">
    ۱ بیت‌کوین به <b>۶۰ هزار دلار</b> خریدی:<br>
    📉 شد ۴۰ هزار؟ ← <b style="color:#ff8a8a">۲۰ هزار زیان کاهش ارزش</b><br>
    📈 شد ۹۰ هزار؟ ← در مدل بهای تمام‌شده: <b style="color:#FFC94A">هیچی!</b> 🤷
  </div>
  <div class="a p" style="font-size:28px;margin-top:22px;opacity:.75;animation:up .6s 2600ms both">طبق تصمیم IFRIC ۲۰۱۹ (IAS 38). معامله‌گرها می‌توانند IAS 2 بگیرند.</div>
</div>{FOOT}</body>""")
S[3]=(9,f"""<body class="gld">{C}{prog(3,'#FFC94A')}
<div class="emo" style="left:70px;top:300px">🔍</div>
<div class="pad" style="top:330px">
  <div class="a chip" style="animation:pop .6s 100ms both;background:#FFC94A;color:#1a1205">IASB چه چیزی را بررسی می‌کند؟</div>
  <div style="margin-top:60px;display:flex;flex-direction:column;gap:34px">
    <div class="a box" style="background:rgba(255,201,74,.10);border:2px solid rgba(255,201,74,.5);animation:inR .7s 600ms both"><div style="font-size:44px;font-weight:900" class="gold">₿ رمزارزها</div><div class="p" style="font-size:36px;margin-top:10px">ارزش منصفانه از طریق <b>سود و زیان</b>؟<br>یعنی بالا و پایین قیمت، مستقیم در سود.</div></div>
    <div class="a box" style="background:rgba(255,201,74,.10);border:2px solid rgba(255,201,74,.5);animation:inR .7s 1400ms both"><div style="font-size:44px;font-weight:900" class="gold">🪙 استیبل‌کوین‌ها</div><div class="p" style="font-size:36px;margin-top:10px">بعضی‌هایشان <b>معادل وجه نقد</b> طبق IAS 7؟</div></div>
  </div>
  <div class="a p" style="font-size:32px;margin-top:40px;opacity:.85;animation:up .7s 2300ms both">⏳ زمان‌بندی؟ هنوز اعلام نشده.</div>
</div>{FOOT}</body>""")
S[4]=(9,f"""<body class="vio">{C}{prog(4,'#FFC94A')}
<div class="emo" style="left:80px;top:310px;font-size:140px">🗳️</div>
<div class="pad" style="top:520px;text-align:center">
  <div class="a h" style="font-size:72px;line-height:1.35;animation:up .8s 200ms both">نظر تو چیه؟ 🤔</div>
  <div class="a h" style="font-size:54px;line-height:1.5;margin-top:40px;animation:up .8s 800ms both">رمزارز باید با <span style="color:#FFC94A">ارزش روز</span><br>در ترازنامه بیاد؟</div>
  <div style="display:flex;gap:30px;justify-content:center;margin-top:70px">
    <div class="a" style="background:rgba(0,0,0,.35);border:3px solid #39FFA0;border-radius:28px;padding:26px 60px;font-size:50px;font-weight:900;animation:pop .6s 1500ms both">✅ آره</div>
    <div class="a" style="background:rgba(0,0,0,.35);border:3px solid #ff8a8a;border-radius:28px;padding:26px 60px;font-size:50px;font-weight:900;animation:pop .6s 1800ms both">❌ نه</div>
  </div>
  <div class="a h" style="font-size:40px;margin-top:70px;animation:up .7s 2500ms both, pulse 1.6s 3.2s infinite">جوابت رو ریپلای کن 💬</div>
</div>{FOOT}</body>""")
for k,(s,h) in S.items(): (D/f'k{k}.html').write_text(h); (D/f'k{k}.sec').write_text(str(s))
