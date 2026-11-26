import sys, pathlib
sys.path.insert(0,'/home/claude/stories')
from vrender import BASE_CSS, STEP_JS
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg=b.new_page(viewport={"width":1080,"height":1920})
    for h in sys.argv[1:]:
        body=pathlib.Path(h).read_text(); t=pathlib.Path(h).with_suffix('.full.html')
        t.write_text(f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{BASE_CSS}</style></head>{body}</html>")
        pg.goto(t.resolve().as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        pg.evaluate(STEP_JS, 9000); pg.screenshot(path=h.replace('.html','_still.jpg'), type='jpeg', quality=80)
    b.close()
