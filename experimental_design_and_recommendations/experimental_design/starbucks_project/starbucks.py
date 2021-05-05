import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('training.csv', index_col=0)

profile = ProfileReport(df, title="Pandas Profiling Report")

profile.to_file("data_report.html")