#!/usr/bin/env python3

import praw
import pdb
import re
import os

reddit = praw.Reddit(client_id="CLIENT ID",
                     client_secret="CLIENT SECRET",
                     user_agent="USER AGENT",
                     username="USERNAME",
                     password="PASSWORD")
print(reddit.user.me())

if not os.path.isfile("TEXT FILE NAME"):
    posts_seen = []
else:
    with open("TEXT FILE NAME", "r") as f:
        posts_seen = f.read()
        posts_seen = posts_seen.split("\n")
        posts_seen = list(filter(None, posts_seen))

for submission in reddit.subreddit("SUBREDDIT NAME").new(limit=100):
    if submission.id not in posts_seen:
        if re.search("KEYWORD IN TITLE", submission.title, re.IGNORECASE):
            reddit.redditor("USERNAME").message("MESSAGE TITLE", "MESSAGE CONTENT " + submission.permalink)
            print(submission.title)
        posts_seen.append(submission.id)

with open("TEXT FILE NAME", "w") as f:
    for post_id in posts_seen:
        f.write(post_id + "\n")
