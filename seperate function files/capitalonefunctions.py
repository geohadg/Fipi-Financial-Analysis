import pandas as pd
import datetime as dt
import category_lists as cl

capitalonecreditsums = []

def restructure_capitalone_creditcard_data(fdf):
    """Adds a column to the dataframe containing the month name"""
    fdf["Month_Name"] = pd.to_datetime(fdf["Transaction Date"]).dt.month_name()
    fdf["Year"] = pd.to_datetime(fdf["Transaction Date"], format="mixed").dt.year
    fdf.loc[fdf["Category"] == "Gas/Automotive", "Category"] = "Gas"
    fdf.loc[fdf["Category"] == "Other Services", "Category"] = "Other"
    fdf.loc[fdf["Category"] == "Professional Services", "Category"] = "Other"
    fdf.loc[fdf["Category"] == "Internet", "Category"] = "Other"
    fdf.loc[fdf["Category"] == "Payment/Credit", "Category"] = "ACH Withdrawal"
    fdf.loc[fdf["Description"].str.contains("AMAZON"), "Category"] = "Amazon"
    for f in cl.fun:
        fdf.loc[fdf["Description"].str.contains(f), "Category"] = "Fun"

    for place in cl.Groceries:
        fdf.loc[fdf["Description"].str.contains(place), "Category"] = "Groceries"

    return fdf

def capitalone_sum_quicksilver_by_month(fdf, date):
    """Produces lists of sums and keys for each category in a given month"""
    monthly_sums = []
    df = fdf.query("Month_Name == @date")
    if df.empty:
        print("No data for this month")
        return None
    
    monthly_keys = list(df.loc[df["Category"] != '']["Category"].unique())
    for key in monthly_keys:
        monthly_sums.append(df[df["Category"] == key]["Debit"].sum()) if key in monthly_keys else None

    return monthly_sums, monthly_keys, "Quicksilver "+date, df

def capitalone_sum_savor_by_month(fdf, date):
    """Produces lists of sums and keys for each category in a given month"""
    monthly_sums = []
    df = fdf.query("Month_Name == @date")
    if df.empty:
        print("No data for this month")
        return None
    
    monthly_keys = list(df.loc[df["Category"] != '']["Category"].unique())
    for key in monthly_keys:
        monthly_sums.append(df[df["Category"] == key]["Debit"].sum()) if key in monthly_keys else None

    return monthly_sums, monthly_keys, "Savor "+date, df

def capitalone_sum_by_creditcard_category(fdf, category):
    """Sums all transactions in a given category"""

    df = fdf.query("Category == @category")
    sum = df["Amount"].sum()
    return sum

def capitalone_creditcard_sum_total(fdf):
    """Produces a list of sums for each category"""
    keys = list(fdf.loc[fdf["Category"] != '']["Category"].unique())
    for key in keys:
        capitalonecreditsums.append(fdf[fdf["Category"] == key]["Debit"].sum())

    return capitalonecreditsums, keys

def quicksilver(fdf):
    fdf = restructure_capitalone_creditcard_data(fdf)
    capitalone_creditcard_sum_total(fdf)
    keys = list(fdf.loc[fdf["Category"] != '']["Category"].unique())

    return capitalonecreditsums, keys, "QuickSilver", fdf

def savor(fdf):
    fdf = restructure_capitalone_creditcard_data(fdf)
    capitalone_creditcard_sum_total(fdf)
    keys = list(fdf.loc[fdf["Category"] != '']["Category"].unique())

    return capitalonecreditsums, keys, "Savor", fdf