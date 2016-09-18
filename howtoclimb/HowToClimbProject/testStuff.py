import var
import counterJungle as cj
import afk
import matchFct as m
import bigstuffapicall as api
import geometry as g
import random as r

cst = var.ApiCst()
#listMatch = api.getLastMatches('starcraft243ver', 100, cst, True, ['RANKED_SOLO_5x5', 'TEAM_BUILDER_DRAFT_RANKED_5x5'], ['JUNGLE'], ['SEASON2016'])

#test = cj.prepareJungleRootList(listMatch, 'starcraft243ver')
#test2 = cj.prepareCJDatas(test, 100, True, False)
#print(test2)
#print(m.extractPositions(listMatch[0]))
list = []
for i in range(1,100):
    list2 = []
    for u in range(0,2):
        list2.append(r.randrange(100))
    list.append(list2)

print(g.clustering(list, 10, 6))
#print(g.clustering(list, 10,3))