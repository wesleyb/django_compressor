from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

MEDIA_URL = getattr(settings, 'COMPRESS_URL', settings.MEDIA_URL)
if not MEDIA_URL.endswith('/'):
    raise ImproperlyConfigured(
        'The MEDIA_URL and COMPRESS_URL settings must have a trailing slash.')

MEDIA_ROOT = getattr(settings, 'COMPRESS_ROOT', settings.MEDIA_ROOT)
OUTPUT_DIR = getattr(settings, 'COMPRESS_OUTPUT_DIR', 'cache')
STORAGE = getattr(settings, 'COMPRESS_STORAGE', 'compressor.storage.CompressorFileStorage')

COMPRESS = getattr(settings, 'COMPRESS', not settings.DEBUG)
COMPRESS_CSS_FILTERS = getattr(settings, 'COMPRESS_CSS_FILTERS', ['compressor.filters.css_default.CssAbsoluteFilter'])
COMPRESS_JS_FILTERS = getattr(settings, 'COMPRESS_JS_FILTERS', ['compressor.filters.jsmin.JSMinFilter'])

COMPRESS_LESSC_BINARY = LESSC_BINARY = getattr(settings, 'COMPRESS_LESSC_BINARY', 'lessc')

CLOSURE_COMPILER_BINARY = getattr(settings, 'COMPRESS_CLOSURE_COMPILER_BINARY', 'java -jar compiler.jar')
CLOSURE_COMPILER_ARGUMENTS = getattr(settings, 'COMPRESS_CLOSURE_COMPILER_ARGUMENTS', '')

CSSTIDY_BINARY = getattr(settings, 'CSSTIDY_BINARY',
    getattr(settings, 'COMPRESS_CSSTIDY_BINARY', 'csstidy'))
CSSTIDY_ARGUMENTS = getattr(settings, 'CSSTIDY_ARGUMENTS',
    getattr(settings, 'COMPRESS_CSSTIDY_ARGUMENTS', '--template=highest'))

YUI_BINARY = getattr(settings, 'COMPRESS_YUI_BINARY', 'java -jar yuicompressor.jar')
YUI_CSS_ARGUMENTS = getattr(settings, 'COMPRESS_YUI_CSS_ARGUMENTS', '')
YUI_JS_ARGUMENTS = getattr(settings, 'COMPRESS_YUI_JS_ARGUMENTS', '')

if COMPRESS_CSS_FILTERS is None:
    COMPRESS_CSS_FILTERS = []

if COMPRESS_JS_FILTERS is None:
    COMPRESS_JS_FILTERS = []

DATA_URI_MIN_SIZE = getattr(settings, 'COMPRESS_DATA_URI_MIN_SIZE', 1024)

# rebuilds the cache every 30 days if nothing has changed.
REBUILD_TIMEOUT = getattr(settings, 'COMPRESS_REBUILD_TIMEOUT', 60 * 60 * 24 * 30) # 30 days

# the upper bound on how long any compression should take to be generated
# (used against dog piling, should be a lot smaller than REBUILD_TIMEOUT
MINT_DELAY = getattr(settings, 'COMPRESS_MINT_DELAY', 30) # 30 seconds

# check for file changes only after a delay (in seconds, disabled by default)
MTIME_DELAY = getattr(settings, 'COMPRESS_MTIME_DELAY', None)

# the backend to use when parsing the JavaScript or Stylesheet files
PARSER = getattr(settings, 'COMPRESS_PARSER', 'compressor.parser.BeautifulSoupParser')

# Allows changing verbosity from the settings.
VERBOSE = getattr(settings, "COMPRESS_VERBOSE", False)

# the cache backend to use
CACHE_BACKEND = getattr(settings, 'COMPRESS_CACHE_BACKEND', None)
if CACHE_BACKEND is None:
    # If we are on Django 1.3 AND using the new CACHES setting...
    if getattr(settings, "CACHES", None):
        CACHE_BACKEND = "default"
    else:
        # fallback for people still using the old CACHE_BACKEND setting
        CACHE_BACKEND = settings.CACHE_BACKEND

# enables the offline cache -- a cache that is filled by the compress management command
OFFLINE = getattr(settings, 'COMPRESS_OFFLINE', False)

# invalidates the offline cache after one year
OFFLINE_TIMEOUT = getattr(settings, 'COMPRESS_OFFLINE_TIMEOUT', 60 * 60 * 24 * 365) # 1 year

# The context to be used when compressing the files "offline"
OFFLINE_CONTEXT = getattr(settings, 'COMPRESS_OFFLINE_CONTEXT', {})
if not OFFLINE_CONTEXT:
    OFFLINE_CONTEXT = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    # Adds the 1.3 STATIC_URL setting to the context if available
    if getattr(settings, 'STATIC_URL', None):
        OFFLINE_CONTEXT['STATIC_URL'] = settings.STATIC_URL
