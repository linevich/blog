"""
This file is only used if you use `make publish` or explicitly specify it as your config file.
"""

from __future__ import unicode_literals

import os
import sys
from pelicanconf import *

sys.path.append(os.curdir)

SITEURL = 'https://linevi.ch'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_RSS = '%s/rss.xml' % DEFAULT_LANG
FEED_USE_SUMMARY = True
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Anton Linevych\'s blog',
        'TWITTER_USERNAME': 'linevich_en',
        'AUTHOR': 'Anton Linevych',
        'FEED_RSS': 'en/rss.xml',
        'CATEGORY_FEED_RSS': 'feeds/%s.rss.xml',
    },
    'uk': {
        'SITENAME': SITENAME,
        'TWITTER_USERNAME': 'linevich_ua',
        'AUTHOR': 'Антон Ліневич'
    },
}

DELETE_OUTPUT_DIRECTORY = True
PLUGINS += PRODUCTION_ONLY_PLUGINS
