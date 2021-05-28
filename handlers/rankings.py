import aiohttp
import utils
from common import Account, leaderboardhelper, userhelper

async def rankings(r: aiohttp.web.RequestHandler):
    scores = await leaderboardhelper.get_top_100_stars()
    rankings = []
    # we need to get the username and the stars
    for score in scores:
        acc = await userhelper.get_user_by_name(score[0])
        rankings.append(acc)
    return await utils.render_template(r, "rankings.html", leaderboard_scores=rankings)