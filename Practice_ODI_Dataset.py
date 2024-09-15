import pandas as pd
import numpy as np
import datetime as dt

Odi = pd.read_json("ODI-Batting_Cricket_Analytics.json")
Odi["MatchDate"] = pd.to_datetime(Odi["MatchDate"], dayfirst=True)
DateRange = Odi["MatchDate"].max , Odi["MatchDate"].min
print(DateRange)

#matches by India in 2010
Matches = Odi[(Odi.Country=="India") & (Odi.MatchDate.dt.year >= 2010)]["MatchDate"].unique().size
print("In 2010",Matches)

#Top Scorer
Top = Odi[(Odi.Country=="India") & (Odi.MatchDate.dt.year == 2010)].groupby(["Versus"])["Runs"].sum().sort_values(ascending=False).head(1)
print("In 2010",Top)

#To see how many matches has been played by india against each country after 2010
IndiaVS = Odi[(Odi.Country=="India") & (Odi.MatchDate.dt.year >= 2010)].groupby(["Country","Versus"])["MatchDate"].nunique()
print("In 2010",IndiaVS)
