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
    session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    session.like_by_tags(['beograd', 'belgrade', 'srbija', 'ig_srbija'], amount=25, interact=True, randomize=True)
    #session.follow_by_tags(['beograd', 'belgrade', 'srbija', 'ig_srbija'], amount=1, interact=True, randomize=True)

