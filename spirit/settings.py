#-*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE
# YOU MAY OVERWRITE THE DEFAULT VALUES IN YOUR settings.py FILE

import os

ST_COMMENTS_PER_PAGE = 20
ST_COMMENTS_PAGE_VAR = 'page'

ST_TOPIC_PRIVATE_CATEGORY_PK = 1
ST_UNCATEGORIZED_CATEGORY_PK = 2

ST_RATELIMIT_ENABLE = True
ST_RATELIMIT_CACHE_PREFIX = 'srl'
ST_RATELIMIT_CACHE = 'default'

ST_NOTIFICATIONS_PER_PAGE = 20

ST_MENTIONS_PER_COMMENT = 30

ST_YT_PAGINATOR_PAGE_RANGE = 3

ST_SEARCH_QUERY_MIN_LEN = 3

ST_USER_LAST_SEEN_THRESHOLD_MINUTES = 1

ST_PRIVATE_FORUM = False

ST_ALLOWED_UPLOAD_IMAGE_FORMAT = ('jpeg', 'png', 'gif')
ST_ALLOWED_UPLOAD_IMAGE_EXT = ST_ALLOWED_UPLOAD_IMAGE_FORMAT + ('jpg', )

# check out http://pythonhosted.org/Markdown/extensions/index.html
ST_MARKDOWN_EXT = (
    'nl2br',
    'fenced_code',
    'spirit.utils.markdown.mention',
    'spirit.utils.markdown.emoji',
    'spirit.utils.markdown.image',
    'spirit.utils.markdown.video',
    'spirit.utils.markdown.audio',
    'spirit.utils.markdown.youtube',
    'spirit.utils.markdown.vimeo',
)


#
# Django settings defined below...
#

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'spirit',
    'haystack',
    'djconfig',
    #'debug_toolbar'
)

# python manage.py createcachetable spirit_cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'spirit_cache',
    },
}

AUTH_USER_MODEL = 'spirit.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'spirit.backends.user.EmailAuthBackend',
)

LOGIN_URL = 'spirit:user-login'
LOGIN_REDIRECT_URL = 'spirit:profile-update'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'spirit.middleware.XForwardedForMiddleware',
    'spirit.middleware.TimezoneMiddleware',
    'spirit.middleware.LastIPMiddleware',
    'spirit.middleware.LastSeenMiddleware',
    'spirit.middleware.ActiveUserMiddleware',
    'spirit.middleware.PrivateForumMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

# Keep templates in memory
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

#
# Third-party apps settings defined below...
#

# django-djconfig

DJC_BACKEND = 'djconfig'

CACHES.update({
    'djconfig': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
})

MIDDLEWARE_CLASSES += (
    'djconfig.middleware.DjConfigLocMemMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'djconfig.context_processors.config',
)

# django-haystack

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}