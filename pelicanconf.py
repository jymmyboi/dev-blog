AUTHOR = 'jymmyboi'
SITENAME = 'DevBlog'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Australia/Adelaide'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Slug settings
ARTICLE_URL = '{slug}'
DRAFT_URL = 'drafts/{slug}'
PAGE_URL = 'pages/{slug}'

# Flex Settings
DISABLE_URL_HASH = True
THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

# Blogroll
LINKS = (
    ("Github", "https://github.com/jymmyboi"),
    ("Twitter", "https://twitter.com/jymmyboi"),
)


DEFAULT_PAGINATION = False

THEME = "./themes/Flex"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True