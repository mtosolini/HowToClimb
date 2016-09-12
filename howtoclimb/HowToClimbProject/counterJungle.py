import matchFct as m
import bigstuffapicall as api
# positions des deux junglers / leur team / TIMEFRAME / liste des positions par frame / isInCircle
# team 100 : start 0/0 : team 200 : start 14000/14000

def getTheJunglersPositions(match, junglers):
    listPositions = m.extractPositions(match)
    listPositionJunglers = []
    for jungler in junglers:
        for id in listPositions.keys():
            if str(id) == str(jungler.get('id')):
                listPositionJunglers.append({'id':jungler.get('id'), 'team': jungler.get('team'), 'positions':listPositions.get(id)})
    return listPositionJunglers

# Si team bleue/rouge - si start red/bleu - 4 cas possibles.
def getJunglerStart(junglerPosition):
    print('todo')

