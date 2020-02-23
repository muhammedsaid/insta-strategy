from instapy import InstaPy
import pandas as pd
import datetime

# login credentials
insta_username = ''  # <- enter username here
insta_password = ''  # <- enter password here

profile = pd.read_json('profile.json')
followers = []

session = InstaPy(username=insta_username, password=insta_password, headless_browser=True, proxy_address='', proxy_port='')

session.login()

for i,z in profile['profiles'].items():

    k = session.grab_followers(username=z, amount="full", live_match=True, store_locally=False)
    followers.append(k)

session.end()

frame = []

for y in followers[0]:
    frame.append(dict(profile=y, script_date=datetime.datetime.now(), scheduled=False))


df = pd.DataFrame(frame)
df.to_csv('followers.csv', sep=',', index=False, header=True)

#followers_csv = pd.read_csv('followers.csv', header=None)
