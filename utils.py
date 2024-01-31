from config import getConfig

def formatURL(typ):
    cfg = getConfig()
    api = cfg['marketAPI']
    return api['URL']+typ+api['APIKey']+'&limit=1000'