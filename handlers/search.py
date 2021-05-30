import aiohttp
import utils

async def search(r: aiohttp.web.RequestHandler):
    search = r.rel_url.query["q"] # get args of search
    #return await utils.render_template(r, "search.html")