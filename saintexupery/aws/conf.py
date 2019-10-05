import datetime
import os

from saintexupery.production import  AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY








AWS_STORAGE_BUCKET_NAME = 'saintexupery'
AWS_S3_ENDPOINT_URL = 'https://saintexupery.fra1.digitaloceanspaces.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_STATIC_LOCATION = 'static/'

AWS_MEDIA_LOCATION = 'media/'

STATIC_URL = "{aws_s3_endpoint_url}/{aws_static_location}".format( aws_s3_endpoint_url= AWS_S3_ENDPOINT_URL, aws_static_location= AWS_STATIC_LOCATION)
MEDIA_URL = "{aws_s3_endpoint_url}/{aws_media_location}".format(aws_s3_endpoint_url=AWS_S3_ENDPOINT_URL, aws_media_location= AWS_MEDIA_LOCATION)
MEDIA_ROOT = MEDIA_URL
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


DEFAULT_FILE_STORAGE = 'saintexupery.aws.utils.MediaRootS3BotoStorage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'saintexupery.aws.utils.StaticRootS3BotoStorage'




#------------------------


DEFAULT_FILE_STORAGE = 'saintexupery.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'saintexupery.aws.utils.StaticRootS3BotoStorage'

