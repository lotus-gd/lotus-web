import aiohttp
from utils import text

async def index(r: aiohttp.web.RequestHandler):
    return text(text="test")