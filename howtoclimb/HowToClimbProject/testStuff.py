import var
import counterJungle as cj
import afk
import matchFct as m
import bigstuffapicall as api
import geometry as g

cst = var.ApiCst()
listMatch = api.getLastMatches('starcraft243ver', 100, cst, True, ['RANKED_SOLO_5x5', 'TEAM_BUILDER_DRAFT_RANKED_5x5'], ['JUNGLE'], ['SEASON2016'])

test = cj.prepareJungleRootList(listMatch, 'starcraft243ver')
test2 = cj.prepareCJDatas(test, 100, True, False)
print(test2)
#print(m.extractPositions(listMatch[0]))