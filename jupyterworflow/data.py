import os
from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
def get_data(filename = 'FremontBridge.csv', url=FREMONT_URL, force_download = True):
    if force_download or not os.path.exists(url):
        urlretrieve(url, filename);
    data = pd.read_csv(filename, index_col = 'Date', parse_dates=True)
    data.columns = ['West', 'East']
    data.fillna(0, inplace=True)
    data['Total'] = data.eval('East + West')
    return data
