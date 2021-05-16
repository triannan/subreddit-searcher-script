# subreddit-searcher-script
Python script used to search a subreddit for a post with a keyword/phrase, and PM a link of that post to a user.

[OAuth2](https://github.com/reddit-archive/reddit/wiki/OAuth2) will be needed to run this script.

# Usage <br />
This script can be used for many purposes such as searching for specific items in subreddit marketplaces. <br /><br />

#### Configuring the Script <br />
For example, if you are looking for an iPad Pro 2020 and an Apple Pencil 2 on r/Appleswap, you can configure the script to look like this, with USERNAME replaced by the reddit username you want to send the PM to.
```
for submission in reddit.subreddit("appleswap").new(limit=100):
    if submission.id not in posts_seen:
        if re.search("ipad pro 2020, submission.title, re.IGNORECASE):
            reddit.redditor("USERNAME").message("ipad air 4", "here is an ipad air 4: " + submission.permalink)
            print(submission.title)
        if re.search("apple pencil 2, submission.title, re.IGNORECASE):
            reddit.redditor("USERNAME").message("apple pencil 2", "here is an apple pencil 2: " + submission.permalink)
            print(submission.title)
        posts_seen.append(submission.id)
```
<br />

#### Running the Script <br />
In order to run this script to check the subreddit in certain intervals, cron or something similar will be needed. <br />
For example, if you want to run the subreddit script to check the subreddit every minute, you can configure your crontab to look like this. <br />
###### Example crontab running the reddit script every minute
```
* * * * * ./pathtofile/subreddit-searcher.py >> /pathtofile/cron.log 2>&1
```
It's a bit harder to run a cronjob for less than a minute, but you can always create a shell script to run your program, and sleep multiple times, and then run a cronjob for the new script. <br />
For example, if you want to run the subreddit script every 30 seconds, you can create a shell script to run the subreddit searcher and rest 30 seconds before running it again. <br />
###### Example shell script running the reddit script 2 times in 30 second intervals
```
#!/bin/bash
python3 /pathtofile/subreddit-searcher.py
sleep 30
python3 /pathtofile/subreddit-searcher.py
sleep 30
```
If you create a cronjob for the example shell script above, running it every minute, it will run the subreddit script every 30 seconds repeatedly. <br />
###### Example crontab running the example shell script every minute
```
* * * * * ./pathtofile/example.sh >> /pathtofile/cron.log 2>&1
```
