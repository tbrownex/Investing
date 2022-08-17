from config import getConfig

def formatURL(typ):
    cfg = getConfig()
    return cfg['URL']+typ+cfg['APIKey']+'&limit=1000'