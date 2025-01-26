import eglincheckingfunctions as eglinf
import capitalonefunctions as onecreditf
import biltfunctions as biltf
import amexfunctions as amexf
import capitalonecheckingfunctions as onecheckingf
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def import_raw_data(file):
    """Imports raw data from a csv file"""

    fdf = pd.read_csv(file)
    #print(fdf)
    return fdf

def graph(sums, label, title):
    """Produces a pie chart from given list of sums and labels"""
    sns.set_palette(['#fcbd74', '#e98d6b', '#e3685c', '#d63c56', '#c93673', '#9e3460', '#8f3371', '#6c2b6d', '#511852'])
    piechart = plt.pie(sums, autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 1 else '', labeldistance=1.2, radius=1.2, startangle=-50, )
    plt.legend(loc="best", labels=label)
    plt.title(title)
    plt.show()

qs = import_raw_data("C:/Users/geoha/OneDrive/Desktop/my-official/pythonpersf/csv's/quicksilver2023.csv")
eglin = import_raw_data("C:/Users/geoha/OneDrive/Desktop/my-official/pythonpersf/csv's/eglinchecking.csv")
capitalonechecking = import_raw_data("C:/Users/geoha/OneDrive/Desktop/my-official/pythonpersf/csv's/capitalonechecking2023.csv")
bilt = import_raw_data("C:/Users/geoha/OneDrive/Desktop/my-official/pythonpersf/csv's/BILT.csv")
amex = import_raw_data("C:/Users/geoha/OneDrive/Desktop/my-official/pythonpersf/csv's/AMEX.csv")

eglin_graph = eglinf.main(eglin)
eglin_monthly_graph = eglinf.eglin_sum_by_month(eglin_graph[3], "January", "2023")
quicksilver_graph = onecreditf.quicksilver(qs)
quicksilver_monthly_graph = onecreditf.capitalone_sum_quicksilver_by_month(quicksilver_graph[3], "October")
bilt_graph = biltf.main(bilt)
bilt_month_graph = biltf.sum_bilt_by_month(bilt_graph[3], "October")
amex_graph = amexf.main(amex)
amex_month_graph = amexf.sum_amex_by_month(amex_graph[3], "October")
co_checking_graph = onecheckingf.main(capitalonechecking)
co_checking_month_graph = onecheckingf.capitalone_sum_by_month(co_checking_graph[3], "October")

graphs = [
    eglin_graph,
    eglin_monthly_graph,
    quicksilver_graph,
    quicksilver_monthly_graph,
    bilt_graph,
    bilt_month_graph,
    amex_graph,
    amex_month_graph,
    co_checking_graph,
    co_checking_month_graph
]

for g in graphs:
    try:
        graph(g[0], g[1], g[2])

    except TypeError:
        print("No data for this graph")