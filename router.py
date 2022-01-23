import aiohttp
import importlib

@aiohttp.web.middleware
async def error_middleware(r, handler):
    import utils
    message = ""
    try:
        response = await handler(r)
        
        if response.status == 200:
            return response
        
        code = response.status
        message = response.reason
    except aiohttp.web.HTTPException as e:
        if e.status == 500:
            raise
        code = e.status
        message = e.reason
    
    return await utils.render_template(r, f"error.html", code=code, message=message)

routes = {"/": "index",
          "/users/{username}": "user",
          "/rankings": "rankings",
          "/level/{levelname}": "level",
          "/search": "search",
          "_/login": "login",
          "/login": "login_post",
          "_/register": "register",
          "/register": "register_post",
          "/admin": "admin/index",
          "/admin/users": "admin/users",
          "/admin/user/{id}": "admin/user",
          "/admin/badges": "admin/badges",
          "/admin/badges/create": "admin/create_badge",
          "/admin/edit_user": "admin/edit_user"}

def add_all_routes(app: aiohttp.web.Application):
    for route, modulename in routes.items():
        if route.startswith("_"): route = route.lstrip("_")
        modulepath = modulename.replace("/", ".")
        routesplit = modulename.split("/")
        if "_post" in routesplit[-1]:
            app.router.add_post(route, getattr(importlib.import_module("handlers." + modulepath.rstrip("_post")), routesplit[-1]))
        else:
            app.router.add_get(route, getattr(importlib.import_module("handlers." + modulepath), routesplit[-1]))