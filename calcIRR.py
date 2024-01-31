import numpy_financial as npf
import numpy as np
import pandas as pd
import datetime

def calcIRR(deposits, endDate, endValue, errorLimit):
    '''
    deposits: DF with dates and amounts of deposits, sorted by date ascending
    endDate and endValue: date and amount the account grew to
    errorLimit: how close you want to be to the exact amount of endValue
    '''
    irr = 2e-4
    total = 1e9
    while abs(total - endValue) > errorLimit:
        irr = abs(np.random.normal(loc=irr, scale=1e-4))
        total = depositLoop(deposits, endDate, irr)
        if abs(total - endValue) < errorLimit:
            print("Total: {:,}\n".format(total))
            break
        if total > endValue:
            irr -= 5e-5
        else:
            irr += 5e-5
    return irr

def calcGrowth(val, dailyRate, numDays):
    return npf.fv(dailyRate, nper=numDays, pmt=0, pv=-val)

def depositLoop(deposits, endDate, irr):
    l = []
    for row in deposits.iterrows():
        startingVal = float(row[1]['value'])
        depositDate = pd.to_datetime(row[1]['date']).date()
        diff = endDate - depositDate
        numDays = diff.days
        x = calcGrowth(startingVal, irr, numDays)
        l.append(x)
    return round(sum(l))