import datetime
import os

from saintexupery.production import  AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY








AWS_STORAGE_BUCKET_NAME = 'saintexupery'
AWS_S3_ENDPOINT_URL = 'https://saintexupery.fra1.digitaloceanspaces.com/'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_STATIC_LOCATION = 'static/'

AWS_MEDIA_LOCATION = 'media/'

STATIC_URL = AWS_S3_ENDPOINT_URL + 'static/' 
MEDIA_URL =  AWS_S3_ENDPOINT_URL + 'media/'
MEDIA_ROOT = MEDIA_URL
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


DEFAULT_FILE_STORAGE = 'saintexupery.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'saintexupery.aws.utils.StaticRootS3BotoStorage'




#------------------------


DEFAULT_FILE_STORAGE = 'saintexupery.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'saintexupery.aws.utils.StaticRootS3BotoStorage'

