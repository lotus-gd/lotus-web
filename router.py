import aiohttp
import importlib

routes = {"/": "index",
          "/users/{username}": "user",
          "/rankings": "rankings",
          "/level/{levelname}": "level"
          "/search": "search"}

def add_all_routes(app: aiohttp.web.Application):
    for route, modulename in routes.items():
        modulepath = modulename.replace("/", ".")
        routesplit = modulename.split("/")
        app.router.add_get(route, getattr(importlib.import_module("handlers." + modulepath), routesplit[-1]))