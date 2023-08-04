import requests
from bs4 import BeautifulSoup
from win11toast import toast
import re
from time import sleep

def get_current_matches():
    
    page = requests.get('http://static.cricinfo.com/rss/livescores.xml') 
    soup = BeautifulSoup(page.text,'lxml') # parsing and building xml tree out of the returned xml file
    matches = soup.find_all('description') # description tags contain the score
    live_matches = [s.get_text() for s in matches if '*' in s.get_text()] # returns only the live matches 
    return live_matches

def fetch_score(num3):
    
    page = requests.get('http://static.cricinfo.com/rss/livescores.xml')
    soup = BeautifulSoup(page.text,'lxml')
    matches = soup.find_all('description')
    live_matches = [s.get_text() for s in matches if '*' in s.get_text()]
    return live_matches[num3]

def notipy(score):
    
    # toaster = ToastNotifier()
    # toaster.show_toast(score, "SO FAR!!", duration=5,icon_path='C:\\Users\\LOHITH\\OneDrive\\Desktop\\criclogo.jpg'to)
    toast(score,"SO FAR!!",icon='C:\\Users\\LOHITH\\OneDrive\\Desktop\\criclogo.jpg',on_click='https://www.espncricinfo.com')


if __name__ == "__main__":

    
    matches = get_current_matches()
    print('Current matches in play\n','...'*10)
   
    
    for i,match in enumerate(matches):
                print('[{}] '.format(i) + 
                        re.search('\D+',match.split('v')[0]).group() + 'vs.' +
                        re.search('\D+',match.split('v')[1]).group())

    print()
    matchNum = int(input('Pick the match number [0,1,2...] => '))


    
    while True:
        current_score = fetch_score(matchNum)
        notipy(current_score)
        sleep(2)