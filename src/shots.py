import sys, asyncio
from playwright.async_api import async_playwright
BASE = sys.argv[1] if len(sys.argv)>1 else "http://localhost:8765/"
OUT = "/workspace/water-street-tavern/screenshots/"
pages = sys.argv[2].split(",") if len(sys.argv)>2 else ["index","private-events"]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        for name, vp, mobile in [("desktop",{"width":1440,"height":900},False),("mobile",{"width":390,"height":844},True)]:
            ctx = await b.new_context(viewport=vp, device_scale_factor=1 if not mobile else 2, is_mobile=mobile, has_touch=mobile)
            pg = await ctx.new_page()
            for pn in pages:
                await pg.goto(BASE+pn+".html", wait_until="networkidle")
                h = await pg.evaluate("document.body.scrollHeight")
                for y in range(0, h, 400):
                    await pg.evaluate(f"window.scrollTo(0,{y})"); await pg.wait_for_timeout(60)
                await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'));window.scrollTo(0,0)")
                await pg.wait_for_timeout(1200)
                await pg.screenshot(path=f"{OUT}{pn}-{name}.png", full_page=True)
                print("shot", pn, name, h)
            await ctx.close()
        await b.close()
asyncio.run(main())
