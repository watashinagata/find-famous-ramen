import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
from find_famous_ramen import Tabelog

nagoya_ramen_review = Tabelog(base_url="https://tabelog.com/aichi/A2301/rstLst/ramen/",test_mode=False, p_ward='名古屋市内')
#CSV保存
nagoya_ramen_review.df.to_csv("nagoya_ramen_review.csv")

nagoya_ramen_review = pd.read_csv('nagoya_ramen_review.csv')
nagoya_ramen_review