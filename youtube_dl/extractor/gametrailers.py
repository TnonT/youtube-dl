from __future__ import unicode_literals

import re

from .mtv import MTVServicesInfoExtractor


class GametrailersIE(MTVServicesInfoExtractor):
    _VALID_URL = r'http://www\.gametrailers\.com/(?P<type>videos|reviews|full-episodes)/(?P<id>.*?)/(?P<title>.*)'
    _TEST = {
        'url': 'http://www.gametrailers.com/videos/zbvr8i/mirror-s-edge-2-e3-2013--debut-trailer',
        'file': '70e9a5d7-cf25-4a10-9104-6f3e7342ae0d.mp4',
        'md5': '4c8e67681a0ea7ec241e8c09b3ea8cf7',
        'info_dict': {
            'title': 'Mirror\'s Edge 2|E3 2013: Debut Trailer',
            'description': 'Faith is back!  Check out the World Premiere trailer for Mirror\'s Edge 2 straight from the EA Press Conference at E3 2013!',
        },
    }

    _FEED_URL = 'http://www.gametrailers.com/feeds/mrss'

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)
        video_id = mobj.group('id')
        webpage = self._download_webpage(url, video_id)
        mgid = self._search_regex([r'data-video="(?P<mgid>mgid:.*?)"',
                                   r'data-contentId=\'(?P<mgid>mgid:.*?)\''],
                                  webpage, 'mgid')
        return self._get_videos_info(mgid)
