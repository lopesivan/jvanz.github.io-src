# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ivan Lopes'
SITENAME = u'Ivan'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('email', 'ivan@42algoritmos.com'),
          ('key', 'https://keybase.io/iczar'),
          ('linkedin', 'https://br.linkedin.com/in/iczar'),
          ('github', 'https://github.com/lopesivan'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Theme stuff
#THEME = ""
#THEME = "/home/ivan/developer/pelican-themes/gum"
THEME = "/home/ivan/developer/pelican-themes/pelican-hyde"
#FAVICON = 'favicon.ico'

BIO = "I'm Ivan Lopes, from south Brazil. Working as Software Engineer. I love Open Source and programming"
PROFILE_IMAGE = "avatar.jpg"

DISQUS_SITENAME = "iczar"

PLUGINS = ['pelican_gist', 'pelican_social']
