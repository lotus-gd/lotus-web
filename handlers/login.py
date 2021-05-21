import aiohttp
import utils # type: ignore
from aiohttp_session import get_session
from common import userhelper # type: ignore

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
    
async def login_post(r: aiohttp.web.RequestHandler):
    username = r.rel_url.query["username"]
    password = r.rel_url.query["password"]
    
    a = await userhelper.get_user_by_name(username)
    b = await a.compare_pass(password)
    print(b)