from pytrends.request import TrendReq
import pandas as pd
from datetime import date, datetime


pytrend = TrendReq(timeout=(10,20), retries=3)
pytrend.build_payload(
    kw_list=["ps4", "sony", "laptop", "samsung"],
    timeframe='today 1-m',
    geo='',
    gprop=''
)

df = pytrend.interest_over_time()
related_queries = pytrend.related_queries()
print(related_queries)
#print(df.head(n=30))