# subreddit-searcher-script
Python script used to search a subreddit for a post with a keyword/phrase, and PM a link of that post to a user.

[OAuth2](https://github.com/reddit-archive/reddit/wiki/OAuth2) will be needed to run this script.

# Usage <br />
This script can be used for many purposes such as searching for specific items in subreddit marketplaces. <br /><br />

#### Configuring the Script <br />
For example, if you are looking for an iPad Pro 2020 and an Apple Pencil 2 on r/Appleswap, and the username you want the post sent to is "cooluser", you can configure the script to look like this.
```
for submission in reddit.subreddit("appleswap").new(limit=5):
    if submission.id not in posts_seen:
        if re.search("ipad pro 2020", submission.title, re.IGNORECASE):
            reddit.redditor("cooluser").message("ipad air 4", "here is an ipad air 4: " + submission.permalink)
            print(submission.title)
        if re.search("apple pencil 2", submission.title, re.IGNORECASE):
            reddit.redditor("cooluser").message("apple pencil 2", "here is an apple pencil 2: " + submission.permalink)
            print(submission.title)
        posts_seen.append(submission.id)
```
