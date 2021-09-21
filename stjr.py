import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
graph = px.scatter(df,x = "Country", y = "InternetUsers",size="Population",color="Per capita")
graph.show()