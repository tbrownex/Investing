1. Download
    a) Download the historical prices for funds and put into /retirement/funds/raw
    The dates should all be first of the month. Last row might have a current month, like 12/14: remove that row...all dates should be 1st of the month
    b) Download the dividend data for the funds and put into /retirement/funds/raw/dividends
2. Format
    a) Run "formatFunds" to remove some extra columns and rename the columns
    b) Run "formatDividends" to aggregate the dividends for a month
3. Run "calcNumShares" which will compute the number of shares a set amount ($10,000) would have bought as of the first price available (first row in the fund data). The account values is calculated from then on as this number of shares times the current price
4. Run "addDividends" to convert the per-share dividend amount to $$. A dividend of $.1 per share times 100 shares would result in a $10 dividend, so compute and store the $10.
Download the benchmark (SPX) and put in folder /retirement/benchmark
5. Run "calcTotalFundValue" to generate the growth of $100


6. Run "summarizeFunds" to generate volatility and annualized growth
5. Go into "mergeFunds"
    a) check the dictionary entries: each account has a set of funds associated which has to be up to date.
    b) set the variable "key" to the account you want to process
    c) run it, producing "merged_<accountName>.csv"
    d) run "verifyMerged" to compare the merged values with raw
    
Now all the funds for that account are in one file, a column for each fund

5. Run "prepFunds" to normalize the values in each fund/column and compute a few statistics like Avg Annual return
    a) run "verifyPrepped" to compare the prepped values with raw
6. Run "prepSPX" to do the same
The two "summary" output files have the average annual return for the fund/benchmar plus the variance

Funds correlated with SPX:
    VFIAX  .9999   10 yr total return: 15.22
    TRBCX  .986    10 yr total return: 18.88
    PRILX  .97     10 yr total return: 15.68
 ...so move all PRILX and VFIAX into TRBCX