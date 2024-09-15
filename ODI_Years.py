import pandas as pd
import datetime as dt


Odi = pd.read_json("ODI-Batting_Cricket_Analytics.json")
#print (Od
#CountryFilter = Odi[Odi.Country == "India")
#What is the Year range?
Odi["MatchDate"] = pd.to_datetime(Odi["MatchDate"], dayfirst=True)
DateRange = Odi["MatchDate"].min(), Odi["MatchDate"].max()
print("The Year Range is")
print (DateRange)


#To see how many matches has been played by india
Matchcount = Odi[Odi.Country == "India"]["MatchDate"].unique().size
print("matches been played by india")
print(Matchcount)

#To see how many matches has been played by india after 2000
print("No of matches after 2000")
After2000 = (Odi[(Odi.Country == "India")&(Odi.MatchDate.dt.year>=2000)]["MatchDate"].unique().size)
print(After2000)

#To check the top scorer
print("The hitman")
print((Odi[(Odi.Country =="India") & (Odi.MatchDate.dt.year==2010)].groupby(["Player"])["Runs"].sum().sort_values(ascending=False).head(1)))


#To see how many matches has been played by india against each country after 2010
print("This is a list of INDIA vs All the Countries in 2010")
print(Odi[(Odi.Country =="India") & (Odi.MatchDate.dt.year==2010)].groupby(["Country","Versus"])["MatchDate"].nunique())