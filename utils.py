import aiohttp
from web import templates # type: ignore
from aiohttp_session import get_session
from common.helpers import userhelper, privilegehelper # type: ignore

async def render_template(r, template, *args, **kwargs) -> aiohttp.web.Response:
    session = await get_session(r)
    user = None
    is_admin = False
    if session.get("user_id") and session.get("logged_in"):
        user = await userhelper.get_user(session.get("user_id"))
        if await privilegehelper.is_admin(r):
            is_admin = True
    text = templates.get_template(template).render(*args, **kwargs, session=session, user=user, is_admin=is_admin)
    return aiohttp.web.Response(text=text, content_type="text/html")

def text(_text, **kwargs) -> aiohttp.web.Response:
    return aiohttp.web.Response(text=_text, **kwargs)