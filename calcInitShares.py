def calcShares(df):
    # Get the number of shares $1 million would buy
    df.sort_values('date', inplace=True)
    initVal = df.iloc[0]['value']
    return round(1e6/initVal, 2)