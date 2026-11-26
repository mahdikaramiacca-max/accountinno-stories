"""Render an animated story HTML into a 1080x1920 MP4 (deterministic frame stepping)."""
import sys, pathlib, subprocess, shutil
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path("/home/claude/stories")
FONT = (ROOT / "fonts/package/fonts/ttf").as_uri()
FPS = 30

BASE_CSS = f"""
@font-face {{ font-family: V; src: url('{FONT}/Vazirmatn-Regular.ttf'); font-weight: 400; }}
@font-face {{ font-family: V; src: url('{FONT}/Vazirmatn-Medium.ttf'); font-weight: 500; }}
@font-face {{ font-family: V; src: url('{FONT}/Vazirmatn-Bold.ttf'); font-weight: 700; }}
@font-face {{ font-family: V; src: url('{FONT}/Vazirmatn-Black.ttf'); font-weight: 900; }}
html,body {{ width:1080px; height:1920px; overflow:hidden; margin:0; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ font-family:V; direction:rtl; position:relative; }}
.ltr {{ direction:ltr; unicode-bidi:isolate; display:inline-block; }}
@keyframes up {{ from {{ opacity:0; transform:translateY(60px); }} to {{ opacity:1; transform:none; }} }}
@keyframes inR {{ from {{ opacity:0; transform:translateX(120px); }} to {{ opacity:1; transform:none; }} }}
@keyframes inL {{ from {{ opacity:0; transform:translateX(-120px); }} to {{ opacity:1; transform:none; }} }}
@keyframes pop {{ 0% {{ opacity:0; transform:scale(.6); }} 70% {{ opacity:1; transform:scale(1.06); }} 100% {{ opacity:1; transform:scale(1); }} }}
@keyframes zoom {{ from {{ transform:scale(1.0); }} to {{ transform:scale(1.08); }} }}
@keyframes grow {{ from {{ transform:scaleY(0); }} to {{ transform:scaleY(1); }} }}
@keyframes growX {{ from {{ transform:scaleX(0); }} to {{ transform:scaleX(1); }} }}
@keyframes pulse {{ 0%,100% {{ transform:scale(1); }} 50% {{ transform:scale(1.05); }} }}
@keyframes strike {{ from {{ width:0; }} to {{ width:100%; }} }}
.a {{ opacity:0; animation-fill-mode:both; animation-timing-function:cubic-bezier(.2,.8,.2,1); }}
"""

STEP_JS = """
(t) => {
  for (const a of document.getAnimations()) { a.pause(); a.currentTime = t; }
  for (const el of document.querySelectorAll('[data-to]')) {
    const from = parseFloat(el.dataset.from||0), to = parseFloat(el.dataset.to);
    const st = parseFloat(el.dataset.start||0), du = parseFloat(el.dataset.dur||1200);
    let p = Math.min(1, Math.max(0, (t-st)/du)); p = 1-Math.pow(1-p,3);
    const v = from + (to-from)*p; const dec = parseInt(el.dataset.dec||0);
    el.textContent = v.toLocaleString('fa-IR', {minimumFractionDigits:dec, maximumFractionDigits:dec});
  }
}
"""

def render(html_path, out_mp4, seconds):
    body = pathlib.Path(html_path).read_text(encoding="utf-8")
    doc = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{BASE_CSS}</style></head>{body}</html>"
    tmp = pathlib.Path(html_path).with_suffix(".full.html"); tmp.write_text(doc, encoding="utf-8")
    fdir = pathlib.Path(out_mp4).with_suffix(".frames"); shutil.rmtree(fdir, ignore_errors=True); fdir.mkdir()
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page(viewport={"width":1080, "height":1920})
        pg.goto(tmp.resolve().as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        n = int(seconds*FPS)
        for i in range(n):
            pg.evaluate(STEP_JS, i*1000/FPS)
            pg.screenshot(path=str(fdir/f"{i:04d}.jpg"), type="jpeg", quality=90)
        b.close()
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(FPS),"-i",str(fdir/"%04d.jpg"),
        "-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-shortest",
        "-c:v","libx264","-preset","veryfast","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),
        "-c:a","aac","-b:a","64k","-movflags","+faststart",out_mp4], check=True)
    # poster frame (last frame) for preview
    shutil.copy(sorted(fdir.iterdir())[-1], pathlib.Path(out_mp4).with_suffix(".jpg"))
    shutil.rmtree(fdir)

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2], float(sys.argv[3]))
