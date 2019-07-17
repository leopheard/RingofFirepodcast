from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

URL = "https://feeds.fans.fm/41.xml"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://s3.amazonaws.com/fansfm_production/1afcee00-2cac-0137-7a39-0f16ad195fd9.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://s3.amazonaws.com/fansfm_production/1afcee00-2cac-0137-7a39-0f16ad195fd9.jpg"},
    ]

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL)
    
    playable_podcast = mainaddon.get_playable_podcast(soup)
    
    items = mainaddon.compile_playable_podcast(playable_podcast)

    return items


if __name__ == '__main__':
    plugin.run()
