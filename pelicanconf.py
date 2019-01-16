#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Omochin'
SITENAME = 'とあるカプセラのチラシの裏'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'
DEFAULT_DATE_FORMAT = '%Y年%m月%d日'
THEME = 'theme'

FAVICON = 'favicon.jpg'
FAVICON_TYPE = 'image/jpg'

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/' + FAVICON: { 'path': FAVICON },
    'extra/post-bg.jpg': { 'path': 'post-bg.jpg' },
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True