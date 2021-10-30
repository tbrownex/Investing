1. Download any/all historical prices for funds
2. Put them all in /retirement/accounts/raw, even if they're not all in the same account
3. Download the benchmark (SPX) and put in folder /retirement/benchmark
4. Run "formatFunds" to remove some extra columns and rename the columns
5. Run "normalizeFunds" to generate the growth of $100
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