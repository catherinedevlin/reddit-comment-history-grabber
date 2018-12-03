# reddit-comment-history-grabber
Pulls quotes from a user's recent comments within a given subreddit

# before use

- `pip install -r requirements.txt`
- Set `subreddit` in config.ini
- Register an application with reddit: https://www.reddit.com/prefs/apps
- copy SAMPLE.config.secret.ini to config.secret.ini and fill with values from Reddit app

# to use

`python manage.py grab_history.py -l 10 redditusername
