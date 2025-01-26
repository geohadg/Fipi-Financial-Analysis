import pandas as pd
import datetime as dt
import category_lists as cl

sums = []

def restructure_bilt_data(fdf):
    """Adds a column to the dataframe containing the month name"""
    fdf["Month_Name"] = pd.to_datetime(fdf["Date"]).dt.month_name()
    fdf["Year"] = pd.to_datetime(fdf.Date, format="mixed").dt.year
    fdf["Category"] = None
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
    fdf.loc[fdf["Description"].str.contains("Bill Pay Payment"), "Category"] = "Payment"
    fdf.loc[fdf["Description"].str.contains("TMOBILE"), "Category"] = "Phone/Cable"
    for place in cl.Groceries:
        fdf.loc[fdf["Description"].str.contains(place), "Category"] = "Groceries"

    return fdf

def sum_bilt_by_month(fdf, date):
    """Produces lists of sums and keys for each category in a given month"""
    monthly_sums = []
    df = fdf.query("Month_Name == @date")
    if df.empty:
        print("No data for this month")
        return None
    
    monthly_keys = list(df.loc[df["Category"] != '']["Category"].unique())
    for key in monthly_keys:
        monthly_sums.append(df[df["Category"] == key]["Amount"].sum()) if key in monthly_keys else None

    return monthly_sums, monthly_keys, "BILT "+date, df

def bilt_sum_by_category(fdf, category):
    """Sums all transactions in a given category"""

    df = fdf.query("Category == @category")
    sum = df["Amount"].sum()
    return sum

def bilt_sum_total(fdf):
    """Produces a list of sums for each category"""
    keys = list(fdf.loc[fdf["Category"] != '']["Category"].unique())
    for key in keys:
        fdf.loc[fdf["Amount"] < 0, "Amount"] = fdf["Amount"] * -1
        sums.append(fdf[fdf["Category"] == key]["Amount"].sum())

    return sums, keys

def main(fdf):
    fdf = restructure_bilt_data(fdf)
    fdf = fdf.query("Category != 'Payment'")
    bilt_sum_total(fdf)
    keys = list(fdf.loc[fdf["Category"] != '']["Category"].unique())
    return sums, keys, "Bilt", fdf