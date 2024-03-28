import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(r"AirlineReviews.csv")

df["DateFlown"] = pd.to_datetime(df["DateFlown"],format="%B %Y", errors="coerce")
df["DatePub"] = df["DatePub"].str.replace("th|rd|st|nd","", regex=True)
df["DatePub"] = pd.to_datetime(df["DatePub"],format="%d %B %Y", errors="coerce")

cutoffdate = pd.to_datetime("2019/12/31", format='%Y/%m/%d')
new_df = df.loc[df["DateFlown"]> cutoffdate]
dropNA_df = new_df.dropna()
dropNA_df = dropNA_df.drop(["Review"], axis=1)

dropNA_df.to_csv(r"cleaned_airliene_reviewd_1.csv", index=False)