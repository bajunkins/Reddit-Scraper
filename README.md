# Reddit Scraper

Simple but versatile method for retrieving information from reddit posts. I personally wrote this method to build a large dataset from the titles of a specific subreddit, but I figured a more generalized version of it could be useful to other developers.

## Usage
*def scrape(subreddit, field, startTime, endTime, quantity):*

subreddit: Subreddit to extract posts from, ex: 'funny'

field: Post characteristic to retrieve

  example options (full list of options can be found on the [Pushshift API](https://github.com/pushshift/api) GitHub):
  
    -'author': post author
    
    -'created_utc': post creation time (epoch time)
    
    -'domain': domain of linked url (if link post)
    
    -'url': full linked url (if link post)
    
    -'full_link': full link to the post itself
    
    -'score': number of upvotes vs downvotes
    
    -'title': title of post
    
    -'selftext': text of post (if self post)
    
startTime: Finds posts after this time (epoch time)

endTime: Finds posts before this time (epoch time)

quantity: Maximum number of posts to retrieve

returns: List of {field} for each post from {subreddit} 


## Example Usage
>>> python

>>> import redditscraper as rs

>>> results = rs.scrape('funny', 'title', 1576810943, 1577312017, 5)

>>> print(results)


## Built With

* Built using the [Pushshift API](https://github.com/pushshift/api) - API for retrieving Reddit data
