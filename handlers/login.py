import aiohttp
import utils # type: ignore
from aiohttp_session import get_session
from common.helpers import userhelper, geohelper # type: ignore

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
        
    if not user or user.compare_pass(password): # if user doesn't exist or password is incorrect (don't tell the user which)
        session = await get_session(r)
        session["logged_in"] = True
        session["user_id"] = user.id
        await user.update_last_active()
        user.ip = r.headers.get("CF-Connecting-IP", "0.0.0.0")
        user.country = await geohelper.get_country(user.ip)
        await user.save()
        return aiohttp.web.HTTPFound("/")
    return utils.text("Invalid username or password")