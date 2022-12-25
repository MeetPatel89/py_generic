import pandas as pd
import numpy as np

# constructing dateindex using pd.date_range
index = pd.date_range(start="2000-01-01", periods=7, freq="T")
df = pd.DataFrame(data=np.random.randint(low=2, high=11, size=7), columns=["data"], index=index)
df = df.reset_index().rename(mapper={"index": "Date_1"}, axis=1)

index = pd.date_range(start="2003-01-23", periods=7, freq="30s")
df["Date_2"] = index

# Date_1 and Date_2 columns are of data type datetime64[ns]

df["Date_Diff"] = df["Date_2"] - df["Date_1"]

# Date_Diff will have timedelta64[ns] data type - data type any time you take difference between datetime64[ns] dtype columns

# df["Date_Diff"].dt.total_seconds() --> gives you total seconds after including all components of timestamp
#df["Date_Diff"].dt.seconds --> extracts only hour+minutes+seconds component of timestamp 
df["Date_Diff_Seconds"] = df["Date_Diff"].dt.total_seconds()

# aggregate Date_Diff and Date_Diff_Seconds
agg_df = df.groupby(by="data", as_index=False)[["Date_Diff", "Date_Diff_Seconds"]].agg(Date_Diff_Mean=("Date_Diff", "mean"), Date_Diff_Sum=("Date_Diff", "sum"), Date_Diff_Secs_Mean=("Date_Diff_Seconds", "mean"), Date_Diff_Secs_Sum=("Date_Diff_Seconds", "sum"))