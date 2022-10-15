""" 
   download and change desktop wallpapers automatically
 """

import json
import requests
import PyWallpaper


api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# get the json
response = requests.get(api_url)
content = response.content.decode('UTF-8')

# print(response)
# print(type(content))
# print(content)

# convert string to json

dict_content = json.loads(content) # convert str to dictionary to access key and value
# print(dict_content)

# get the image url
image_url = dict_content['url']
# print(image_url)

# download the image
res = requests.get(image_url)
# print(res)

# save the image
with open('apod.png','wb') as image:
  image.write(res.content)

# set as wallpaper
PyWallpaper.change_wallpaper('F:\Phitron course\phitron problem solving\Python\apod.png')