from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = ''  # <- enter username here
insta_password = ''  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)
with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    # activities

    """ Massive Follow of users followers (I suggest to follow not less than
    3500/4000 users for better results)...
    """
    session.follow_user_followers(['nba', 'wizkhalifa'], amount=800,
                                  randomize=True, interact=True)

    """ First step of Unfollow action - Unfollow not follower users...
    """
