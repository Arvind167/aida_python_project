import numpy as np
import pandas as pd

from alpha_vantage.timeseries import TimeSeries
import requests

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

from sklearn.preprocessing import MinMaxScaler


def create_df(df):
    df_prelude = df.drop(['Province/State', 'Lat', 'Long'], axis=1).copy()
    df_prelude.columns = pd.to_datetime(df_prelude.columns)
    df_pivot = df_prelude.pivot_table(columns=df_prelude.index, aggfunc='sum')
    #  df_pivot.reset_index(inplace = True)
    #  df_pivot.rename(columns = {'index': 'Date'}, inplace = True)
    return df_pivot


confirmed_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
deaths_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"