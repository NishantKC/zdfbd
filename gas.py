import pandas as pd
import plotly.express as px
df=pd.read_csv("line_chart.csv")
graph = px.line(df,x = "Year", y = "Per capita income",title="Country Line Graph",color="Country" )
graph.show()