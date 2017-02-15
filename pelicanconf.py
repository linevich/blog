#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

SITENAME = 'Блоґ Антона Ліневича'
SITEURL = '/'

PATH = 'content'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'uk'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/atom-%s.xml'
FEED_USE_SUMMARY = True

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
)

# Social widget
SOCIAL = (('Github', 'https://github.com/linevich'),
          ('Facebook', 'https://facebook.com/anton.linevich'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'theme'
CUSTOM_CSS = 'theme/css/bootstrap-material-design.css'
STATIC_PATHS = [
    'images',
    'favicon',
    'pdf'
]

POST_THUMBNAIL = '623x300'

PLUGINS = [
    'plugins.i18n_subsites',
    'representative_image',
    'autostatic',  # Easily staticfiles management
    'advthumbnailer',  # Generating thumbnails
    'plugins.related_posts',
    'plugins.sitemap',
    'plugins.gzip_cache',
    'pelican_youtube',
    # Disabled until I find the solution: https://github.com/getpelican/pelican-plugins/issues/650
    # 'plugins.feed_summary',
    'minify',
    'plugins.simple_footnotes',

]

JINJA_EXTENSIONS = [
    'jinja2.ext.i18n',
]

I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Anton Linevych\'s blog',
        'TWITTER_USERNAME': 'linevich_en',
        'AUTHOR': 'Anton Linevych'
    },
    'uk': {
        'SITENAME': SITENAME,
        'TWITTER_USERNAME': 'linevich_ua',
        'AUTHOR': 'Антон Ліневич'
    },
}

I18N_GETTEXT_LOCALEDIR = 'locales'
I18N_GETTEXT_DOMAIN = 'messages'

SHOW_ARTICLE_AUTHOR = False
CC_LICENSE = 'cc-by-nc'

DISQUS_SITENAME = 'linevich'
RELATED_POSTS_MAX = 5
GOOGLE_ANALYTICS_UNIVERSAL = 'UA-43408213-3'
DISPLAY_CATEGORIES_ON_MENU = True
USE_OPEN_GRAPH = True
OPEN_GRAPH_FB_APP_ID = 553505671478948
DEFAULT_DATE_FORMAT = "%d/%m/%y"

MINIFY = {
    'remove_comments': True,
    'remove_all_empty_space': True,
    'remove_optional_attribute_quotes': False
}

IMAGE_OPTIMIZATION_ONCE_AND_FOR_ALL = False

MD_EXTENSIONS = [
    'codehilite(css_class=highlight)',
    'extra',
    'toc',
    'captions',
    'smarty',
]

# Original idea of full language name filter: https://goo.gl/oNGKcu
LANGUAGES = {
    'en': 'English',
    'uk': 'Українська',
}


def full_language_name(lang_code):
    return LANGUAGES[lang_code]


JINJA_FILTERS = {
    'full_language_name': full_language_name,
}

TWITTER_CARDS = True