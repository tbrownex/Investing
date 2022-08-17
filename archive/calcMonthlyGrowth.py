def calcGrowthRate(df, fundName):
    # computes the compounded monthly return for a fund
    initVal = df.iloc[0][fundName]
    finalVal = df.iloc[-1][fundName]
    numMonths = len(df)
    return 1+np.rate(nper=numMonths, pmt=0, pv=-initVal, fv=finalVal)