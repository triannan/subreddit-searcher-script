#!/usr/bin/env python3

import praw
import pdb
import re
import os

#get all this information from https://www.reddit.com/prefs/apps when you make a new app
#you need to enter a reddit username/password that the script can access to send PMs
reddit = praw.Reddit(client_id="CLIENT ID",
                     client_secret="CLIENT SECRET",
                     user_agent="USER AGENT",
                     username="USERNAME",
                     password="PASSWORD")
print(reddit.user.me())

#you need to create a text file to store the IDs of the posts that have already been seen by the script, so it won't PM duplicates
#the same text file will be used throughout the script where TEXT FILE NAME is specified
if not os.path.isfile("TEXT FILE NAME"):
    posts_seen = []
else:
    with open("TEXT FILE NAME", "r") as f:
        posts_seen = f.read()
        posts_seen = posts_seen.split("\n")
        posts_seen = list(filter(None, posts_seen))

#enter the subreddit name, keyword to be searched for, the username of the redditor to PM the link to, and the contents of the PM
for submission in reddit.subreddit("SUBREDDIT NAME").new(limit=100):
    if submission.id not in posts_seen:
        if re.search("KEYWORD IN TITLE", submission.title, re.IGNORECASE):
            reddit.redditor("USERNAME").message("MESSAGE TITLE", "MESSAGE CONTENT " + submission.permalink)
            print(submission.title)
        posts_seen.append(submission.id)

with open("TEXT FILE NAME", "w") as f:
    for post_id in posts_seen:
        f.write(post_id + "\n")
