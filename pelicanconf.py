AUTHOR = 'jymmyboi'
SITENAME = 'DevBlog'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Australia/Adelaide'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = '{slug}.html'

DRAFT_URL = 'drafts/{slug}.html'

PAGE_URL = 'pages/{slug}.html'

DISABLE_URL_HASH = True

# Blogroll
LINKS = (
    ("Github", "https://github.com/jymmyboi"),
    ("Twitter", "https://twitter.com/jymmyboi"),
)


DEFAULT_PAGINATION = False

THEME = "./themes/Flex"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True