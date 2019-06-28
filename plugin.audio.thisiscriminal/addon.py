#criminal podcast
#criminal show
#this is criminal

from xbmcswift2 import Plugin, xbmcgui
from resources.lib import thisiscriminal

plugin = Plugin()

# base url for fetching podcasts 
URL = "http://feeds.thisiscriminal.com/CriminalShow"


@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
#        {
#            'label': plugin.get_string(30000), 
#            'path': "http://www.abc.net.au/radio/stations/RN/live?play=true",
#            'thumbnail': "http://www.abc.net.au/local/global_img/programs/howtolisten.jpg", 
#            'is_playable': True},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://f.prxu.org/criminal/images/aaff5251-e6ab-44da-8886-092289630040/CRIMINAL_LOGOS_FINAL_wt_sq.png"},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.thisiscriminal/resources/media/cropped-favicon-2-180x180-inverted.png"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('new_to_criminal'),
            'thumbnail': "https://f.prxu.org/criminal/images/aaff5251-e6ab-44da-8886-092289630040/CRIMINAL_LOGOS_FINAL_wt_sq.png"},
    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = thisiscriminal.get_soup(URL)
    
    playable_podcast = thisiscriminal.get_playable_podcast(soup)
    
    items = thisiscriminal.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/new_to_criminal/')
def new_to_criminal():
    """
    contains playable podcasts listed as just-in
    """
    #soup = thisiscriminal.compile_new_to_criminal(URL)
    
    compile_ntc = thisiscriminal.get_new_to_criminal
    
    items = thisiscriminal.compile_new_to_criminal(compile_ntc)

    return items


@plugin.route('/latest_episode/')
def latest_episode():
    """
    contains playable podcasts listed as just-in
    """
    soup = thisiscriminal.get_soup(URL)
    
    compile_latest = thisiscriminal.get_latest_episode(soup)
    
    items = thisiscriminal.compile_latest_episode(compile_latest)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = thisiscriminal.get_soup(URL)
    
    playable_podcast1 = thisiscriminal.get_playable_podcast1(soup)
    
    items = thisiscriminal.compile_playable_podcast1(playable_podcast1)

    return items


@plugin.route('/subject_list/')
def subject_list():
    """
    contains a list of navigable podcast by subjects
    """
    items = []

    soup = thisiscriminal.get_soup(URL)
    
    subject_heading = thisiscriminal.get_podcast_heading(soup)
    
    for subject in subject_heading:
        items.append({
            'label': subject['title'],
            'path': plugin.url_for('subject_item', url=subject['url']),
        })

    return items

if __name__ == '__main__':
    plugin.run()
