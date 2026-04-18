'''
    resources.lib.uzg
    ~~~~~~~~~~~~~~~~~
    An XBMC addon for watching NPO Start
    :license: GPLv3, see LICENSE.txt for more details.
    NPO Start = Made by Bas Magre (Opvolger)

'''
import xbmc

from resources.lib.npoapihelpers import NpoHelpers
from resources.lib.npoapiclasses import AddonItems, QueryItems, SeasonItems, Channels, SeasonItems, EpisodesOfSeasonItems, EpisodesOfSerieItems, AllItems, CollectionItems, Broadcasters
from typing import List

class Uzg:
    def __init__(self):
        self.channels = Channels()
        self.allItems = AllItems()
        self.queryItems = QueryItems()
        self.episodesOfSeasonItems = EpisodesOfSeasonItems()
        self.episodesOfSerieItems = EpisodesOfSerieItems()
        self.collectionItems = CollectionItems()
        self.seasonItems = SeasonItems()
        self.broadcasters = Broadcasters()

    def getItems(self, action, guid = None, productId = None, slug = None, text = None) -> List[AddonItems]:
        if action == 'Live kanalen':
            return self.channels.getItems()
        elif action == 'Omroepen':
            buildId = self.broadcasters.getCollectionId()
            return self.broadcasters.getItems(buildId)
        elif action == 'Alle programmas':
            buildId = self.allItems.getBuildId()
            return self.allItems.getItems('https://npo.nl/start/_next/data/{}/categorie/programmas.json?slug=programmas'.format(buildId))
        elif action == 'webcollectie':
            buildId = self.allItems.getBuildId()
            url = 'https://npo.nl/start/_next/data/{}/collectie/{}.json?slug={}'.format(buildId, slug, slug)
            return self.allItems.getItems(url)
        elif action == 'Zoeken':
            if text:
                return self.queryItems.getItems(text)
            return []
        elif action == 'episodesSeason':
            return self.episodesOfSeasonItems.getItems(guid)
        elif action == 'episodesSerie':
            return self.episodesOfSerieItems.getItems(guid)
        elif action == 'collection':
            return self.collectionItems.getItems(guid, slug)
        elif action == 'seasons':
            return self.seasonItems.getItems(slug)
        return None
