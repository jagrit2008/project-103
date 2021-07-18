import pandas as pd
import plotly.express as px

df = pd.read_csv("covidData.csv")
fig = px.scatter(df, x="date", y="cases",
	          size="numbers",color="Country",
                   size_max=50)
fig.show()
