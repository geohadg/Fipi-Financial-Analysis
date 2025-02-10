---
title: Fipi Financial Analysis
---

## Abstract

I want to write a tool in python that can automatically parse csv files from multiple different
banks and turn them into a pandas dataframe that can be queried by user selection and turned
into a graph. It will be wrapped up in a CustomTkinter GUI and packaged as a .EXE to be run on 
computers without python installed

## Features

#### 1. Import of Several Bank Types: Just (AMEX, BILT, Eglin Checking, CapitalOne Checking, Quicksilver, Savor) for now!

#### 2. Categorize Spending and Label according to Transaction Descriptions (i.e. a line containing "CHIK-FIL-A" will be labeled as Dining)

#### 3. Export to a single consolidated csv file with fluff cleaned out and formatted

#### 4. Generated Charts with changeable parameters (i.e. Month and Year Selections, spending between categories, spending between accounts)

#### 5. Save graph as a .png

#### 6. Generate a Customized Report with the data given as .txt

for now the only graph type embedded is a pie chart that changes labels for graphing categories between accounts but bar charts are coming

## Notes

For now the categorization feature is limited to recognizing vendors contained within a list inside Fipi, in the future this will be replaced by some form of NER combined with web scraping or something that wouldn't require a massive list of exact strings to compare against. The graphs are limited to only Pie Charts for all parameter changes but do change labels in order to make data more digestable for certain config options, in the future this will be replaced with 
some form of adaptive graphing that uses different plot methods for different data selections
