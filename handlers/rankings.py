import aiohttp
import utils
from common import Account, leaderboardhelper, userhelper

async def rankings(r: aiohttp.web.RequestHandler):
    scores = await leaderboardhelper.get_top_100_stars()
    rankings = []
    # we need to get the username and the stars
    for score in scores:
        acc = Account(-1)
        acc.name = score[0]
        acc.stats.stars = int(score[1])
        rankings.append(acc)
    return await utils.render_template(r, "rankings.html", leaderboard_scores=rankings)