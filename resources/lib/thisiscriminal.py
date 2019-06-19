import requests
import re
from bs4 import BeautifulSoup

def get_soup(url):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    print "type: ", type(soup)
    return soup

get_soup("http://feeds.thisiscriminal.com/CriminalShow")

def get_playable_podcast(soup):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup.find_all():
        
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('title')
            #<item><guid isPermaLink="false"> == is causing doubling of first episode
            #title = content.find('title')
            title = title.get_text()

            desc = content.find('itunes:subtitle')
            desc = desc.get_text()
            
            #thumbnail = content.find('itunes:image')
            #thumbnail = thumbnail.get('href')

            #thumbnail = content.find('image')
            #thumbnail = thumbnail.get('src')

            #thumbnail = content.find('image')
            #thumbnail = thumbnail.get('/resources/media/cropped-favicon-2-32x32.png')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
                'desc': desc,
                #'thumbnail': thumbnail
        }
        
        #needto check that item is not null here
        subjects.append(item) 
    
    return subjects


def get_podcast_heading(soup):
    """
    @para: parsed html page
    """
    subjects = []
    
    for content in soup.find_all():    
        
        link = content.find('enclosure')
        link = link.get('url')
        print "\n\nLink: ", link

#        title = content.find('item', {'title'})
#<item><guid isPermaLink="false"> == is causing doubling of first episode
        title = content.find('title')
        title = title.get_text()

        desc = content.find('itunes:subtitle')
        desc = desc.get_text()

        #thumbnail = content.find('itunes:image')
        #thumbnail = thumbnail.get('href')

        #thumbnail = content.find('image')
        #thumbnail = thumbnail.get('src')

        #thumbnail = content.find('image')
        #thumbnail = thumbnail.get('/resources/media/cropped-favicon-2-32x32.png')
        
        item = { 
                'url': link,
                'title': title
                #'desc': desc, THESE MESS IT UP
                #'thumbnail': thumbnail THESE MESS IT UP
        }

        subjects.append(item)

    return subjects


def compile_playable_podcast(playable_podcast):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            #'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            #'info': podcast['desc'],
            'is_playable': True,
    })

    return items
