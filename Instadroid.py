#Instadroid.py for testing auto-post and scheduling post via python

#import
from InstagramAPI import InstagramAPI # Instagram API -> https://github.com/LevPasha/Instagram-API-python
from random import randint # random number for random picture
import schedule # Schedule -> https://github.com/dbader/schedule
import time
import os 

#login
usr = "" # username
pwd = ""    # password
API = InstagramAPI(usr,pwd)
API.login()

#caption
caption = ""

def random_picture(): # we require you to rename your picture as number :3
     pic = randint(1,10) # random number ? - ?
     auto_post(pic)
     
def auto_post(pic): # real brute force
    picname = str(pic)+".jpg" # picture name
    strcon = r'\picture' # concat picture directory
    def_path = os.getcwd()+strcon # get current directory
    photo_path = def_path+"\\"+picname
    API.uploadPhoto(photo_path, caption)
    
schedule.every(0.2).minutes.do(random_picture) # every ? minutes
schedule.every(4).hours.do(random_picture) # every ? hours

while True:
    schedule.run_pending() # waiting for schedule
    time.sleep(1) # countdown 1 second
