import pandas as pd
import datetime as dt
import category_lists as cl

sums = []

def restructure_capitalone_data(fdf):
    """Adds Month Name to new Column, Removes Unwanted Transaction Types, and assigns Categories to each transaction"""

    fdf["Month_Name"] = pd.to_datetime(fdf["Transaction Date"], format="%m/%d/%y").dt.month_name()
    fdf["Year"] = pd.to_datetime(fdf["Transaction Date"], format="mixed").dt.year

    for grocery in cl.Groceries:
        fdf.loc[fdf["Transaction Description"].str.contains(grocery), "Category"] = "Groceries"

    for place in cl.Restaurant:
        fdf.loc[fdf["Transaction Description"].str.contains(place), "Category"] = "Dining"
        
    for station in cl.Gas:
        fdf.loc[fdf["Transaction Description"].str.contains(station), "Category"] = "Gas"

    for f in cl.fun:
        fdf.loc[fdf["Transaction Description"].str.contains(f), "Category"] = "Fun"

    fdf.loc[fdf["Transaction Description"].str.contains("AMAZON"), "Category"] = "Amazon"

    for ach in cl.ACHWhitdrawal:
        fdf.loc[fdf["Transaction Description"].str.contains(ach), "Category"] = "ACH Withdrawal"

    fdf.loc[fdf["Category"].isnull(), "Category"] = "Other"
    fdf.loc[fdf["Transaction Description"].str.contains("Deposit"), "Category"] = "Deposit"
    fdf.loc[fdf["Transaction Description"].str.contains("TMOBILE"), "Category"] = "Phone/Cable"
    return fdf
    
def capitalone_sum_by_month(fdf, date):
    """Produces lists of sums and keys for each category in a given month"""
    monthly_sums = []
    df = fdf.query("Month_Name == @date")
    if df.empty:
        print("No data for this month")
        return None
    
    monthly_keys = list(df.loc[df["Category"] != '']["Category"].unique())
    for key in monthly_keys:
        monthly_sums.append(df[df["Category"] == key]["Transaction Amount"].sum()) if key in monthly_keys else None

    return monthly_sums, monthly_keys, "CapitalOne " + date, df

def capitalone_sum_by_category(fdf, category):
    """Sums all transactions in a given category"""

    df = fdf.query("Category == @category")
    sum = df["Amount"].sum()
    return sum

def capitalone_sum_total(fdf):
    """Produces a list of sums for each category"""
    keys = list(fdf.loc[fdf["Category"] != '']["Category"].unique())
    for key in keys:
        sums.append(fdf[fdf["Category"] == key]["Transaction Amount"].sum())

    return sums, keys

def main(fdf):
    
    cdf = restructure_capitalone_data(fdf)
    cdf = cdf.query("Category != 'Deposit'")
    keys = list(cdf.loc[cdf["Category"] != '']["Category"].unique())
    capitalone_sum_total(cdf)
    return sums, keys, "CapitalOne Checking", cdf