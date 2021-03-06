#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '沈国栋'
SITENAME = '工具不能代替人类思考'
SITEURL = ''


PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'chs'

# configure of gdshen
THEME = "/home/gdshen/GithubBlog/pelican-elegant"
PLUGIN_PATHS = ['/home/gdshen/GithubBlog/pelican-plugins']
PLUGINS = ['render_math']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

USE_FOLDER_AS_CATEGORY = True
