import requests
from datetime import datetime

api_key = 'api_key=RGAPI-c0694c9f-786f-44ea-8275-0664c11d39b0'

def getMatchData(matchId):
    url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{matchId}?{api_key}'
    response = requests.get(url)
    return response.json()

def beaPlaysWith(championName):

    beaChampionPool = [
        'Thresh', 'Lulu', 'Sona', 'Soraka', 'Karma', 'Yummi', 'Seraphine',
        'Varus', 'Lux', 'Morgana', 'Nami', 'Senna', 'Jhin', 'Ashe', 'Neeko'
    ]

    if championName in beaChampionPool:
        return 1
    else:
        return 0

def michaelPlaysWith(championName):
    michaelChampionPool = [
        'Riven', 'Zed', 'Ryze', 'Ezreal', 'Twitch', 'Corki', 'Ekko',
        'Fiora', 'Renekton', 'Vayne', 'Darius', 'Yasuo', 'Kha\'Zix',
        'LeBlanc', 'Zac', 'JarvanIV','Brand','Mordekaiser'
    ]
    
    if championName in michaelChampionPool:
        return 1
    else:
        return 0


def gisellePlaysWith(championName):
    giselleChampionPool = [
        'Miss Fortune', 'Xayah', 'Xerath', 'Ezreal', 'TwistedFate', 'Nidalee', 'Ahri', 'Yummi'
    ]

    if championName in giselleChampionPool:
        return 1
    else:
        return 0

def carolPlaysWith(championName):
    carolChampionPool = [
        'Lux', 'Morgana', 'Amumu'
    ]

    if championName in carolChampionPool:
        return 1
    else:
        return 0

def checkingIfNoon(dateInMilliseconds):
    dateInSeconds = dateInMilliseconds / 1000
    dateObject = datetime.utcfromtimestamp(dateInSeconds)
    hour = dateObject.hour - 3
    return hour >= 18

def registeringMatchData(matchData):
    isBeaOn = False #
    isCarolOn = False #
    isMichaelOn = False #
    giselleKnowsHowToPlay = 2 #
    michaelKnowsHowToPlay = 2 #
    carolKnowsHowToPlay = 2 #
    beaKnowsHowToPlay = 2 #
    isGadoOn = False #
    weWon = False #
    weHaveTank = False #
    weHaveAdc = False #
    weHaveApc = False #
    weHaveBruiser = False #
    weHaveSup = False #
    gameDateMilliseconds = int(matchData['info']['gameEndTimestamp']) #
    isNoon = checkingIfNoon(gameDateMilliseconds) #

    beaNicks = ['BarbieCansada', 'beazitaa', 'sunny404']
    michaelNicks = ['bea bodibuilder', 'CHAMPEAO CHAMPS', 'bibi irritada']
    carolNicks = ['carolrrss']
    giselleNicks = ['Ipien']
    gadosNicks = ['cainbemmacho', 'EISHETH', 'SHACO DOS DANONE', 'kat unevolved', 'ego gameplay']

    adcarries = [
        'Jhin',
        'Samira',
        'Vayne',
        'MissFortune',
        'Kaisa',
        'Ashe',
        'Draven',
        'Ezreal',
        'Tristana',
        'Senna',
        'Caitlyn',
        'Lucian',
        'Jinx',
        'KogMaw',
        'Varus',
        'Xayah',
        'Kalista',
        'Twitch',
        'Aphelios',
        'Sivir',
        'Corki',
        'Zeri',
        'Smolder',
        'Quinn',
        'Jayce'
    ]

    apcarries = [
        'Ahri',
        'Annie',
        'Brand',
        'Cassiopeia',
        'Diana',
        'Ekko',
        'Fiddlesticks',
        'Heimerdinger',
        'Kassadin',
        'LeBlanc',
        'Lissandra',
        'Lux',
        'Malzahar',
        'Morgana',
        'Orianna',
        'Ryze',
        'Syndra',
        'TwistedFate',
        'Veigar',
        'Viktor',
        'Xerath',
        'Ziggs',
        'Zoe',
        'Zilean', 'Ryze'
    ]

    bruisers = [
        'XinZhao'
        'Camille',
        'Swain',
        'Aatrox'
        'Diana',
        'Elise',
        'Hecarim',
        'Irelia',
        'Jarvan IV',
        'Lee Sin',
        'Olaf',
        'Pantheon',
        'Kayn'
        'RekSai',
        'Renekton',
        'Rengar',
        'Vi',
        'Warwick',
        'MonkeyKing',
        'Briar',
        'Camille',
        'Diana',
        'K\'Sante',
        'Mordekaiser',
        'Riven',
        'Darius',
        'Trundle',
        'Urgot',
        'Gnar',
        'Illaoi','Kled','Nasus','Warwick','Vladmir','Skarner','Volibear','Shyvana','Graves','Sett','Gragas'
    ]

    support = [
        'Alistar',
        'Bard',
        'Blitzcrank',
        'Braum',
        'Janna',
        'Karma',
        'Leona',
        'Lulu',
        'Nami',
        'Nautilus',
        'Rakan',
        'Senna',
        'Sona',
        'Soraka',
        'Taric',
        'Thresh',
        'Yuumi',
        'Milio',
    ]

    tank = [
        'Alistar', 'Amumu', 'Leona', 'Malphite', 'Maokai', 'Nautilus',
        'Ornn', 'Rammus', 'Rell', 'Sejuani', 'Sion', 'Zac', 'Taric', 'Shen',
        'TahmKench', 'Braum', 'Galio', 'Poppy',
        'Thresh','Chogath', 'Dr. Mundo',
        'Singed',
    ]

    championsInMatch = []
    playerNumber = 0

    gisellePosition = 0

    playersInfo = matchData['info']['participants']
    for player in playersInfo:

        championsInMatch.append(player['championName'])
        playerNumber += 1

        if player['riotIdGameName'] in beaNicks:
            isBeaOn = True
            beaKnowsHowToPlay = beaPlaysWith(player['championName'])
        elif player['riotIdGameName'] in carolNicks:
            isCarolOn = True
            carolKnowsHowToPlay = carolPlaysWith(player['championName'])
        elif player['riotIdGameName'] in michaelNicks:
            isMichaelOn = True
            michaelKnowsHowToPlay = michaelPlaysWith(player['championName'])
        elif player['riotIdGameName'] in giselleNicks:
            weWon = player['win']
            gisellePosition = playerNumber
            giselleKnowsHowToPlay = gisellePlaysWith(player['championName'])
        elif player['riotIdGameName'] in gadosNicks:
            isGadoOn = True
    
    allyTeamChampions = []
    giselleIsBlueSide = gisellePosition < 5
    
    if giselleIsBlueSide:
        for i in range(5):
            allyTeamChampions.append(championsInMatch[i])
    else:
        for i in range(5,10):
            allyTeamChampions.append(championsInMatch[i])

    weHaveTank = any(champion in tank for champion in allyTeamChampions)
    weHaveAdc = any(champion in adcarries for champion in allyTeamChampions)
    weHaveApc = any(champion in apcarries for champion in allyTeamChampions)
    weHaveBruiser = any(champion in bruisers for champion in allyTeamChampions)
    weHaveSup = any(champion in support for champion in allyTeamChampions)

    newMatchRegister = {
        'isBeaOn': isBeaOn,
        'isCarolOn': isCarolOn,
        'isMichaelOn': isMichaelOn,
        'isNoon': isNoon,
        'giselleKnowsHowToPlay': giselleKnowsHowToPlay,
        'michaelKnowsHowToPlay': michaelKnowsHowToPlay,
        'carolKnowsHowToPlay': carolKnowsHowToPlay,
        'beaKnowsHowToPlay': beaKnowsHowToPlay,
        'champion1': allyTeamChampions[0],
        'champion2': allyTeamChampions[1],
        'champion3': allyTeamChampions[2],
        'champion4': allyTeamChampions[3],
        'champion5': allyTeamChampions[4],
        'weWon': weWon,
        'isGadoOn': isGadoOn,
        'weHaveTank': weHaveTank,
        'weHaveAdc': weHaveAdc,
        'weHaveApc': weHaveApc,
        'weHaveBruiser': weHaveBruiser,
        'weHaveSup': weHaveSup,
        'gameDateMilliseconds': gameDateMilliseconds,
        'matchId': matchData['metadata']['matchId']
    }

    return newMatchRegister 

def convertingMatchToRow(matchId):
    matchData = getMatchData(matchId)
    return registeringMatchData(matchData)
