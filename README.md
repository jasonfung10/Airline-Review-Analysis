# Airline-Review-Analysis

It is a data analysis mini project to analyse different airlines ratings with data sourced from Kaggle.

Skills used
- `Python`
- `Tableau`

Data can ben downloaded [here](https://www.kaggle.com/datasets/joelljungstrom/128k-airline-reviews/data)

## Data Cleaning
- first download from Kaggle in `csv`
- cleaned by using `Python``Pandas`
- First format the date time as follow:
```
df["DateFlown"] = pd.to_datetime(df["DateFlown"],format="%B %Y", errors="coerce")
df["DatePub"] = df["DatePub"].str.replace("th|rd|st|nd","", regex=True)
df["DatePub"] = pd.to_datetime(df["DatePub"],format="%d %B %Y", errors="coerce")
```
- then filter and limited data from 2020 and also remove all NA data. "Review" from the original data is also removed as it will make the data size too large to handle in `Tableau` efficiently
```
cutoffdate = pd.to_datetime("2019/12/31", format='%Y/%m/%d')
new_df = df.loc[df["DateFlown"]> cutoffdate]
dropNA_df = new_df.dropna()
dropNA_df = dropNA_df.drop(["Review"], axis=1)
```
- Then save the cleaned data into a `CSV` file to be parsed into `Tableau`


## Data Visualisation
<img width="1411" alt="Screenshot 2024-03-28 at 10 42 17 PM" src="https://github.com/jasonfung10/Airline-Review-Analysis/assets/111647154/964ed3ff-d16b-404d-9329-ede580dbe7fa">

`Tableau` is used for the visulation in order to create a interactive dashboard
- Top 5 overall rated airlines was displated at the top
- Top N (can be customised in the left most filter section) airlines in 3 areas are displayed at the bottome bar charts
- Average monthly ratings and rating in different countries are displayed in the middle row
- Filters of month, cabine class and travelling type are available to further select certain data





