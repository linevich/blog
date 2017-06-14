from __future__ import unicode_literals
import os

SITENAME = 'Блоґ Антона Ліневича'
SITEURL = '/'

PATH = 'content'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'uk'

CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_RSS = '%s/rss.xml' % DEFAULT_LANG
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
RELATED_POST_THUMBNAIL = '360x173'

PLUGINS = [
    'plugins.i18n_subsites',
    'plugins.representative_image',
    'autostatic',  # Easily staticfiles management
    'advthumbnailer',  # Generating thumbnails
    'plugins.related_posts',
    'plugins.sitemap',
    'plugins.gzip_cache',
    'org_reader',
    'pelican_youtube',
    # Disabled until I find the solution: https://github.com/getpelican/pelican-plugins/issues/650
    # 'plugins.feed_summary',
    'minify',
    'plugins.simple_footnotes',
]

JINJA_ENVIRONMENT = {
    'extensions': [
        'jinja2.ext.i18n',
        'jinja2.ext.with_',
    ],
}

OPEN_GRAPH_AUTHOR = {
    'first_name': 'Anton',
    'last_name': ' Linevych',
    'username': 'linevich',
    'gender': 0
}

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

LANGUAGES_TRANSLATION_LINK_TEXT = {
    'uk': 'Переглянути Українську версію',
    'en': 'View English version'
}


def full_language_name(lang_code):
    return LANGUAGES[lang_code]


def translation_link_text(lang_code):
    """
    Return translation link text.

    Example:
        View English version of the article.

    :param lang_code: language code
    """
    if lang_code:
        if lang_code in LANGUAGES_TRANSLATION_LINK_TEXT.keys():
            return LANGUAGES_TRANSLATION_LINK_TEXT[lang_code]
        else:
            if lang_code in LANGUAGES.keys():
                return 'View {} version'.format(LANGUAGES[lang_code])


TWITTER_CARDS = True

# Schema.org
SCHEMA_TECH_ARTICLE = 'http://schema.org/TechArticle'
SCHEMA_BLOG_POST = 'http://schema.org/BlogPosting'

SCHEMA_DEFAULT_ARTICLE_SCOPE = SCHEMA_TECH_ARTICLE


def schema_article_scope(article):
    """
    Returns ``itemptype`` value for article scope.

    :param article: article object.
    """
    scope = getattr(article, 'scope', None)
    if scope in ['post', 'blog-post', 'blog_post']:
        return SCHEMA_BLOG_POST
    elif scope:
        return scope
    else:
        return SCHEMA_DEFAULT_ARTICLE_SCOPE


JINJA_FILTERS = {
    'full_language_name': full_language_name,
    'translation_link_text': translation_link_text,
    'schema_article_scope': schema_article_scope,
}

ORG_READER_EMACS_LOCATION = '/usr/bin/emacs'
ORG_READER_EMACS_SETTINGS = os.path.abspath('lisp/config.el')
ORG_READER_BACKEND = "'pelican-html"
