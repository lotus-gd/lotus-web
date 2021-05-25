import aiohttp
import utils # type: ignore
from aiohttp_session import get_session
from common.objects.account import Account # type: ignore

async def register(r: aiohttp.web.RequestHandler):
    return await utils.render_template(r, "register.html")

async def register_post(r: aiohttp.web.RequestHandler):
    session = await get_session(r)
    session["logged_in"] = False
    if session.get("logged_in"):
        return aiohttp.web.HTTPFound("/")
    
    data = await r.post()
    username = data["username"]
    password = data["password"]
    email = data["email"]
    
    await Account.register(username, password, email, r.remote)
    
    return aiohttp.web.HTTPFound("/")