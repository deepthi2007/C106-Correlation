import pandas as pd
import plotly.express as px
import numpy as np

def getData (path) :
    data = pd.read_csv(path)
    marks=data["Marks In Percentage"].tolist()
    attendence = data["Days Present"].tolist()
    return {
        "x":marks,
        "y":attendence
    }

def coef (data) :
    correlation = np.corrcoef(data["x"],data["y"])
    print("Co-relation between Student Marks and Attendence -> ",correlation[0,1])
    return correlation

def plotFigure(path) :
    df = pd.read_csv(path)
    fig = px.scatter(df,x="Marks In Percentage",y="Days Present")
    fig.show()

def setup ():
    data = getData("D:\deepthi projects\C106\Student Marks vs Days Present.csv")
    coef(data)
    plotFigure("D:\deepthi projects\C106\Student Marks vs Days Present.csv")

setup()
