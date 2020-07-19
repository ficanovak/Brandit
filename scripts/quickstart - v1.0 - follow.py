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
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=6000,
                                    max_following=6000,
                                    min_followers=30,
                                    min_following=30)
    
    #amount_number=10
    
    #session.set_do_like(enabled=True, percentage=100)
    #session.set_user_interact(amount=2, randomize=True, percentage=50, media='Photo')
    session.follow_by_tags(['beograd', 'belgrade', 'srbija', 'ig_srbija'], amount=40)
    session.follow_by_locations(['213801245/belgrade-serbia/', '213825898/vracar-historical/', '215512174/mr-stefan-braun-beograd/', '471812246551827/beton-hala/', '842503471/port-by-community/', '6776759/dorcol/'], amount=30)
    
    # unfollow activity
    #session.unfollow_users(amount=212, nonFollowers=True, style="RANDOM",
    #                       unfollow_after=42 * 60 * 60, sleep_delay=300)

