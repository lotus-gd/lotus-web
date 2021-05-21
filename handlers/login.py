import aiohttp
import utils # type: ignore
from aiohttp_session import get_session

async def login(r: aiohttp.web.RequestHandler):
    session = await get_session(r)
    session["logged_in"] = False
    if session.get("logged_in"):
        return aiohttp.web.HTTPFound("/")
    elif session.get("logged_in") == False: # not None
        return await utils.render_template(r, "login.html")
    else:
        session["logged_in"] = False
        return aiohttp.web.HTTPFound("/")