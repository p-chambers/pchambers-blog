#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys

AUTHOR = u'Paul Chambers'
SITENAME = u'P Chambers'
SITEURL = 'https://p-chambers.github.io'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'notebooks']

# Most of below borrowed from H Fangohrs blog
#############################################
# # Blogroll
LINKS = (('occ-airconics docs', 'http://occ-airconics.readthedocs.io/en/latest/'),
         ('Next Generation Computational Modelling CDT',
            'http://www.ngcm.soton.ac.uk/'))

# # Social widget
SOCIAL = (('Twitter', 'https://twitter.com/pr_chambers'),
          ('GitHub', 'https://github.com/p-chambers'),
          ('LinkedIn', 'https://uk.linkedin.com/in/paul-chambers-88b72b78'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# install from https://github.com/duilio/pelican-octopress-theme
THEME = 'themes/pelican-bootstrap3'

# what is displayed at the top
MENUITEMS = [('Archives', '/archives.html'),]
             # ('Python', 'categories.html'), ]

# Setting names of output files. Include date, so we can have many entries
# over time:
ARTICLE_URL = '{date:%Y}-{date:%m}-{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}-{date:%m}-{date:%d}/{slug}.html'

# make enttries in 'seminar' to appear in category 'seminar' as default
USE_FOLDER_AS_CATEGORY = True

# Sharing
TWITTER_USER = 'pr_chambers'

# I couldn't get the inlining of tweets to work (HF)
# both IDs should work for NGCM_Soton
TWITTER_WIDGET_ID = 600980431568244737
TWITTER_TWEET_BUTTON = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 5
TWITTER_SHOW_REPLIES = True
TWITTER_SHOW_FOLLOWER_COUNT = True

# Search
SEARCH_BOX = True

# Other pages (not advertised currently)
# TAG_URL = 'tag-{slug}.html'
# TAG_SAVE_AS = 'tag-{slug}.html'

CATEGORY_URL = 'category-{slug}.html'
CATEGORY_SAVE_AS = 'category-{slug}.html'

AUTHOR_URL = 'author-{slug}.html'
AUTHOR_SAVE_AS = 'author-{slug}.html'


# Create archives
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'


# More settings from README.rst in octopress-theme
# Works, is cool. But too geeky.
QR_CODE = False

# Works, but doesn't look good. Let's switch it off.
# SIDEBAR_IMAGE = "images/ngcm.png"
# SIDEBAR_IMAGE_ALT = "NGCM CDT Logo"
# SIDEBAR_IMAGE_WIDTH = 100

# Our (NGCM) additions to the octopress theme - should be push back into
# central
# repo?)
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False

# Allow discussion
DISQUS_SITENAME = "p-chambers"
DISQUSURL = SITEURL

# The remaining entries in this config file are not currently
# used (Oct 2015): we do not need plugins, and we do not have
# IPython notebooks.
# However, we leave the comments here to help with configuration
# should we need this.

# # Tell pelican which directories contains the plugins
PLUGIN_PATHS = ["plugins"]
# # Currently, this directory is empty, but we leave it here
# #

# # The next few lines allow automatic conversion of
# # ipython notebooks to html as blog entries. We use Jake Vanderplaas'
# # liquid_tags.notebook (see
# https://github.com/getpelican//pelican-plugins/blob/master/liquid_tags/Readme.md)

# # Allo use of the following plugins:

PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'render_math', 'extract_toc']
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'toc']

# # The above plugins should in principle allow to integrate a IPython Notebook
# # (see example
# # in content/notebooks) but we deactivate this for now as we never needed it,
# # and it
# # requires additional dependencies (such as markdown for example) which make
# # the whole
# # thing harder to read.

# # the ipython notebook liquid_tags plugin needs the following:
if sys.version_info[0] == 2:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
else:  # python3 and above
    EXTRA_HEADER = open('_nb_header.html').read()

# # Define the directory below which notebooks (*.ipynb) need to be
# # stored
NOTEBOOK_DIR = 'notebooks'


# Add custom css
CUSTOM_CSS = 'static/custom.css'
# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['images', 'extra/custom.css', 'downloads']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}