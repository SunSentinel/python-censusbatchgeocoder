import pandas as pd
import requests
import censusbatchgeocoder

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

"""
df = pd.read_excel(
    "./addresses.xlsx",
    #skiprows=1
)
"""

df = pd.read_csv(
    "./addresses.csv"
)

result = censusbatchgeocoder.geocode(
    df.to_dict("records")[0:],
    id="id",
    address="address",
    city="city",
    state="state",
    zipcode="zipcode"
)

result_df = pd.DataFrame(result)
result_df.to_csv('output.csv')
