from config import getConfig

def formatURL(typ):
    cfg = getConfig()
    return cfg['marketAPI']['URL']+typ+cfg['marketAPI']['APIKey']+'&limit=1000'