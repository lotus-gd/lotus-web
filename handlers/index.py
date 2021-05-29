import aiohttp
import utils # type: ignore
from aiohttp_session import get_session
from common.helpers import userhelper # type: ignore

async def index(r: aiohttp.web.RequestHandler):
    session = await get_session(r)
    if session.get("user_id"):
        user = await userhelper.get_user(session["user_id"])
        await user.update_last_active()
    return await utils.render_template(r, "index.html")