def getConfig():
    return {
        'ETrade': {
            'dataLoc': '~/data/investing/ETrade/',
            'fileName': 'accountValues.csv'
        },
        'Fisher': {
            'dataLoc': '~/data/investing/Fisher/'
        },
        'SPX': {
            'dataLoc': '~/data/investing/benchmark/',
            'fileName': 'spx.csv'
        },
        'MSCI': {
            'dataLoc': '~/data/investing/benchmark/',
            'fileName': 'msci.csv'
        },
        'marketAPI': {
            "URL": 'http://api.marketstack.com/v1/',
            "APIKey": '?access_key=ffa68edbfb08de7589a43751795e0e07'
        }
    }