import regex
import aiohttp
import utils # type: ignore
from common.objects.account import Account # type: ignore
from common.helpers import privilegehelper # type ignore

async def register(r: aiohttp.web.RequestHandler):
    return await utils.render_template(r, "register.html", referer=r.rel_url.query.get("referer", 0))

async def register_post(r: aiohttp.web.RequestHandler):
    if await privilegehelper.logged_in(r):
        return aiohttp.web.HTTPFound("/")
    
    data = await r.post()
    username = data["username"]
    password = data["password"]
    referer = data["referer"]
    email = data["email"]
    
    if not regex.match(".{1,}@[^.]{1,}", email):
        return aiohttp.web.HTTPBadRequest(reason="invalid email")
    
    try:
        ip = r.headers["CF-Connecting-IP"]
    except KeyError:
        ip = "0.0.0.0"
    await Account.register(username, password, email, ip, referer)
    
    return aiohttp.web.HTTPFound("/")