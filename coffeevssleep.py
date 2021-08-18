import pandas as pd
import plotly.express as px
import numpy as np

def getData (path) :
    data = pd.read_csv(path)
    coffee=data["Coffee in ml"].tolist()
    sleep = data["sleep in hours"].tolist()
    return {
        "x":coffee,
        "y":sleep
    }

def coef (data) :
    correlation = np.corrcoef(data["x"],data["y"])
    print("Co-relation between Coffee and Sleep -> ",correlation[0,1])
    return correlation

def plotFigure(path) :
    df = pd.read_csv(path)
    fig = px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()

def setup ():
    data = getData("D:\deepthi projects\C106\cups of coffee vs hours of sleep.csv")
    coef(data)
    plotFigure("D:\deepthi projects\C106\cups of coffee vs hours of sleep.csv")

setup()
