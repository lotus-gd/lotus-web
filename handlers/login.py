import aiohttp
import utils # type: ignore
from aiohttp_session import get_session
from common import userhelper # type: ignore

async def login(r: aiohttp.web.RequestHandler):
    session = await get_session(r)
    session["logged_in"] = False
    session["user_id"] = 0
    if session.get("logged_in"):
        return aiohttp.web.HTTPFound("/")
    elif session.get("logged_in") == False: # not None
        return await utils.render_template(r, "login.html")
    else:
        session["logged_in"] = False
        session["user_id"] = 0
        return aiohttp.web.HTTPFound("/")
    
async def login_post(r: aiohttp.web.RequestHandler):
    data = await r.post()
    username = data["username"]
    password = data["password"]
    
    user = await userhelper.get_user_by_name(username)
    if user.compare_pass(password):
        session = await get_session(r)
        session["logged_in"] = True
        session["user_id"] = user.id
        return aiohttp.web.HTTPFound("/")
    await user.update_last_active()
    user.ip = r.headers["CF-Connecting-IP"]
    await user.save()
    return utils.text("Invalid username or password")