# import requests
# from bs4 import BeautifulSoup
from unidecode import unidecode
from asyncpraw import Reddit
import pandas as pd
import asyncio

#%%
async def main(reddit_id, url_in, file_name):
    
    # ultilize resources by freeing the CPU from hanging in slow IO processes
    
    # create dictionary
    comment_dict = {'content': []}
    submission = await reddit_id.submission(url=url_in)
    
    # extract comments in a post; add printed lines to notify progress
    print("Loading comments, please wait...")
    await submission.comments.replace_more(limit=None)
    print("Comments fetched, saving...")
    
    for comment in submission.comments.list():
        comment_dict['content'].append(unidecode(str(comment.body)))
    
    # create pandas DataFrame, export comments as csv file
    df = pd.DataFrame(comment_dict)
    df.to_csv(file_name + '.csv')
    print("Finished!")

if __name__ == "__main__":
    
    import os
    
    # add script credentials from personal praw.ini file at another directory
    os.chdir(r'D:/Projects')
    script_id = Reddit("bot1", config_interpolation="basic")
    os.chdir(r'./ML-youtube-audio/examples')
    
    # --- example URLs for post comments extraction ---
    # podcast_review_URL = "https://www.reddit.com/r/AskReddit/comments/12j384c/whats_a_podcast_actually_worth_listening_to/"
    podcast_review_URL = "https://www.reddit.com/r/redditdev/comments/p0d7tz/asyncpraw_problems/"
    # podcast_review_URL = "https://www.reddit.com/r/hatsune/comments/13uqjbt/stunning_uwu/"
    
    # export comments into a csv file
    exported_data = 'reddit_comments2'
    asyncio.create_task(main(script_id, podcast_review_URL, exported_data))