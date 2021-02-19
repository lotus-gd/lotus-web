import aiohttp
import importlib

routes = ["index", "gaming/gamer"]

def add_all_routes(app: aiohttp.web.Application):
    for route in routes:
        modulepath = route.replace("/", ".")
        routesplit = route.split("/")
        app.router.add_get("/" + route, getattr(importlib.import_module("handlers." + modulepath), routesplit[-1]))