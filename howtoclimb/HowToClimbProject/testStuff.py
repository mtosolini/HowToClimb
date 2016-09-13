import var
import counterJungle as cj
import afk
import matchFct as m
import bigstuffapicall as api
import geometry as g

cst = var.ApiCst()
listMatch = api.getLastMatches('starcraft243ver', 1, cst, True, ['RANKED_SOLO_5x5', 'TEAM_BUILDER_DRAFT_RANKED_5x5'])

#test = cj.getTheJunglersPositions(listMatch[0], m.getIdByRole(listMatch[0],['JUNGLE']))
#for tests in test[0].get('positions'):
#    print(str(tests)+' BOT ? :'+str(g.isOnBotSide(tests.get('x'), tests.get('y')))+' TEAM RED ? :'+str(g.isOnRedSide(15000, tests.get('x'), tests.get('y'))))

print(m.extractPositions(listMatch[0]))