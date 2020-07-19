"""
This template is written by @ficanovak

What does this quickstart script aim to do?
- Follow users based on location, interact with them by liking 2 photos of the user it has followed, and finally unfollow number of users.
"""

from instapy import InstaPy
from instapy import smart_run

insta_username = 'username'
insta_password = 'password'

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True)

# let's go! :>
with smart_run(session):
    # general settings   
    # unfollow activity
    #session.unfollow_users(amount=212, nonFollowers=True, style="RANDOM",
    #                       unfollow_after=42 * 60 * 60, sleep_delay=300)
    session.unfollow_users(amount=300, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=48*60*60, sleep_delay=600)

