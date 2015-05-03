# encoding: utf-8

import requests
from bs4 import BeautifulSoup

class RelatedTube(object):
    URL = 'http://youtube.com/watch?v='
    
    def __init__(self, youtube_video_id):
        self.video = youtube_video_id
    
    def get(self):
        response = requests.get(self.URL +self.video)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content)
            related = soup.findAll('li', {'class': ['related-list-item']})
            return [self.URL + vid_id.find('a').get('href')[9:] for vid_id in related]
    
    def set(self, youtube_video_id):
        self.video = youtube_video_id