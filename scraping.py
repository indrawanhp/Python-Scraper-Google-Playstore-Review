from google_play_scraper import Sort, reviews_all
import pandas as pd

result = reviews_all(
    'com.tencent.ig',
    sleep_milliseconds=0, # defaults to 0
    lang='id', # defaults to 'en'
    country='id', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=None # defaults to None(means all score)
)

df = pd.DataFrame(result)
dataset = df[['userName', 'content' , 'score']]
dataset.to_csv('pubg_review.csv')