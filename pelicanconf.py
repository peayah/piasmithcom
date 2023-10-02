AUTHOR = 'peayah'
SITENAME = 'python, pandas and ponderings'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "theme/myresponsiveidea"

# PAGE_ORDER_BY = 'Order'

# Blogroll
LINKS = (('flask', 'https://flask.palletsprojects.com/en/3.0.x/'),
         ('jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('matplotlib', 'https://matplotlib.org/stable/users/index'),
         ('numPy', 'https://numpy.org/'),
         ('pandas', 'https://pandas.pydata.org/'),
         ('pelican', 'https://getpelican.com/'),
         ('postgreSQL', 'https://www.postgresql.org/'),
         ('python.org', 'https://www.python.org/'),
         ('seaborn', 'https://seaborn.pydata.org/'),
         ('tkinter','https://docs.python.org/3/library/tkinter.html'),)

# Social widget
SOCIAL = (( 'https://github.com/peayah', ''),
         ('https://twitter.com/pia_smith', ''),
          )

DEFAULT_PAGINATION = 20

STATIC_PATHS = [
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/LICENSE': {'path': 'LICENSE'},
    'extra/README': {'path': 'README'},
}

ARTICLE_EXCLUDES = [
    'extra'
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
