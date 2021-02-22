import aiohttp
import utils

async def index(r: aiohttp.web.RequestHandler):
    return utils.render_template("index.html")
