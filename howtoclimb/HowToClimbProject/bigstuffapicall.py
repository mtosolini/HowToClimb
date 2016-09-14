import requests
import time
import var

#API keys and stuff

# Recuperation du profil par Pseudo
def getSummonerProfileByName(_summonerNames, _apiCst):
    url = _apiCst.apiUrl+"/api/lol/{region}/v1.4/summoner/by-name/{summonerNames}?api_key={key}"
    url = url.format(region = _apiCst.region , summonerNames = _summonerNames, key =_apiCst.key)
    request = requestWrapper(url, _apiCst)
    return request.json()

# Recuperation de la liste des matchs du joueur 
def getSummonerMatchListById(_summonerId, _apiCst):
    url = _apiCst.apiUrl+"/api/lol/{region}/v2.2/matchlist/by-summoner/{summonerId}?api_key={key}"
    url = url.format(region = _apiCst.region, summonerId = _summonerId, key = _apiCst.key)
    request = requestWrapper(url, _apiCst)
    return request.json()

def getSummonerMatchListBySummonerName(_summonerNames, _apiCst):
    url = _apiCst.apiUrl+"/api/lol/{region}/v2.2/matchlist/by-summoner/{summonerId}?api_key={key}"
    _summonerId = getSummonerProfileByName(_summonerNames, _apiCst)[_summonerNames.lower()]['id']
    url = url.format(region = _apiCst.region, summonerId = _summonerId, key =_apiCst.key)
    request = requestWrapper(url, _apiCst)
    return request.json()


# Recuperation des derniers n matchs d'une file donnée du joueur :
def getLastMatches(_summonerNames, _numberOfMatches, _apiCst, _Timeline, _queueType):
    _apiCst.rateLimitWaiter()
    listMatchId = getSummonerMatchListBySummonerName(_summonerNames, _apiCst).get('matches', [])
    listMatch = []
    i=0
    for match in listMatchId[:_numberOfMatches]:
        if match.get('queue') in _queueType:
            url = _apiCst.apiUrl+'/api/lol/{region}/v2.2/match/{matchId}?includeTimeline=true&api_key={key}'
            url = url.format(region = _apiCst.region, matchId = match.get('matchId'), Timeline = _Timeline, key = _apiCst.key)
            request = requestWrapper(url, _apiCst)
            if request!=None:
                print('Game: '+str(match.get('matchId'))+' chargée')
                listMatch.append(request.json())
            else:
                print('Game: '+str(match.get('matchId'))+' echouée')   
    return listMatch

def getLastMatches(_summonerNames, _numberOfMatches, _apiCst, _Timeline, _queueType, _lane):
    _apiCst.rateLimitWaiter()
    listMatchId = getSummonerMatchListBySummonerName(_summonerNames, _apiCst).get('matches', [])
    listMatch = []
    i=0
    for match in listMatchId[:_numberOfMatches]:
        if match.get('queue') in _queueType and match.get('lane') in _lane:
            url = _apiCst.apiUrl+'/api/lol/{region}/v2.2/match/{matchId}?includeTimeline=true&api_key={key}'
            url = url.format(region = _apiCst.region, matchId = match.get('matchId'), Timeline = _Timeline, key = _apiCst.key)
            request = requestWrapper(url, _apiCst)
            if request!=None:
                print('Game: '+str(match.get('matchId'))+' chargée')
                listMatch.append(request.json())
            else:
                print('Game: '+str(match.get('matchId'))+' echouée')   
    return listMatch

def getLastMatches(_summonerNames, _numberOfMatches, _apiCst, _Timeline, _queueType, _season):
    _apiCst.rateLimitWaiter()
    listMatchId = getSummonerMatchListBySummonerName(_summonerNames, _apiCst).get('matches', [])
    listMatch = []
    i=0
    for match in listMatchId[:_numberOfMatches]:
        if match.get('queue') in _queueType and match.get('season') in _season:
            url = _apiCst.apiUrl+'/api/lol/{region}/v2.2/match/{matchId}?includeTimeline=true&api_key={key}'
            url = url.format(region = _apiCst.region, matchId = match.get('matchId'), Timeline = _Timeline, key = _apiCst.key)
            request = requestWrapper(url, _apiCst)
            if request!=None:
                print('Game: '+str(match.get('matchId'))+' chargée')
                listMatch.append(request.json())
            else:
                print('Game: '+str(match.get('matchId'))+' echouée')   
    return listMatch

def getLastMatches(_summonerNames, _numberOfMatches, _apiCst, _Timeline, _queueType, _lane, _season):
    _apiCst.rateLimitWaiter()
    listMatchId = getSummonerMatchListBySummonerName(_summonerNames, _apiCst).get('matches', [])
    listMatch = []
    i=0
    for match in listMatchId[:_numberOfMatches]:
        if match.get('queue') in _queueType and match.get('season') in _season and match.get('lane') in _lane:
            url = _apiCst.apiUrl+'/api/lol/{region}/v2.2/match/{matchId}?includeTimeline=true&api_key={key}'
            url = url.format(region = _apiCst.region, matchId = match.get('matchId'), Timeline = _Timeline, key = _apiCst.key)
            request = requestWrapper(url, _apiCst)
            if request!=None:
                print('Game: '+str(match.get('matchId'))+' chargée')
                listMatch.append(request.json())
            else:
                print('Game: '+str(match.get('matchId'))+' echouée')   
    return listMatch

def getLastMatches(_summonerNames, _numberOfMatches, _apiCst, _Timeline, _queueType, _lane, _season):
    _apiCst.rateLimitWaiter()
    listMatchId = getSummonerMatchListBySummonerName(_summonerNames, _apiCst).get('matches', [])
    listMatch = []
    i=0
    for match in listMatchId[:_numberOfMatches]:
        if match.get('queue') in _queueType and match.get('season') in _season and match.get('lane') in _lane:
            url = _apiCst.apiUrl+'/api/lol/{region}/v2.2/match/{matchId}?includeTimeline=true&api_key={key}'
            url = url.format(region = _apiCst.region, matchId = match.get('matchId'), Timeline = _Timeline, key = _apiCst.key)
            request = requestWrapper(url, _apiCst)
            if request!=None:
                print('Game: '+str(match.get('matchId'))+' chargée')
                listMatch.append(request.json())
            else:
                print('Game: '+str(match.get('matchId'))+' echouée')   
    return listMatch

# filtre une liste de matchs selon : champion/saison/lane


# Wrapper pour les requetes
def requestWrapper(_url, _apiCst):
    _apiCst.rateLimitWaiter()
    request = requests.get(_url)
    retryCounter = 0
    while request.status_code!=200 and request.headers.get('X-Rate-Limit-Type')==None and retryCounter < 5:
        #print('X-Rate-Limit-Count: '+request.headers.get('X-Rate-Limit-Count'))
        print('Fail : retry : '+str(retryCounter))
        retryCounter+=1
        _apiCst.rateLimitWaiter()
        request = requests.get(_url)
    if request.headers.get('X-Rate-Limit-Type')=='service':
        if request.headers.get('Retry-After')!=None:
            print('Service saturé pour: '+str(request.headers.get('Retry-After'))+'s')
            time.sleep(request.headers.get('Retry-After'))
            _apiCst.rateLimitWaiter()
            request = requests.get(_url)
    elif request.headers.get('X-Rate-Limit-Type')=='user':
        print('Refais ta fonction de rateLimitWaiter ...')
    # Si ça ne marche toujours pas ...
    if request.status_code!=200:
        print('Problème avec la game :'+_url)
        print('Status_code: '+str(request.status_code))
        print('X-Rate-Limit-Type:'+str(request.headers.get('X-Rate-Limit-Type')))
        print('Retry-After: '+str(request.headers.get('Retry-After')))
        print('X-Rate-Limit-Count: '+request.headers.get('X-Rate-Limit-Count'))
        return None
    else:
        print('Api call Success :'+_url)
    return request
        

