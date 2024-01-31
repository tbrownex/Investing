import pandas as pd

def calcAnnualReturn(df):
    df['month'] = df['date'].apply(lambda x: pd.to_datetime(x).month)
    dec = df[df['month']==12]
    print('Year     Return')
    for yr in range(len(dec)-1):
        start = dec.iloc[yr]['value']
        end = dec.iloc[yr+1]['value']
        yr = dec.iloc[yr]['date']
        yr = pd.to_datetime(yr)
        annReturn = (end-start)/start
        print("{:<9}{:.1%}".format(yr.year+1, annReturn))