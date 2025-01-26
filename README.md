# Fipi-Financial-Analysis

## Abstract
I want to write a tool in python that can automatically parse csv files from multiple different
banks and turn them into a pandas dataframe that can be queried by user selection and turned
into a graph. It will be wrapped up in a CustomTkinter GUI and packaged as a .EXE to be run on 
computers without python installed

## Features
1. Import of Several Bank Types: Just (AMEX, BILT, Eglin Checking, CapitalOne Checking, Quicksilver, Savor) for now!
2. Export to a single consolidated csv file with fluff cleaned out
3. Generated Charts with changeable parameters (i.e. Month and Year Selections, spending between categories, spending between accounts)
4. Save graph as a .png
* for now the only graph type embedded is a pie chart that changes labels for graphing categories between accounts but bar charts are coming
