#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://lopesivan.github.com'
RELATIVE_URLS = False

AUTHOR = u'Ivan Lopes'
SITENAME = u'Ivan'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
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
SOCIAL = (('email', 'ivan@42algoritmos.com.br'),
	('twitter', 'https://twitter.com/42iczar42'),
	('linkedin', 'https://br.linkedin.com/in/iczar'),
	('github', 'https://github.com/lopesivan'))

DEFAULT_PAGINATION = 10

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Theme stuff
THEME = "/home/ivan/developer/pelican-themes/pelican-hyde"

BIO = "I'm Ivan Lopes, from south Brazil. Working as Software Engineer. I love Open Source and programming"
PROFILE_IMAGE = "avatar.jpg"

PLUGINS = ['pelican_gist']

DISQUS_SITENAME = "ivan"
GOOGLE_ANALYTICS = "UA-73126405-1"
