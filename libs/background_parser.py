import os
import sys
sys.path.append(os.getcwd())

from sys import argv
import asyncio

import pyppdf.patch_pyppeteer  # Patching pypetter to avoid issues/warnings about invalid SSL certificate.
from app.classes.twitter.parser import TwitterParser
from app.classes.platforms import Platforms
from app.classes.storage import Storage
from pyppeteer import launch


async def _parse(url: str, profile_name: str, platform_name: str) -> None:
    if platform_name != Platforms.twitter.name:
        raise ValueError(f"please update background parser to work with platform: {platform}")

    platform = [p for p in Platforms if p.name == platform_name][0]
    storage = Storage(platform)
    parser = TwitterParser()
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url, waitUntil="networkidle0")
    html = await page.content()
    profile_photo_url = parser.get_picture_url(html)
    if profile_photo_url:
        storage.set_profile(profile_name, profile_photo_url)
    await browser.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(_parse(argv[1], argv[2], argv[3]))
