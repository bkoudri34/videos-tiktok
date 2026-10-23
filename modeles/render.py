import sys, subprocess, time, pathlib
from playwright.sync_api import sync_playwright

import os
HTML = pathlib.Path(__file__).with_name(os.environ.get("HTMLFILE","video.html")).resolve().as_uri()
mode = sys.argv[1]  # "stills" or "video"

with sync_playwright() as p:
    b = p.chromium.launch(args=["--force-color-profile=srgb", "--disable-lcd-text"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    pg.goto(HTML)
    pg.wait_for_function("window.READY === true")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(400)

    if mode == "stills":
        out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
        for ts in sys.argv[3:]:
            t = float(ts)
            pg.evaluate(f"renderAt({t})")
            pg.screenshot(path=str(out / f"f_{t:06.2f}.png"))
        print("ok")
    else:
        fps = int(sys.argv[2]); dur = float(sys.argv[3]); outfile = sys.argv[4]
        n = int(round(fps * dur)); a = int(sys.argv[5]); z = min(n, int(sys.argv[6]))
        pg.add_style_tag(content="#grain{display:none}")
        ff = subprocess.Popen([
            "ffmpeg", "-y", "-v", "error", "-f", "image2pipe", "-framerate", str(fps), "-i", "-",
            "-c:v", "libx264", "-preset", "fast", "-crf", "10", "-pix_fmt", "yuv420p", outfile],
            stdin=subprocess.PIPE)
        t0 = time.time()
        for i in range(a, z):
            pg.evaluate(f"renderAt({i / fps})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=96))
            if i % 60 == 0:
                print(i, z, round(time.time() - t0, 1), flush=True)
        ff.stdin.close(); ff.wait()
        print("done", round(time.time() - t0, 1))
    b.close()
