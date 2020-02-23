from instapy import InstaPy
from instapy.util import web_address_navigator
from instapy import smart_run
import pandas as pd
import schedule, time
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()

# login credentials
insta_username = ''  # <- enter username here
insta_password = ''  # <- enter password here
# datetime object containing current date and time
   # if you want to run this script on a server,
def insta_strategy():
    followers = pd.read_csv('followers.csv')
    session = InstaPy(username=insta_username, password=insta_password,
                      headless_browser=True, proxy_address='', proxy_port='')


    to_follow = followers[followers.scheduled == False].tail(4)
    print(to_follow['profile'].values.tolist())
    session.login()
    session.set_action_delays(enabled=True, follow=30)
    session.follow_by_list(to_follow['profile'].values.tolist())
    session.end()
    to_follow['scheduled'] = True
    to_follow['following_date'] = now
    followers.update(to_follow)

    followers.to_csv('followers.csv', header=True, index=False)


#schedule.every(1).at(3).minutes.do(insta_strategy)
schedule.every(0).to(10).minutes.do(insta_strategy)
#schedule.every().day.at("18:00").do(insta_strategy)



while True:
    schedule.run_pending()
    time.sleep(1)
