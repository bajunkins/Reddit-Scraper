import requests as rq
import json as js

#subreddit: subreddit to retrieve from
#field: type of information from desired, ex: 'title'
#times are in epoch time
#quantity: total number of posts to retrieve
def scrape(subreddit, field, startTime, endTime, quantity):
    size = 1000 #1000 is limit
    total_lines = 0
    ret = []

    while startTime < endTime:
        if (total_lines >= quantity): break
        idx = 0
        getURL = f'https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&sort=asc&sort_type=created_utc&after={startTime}&before={endTime}&size={size}'
        responseJS = rq.get(getURL).json()
        for post in responseJS['data']:
            idx+=1
            total_lines += 1
            if (total_lines >= quantity): break
            ret.append(post[field])
            if (idx == size): startTime = post['created_utc'] + 1

    return ret