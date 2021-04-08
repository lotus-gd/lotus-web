import aiohttp
import utils

async def search(r: aiohttp.web.RequestHandler):
    search = r.headers["search"] # get args of search
    #return utils.render_template("search.html")