import pandas as pd
import datetime as dt
import category_lists as cl

sums=[]

def restructure_eglin_data(fdf):
    """Adds Month Name to new Column, Removes Unwanted Transaction Types, and assigns Categories to each transaction"""

    fdf["Month_Name"] = pd.to_datetime(fdf["Date"]).dt.month_name()
    fdf["Year"] = pd.to_datetime(fdf.Date, format="mixed").dt.year

    for category in cl.unwanted_categories:
        fdf = fdf.drop(fdf[fdf['Ext'] == category].index)

    for grocery in cl.Groceries:
        fdf.loc[fdf["Description"].str.contains(grocery), "Category"] = "Groceries"

    for place in cl.Restaurant:
        fdf.loc[fdf["Description"].str.contains(place), "Category"] = "Dining"
        
    for station in cl.Gas:
        fdf.loc[fdf["Description"].str.contains(station), "Category"] = "Gas"

    for f in cl.fun:
        fdf.loc[fdf["Description"].str.contains(f), "Category"] = "Fun"

    fdf.loc[fdf["Description"].str.contains("AMAZON"), "Category"] = "Amazon"

    for ach in cl.ACHWhitdrawal:
        fdf.loc[fdf["Description"].str.contains(ach), "Category"] = "ACH Withdrawal"

    fdf.loc[fdf["Category"].isnull(), "Category"] = "Other"
    fdf.loc[fdf["Description"].str.contains("TMOBILE"), "Category"] = "Phone/Cable"
    return fdf
    
def eglin_sum_by_month(fdf, date, year):
    """Produces lists of sums and keys for each category in a given month"""
    monthly_sums = []
    df = fdf.query("Month_Name == @date")
    if df.empty:
        return None
    
    df = fdf.query("Year == @year")
    if df.empty:
        return None
    
    monthly_keys = list(df.loc[df["Category"] != '']["Category"].unique())
    for key in monthly_keys:
        df.loc[df["Amount"] < 0, "Amount"] = df["Amount"] * -1
        monthly_sums.append(df[df["Category"] == key]["Amount"].sum()) if key in monthly_keys else None


    return monthly_sums, monthly_keys, "Eglin " + date+year, df

def eglin_sum_by_category(fdf, category):
    """Sums all transactions in a given category"""

    df = fdf.query("Category == @category")
    sum = df["Amount"].sum()
    return sum

def eglin_sum_total(fdf):
    """Produces a list of sums for each category"""

    keys = list(fdf.loc[fdf["Category"] != '']["Category"].unique())
    for key in cl.keys:
        fdf.loc[fdf["Amount"] < 0, "Amount"] = fdf["Amount"] * -1
        sums.append(fdf[fdf["Category"] == key]["Amount"].sum())

    return sums, keys

def main(fdf):
    edf = restructure_eglin_data(fdf)
    eglin_sum_total(edf)
    keys = list(edf.loc[edf["Category"] != '']["Category"].unique())
    return sums, keys, "Eglin Total ", edf