#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Антон Ліневич'
SITENAME = 'Блог Антона Ліневича'
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
STATIC_PATHS = ['images',]

CARD_THUMBNAIL = '360x216'

PLUGINS = [
    'plugins.i18n_subsites',
    'plugins.representative_image',
    'plugins.related_posts',
    'pelican.plugins.sitemap',
    'pelican.plugins.feed_summary',
    'advthumbnailer',  # Generating thumbnails
    'autostatic',  # Easily staticfiles management
]

JINJA_EXTENSIONS = [
    'jinja2.ext.i18n',
]

I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Anton Linevich\'s blog',
    },
    'uk': {
        'SITENAME': SITENAME,
    },
}

I18N_GETTEXT_LOCALEDIR = 'locales'
I18N_GETTEXT_DOMAIN = 'messages'

SHOW_ARTICLE_AUTHOR = True
CC_LICENSE = 'cc-by-nc'

DISQUS_SITENAME = 'linevich'
RELATED_POSTS_MAX = 5
GOOGLE_ANALYTICS_UNIVERSAL = 'UA-43408213-3'
