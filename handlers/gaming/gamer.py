import aiohttp
from utils import text

async def gamer(r: aiohttp.web.RequestHandler):
    return text(text="a")