import datetime
import os

from saintexupery.production import  AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY







AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False


AWS_STORAGE_BUCKET_NAME = 'saintexupery'
AWS_S3_ENDPOINT_URL = 'https://saintexupery.fra1.cdn.digitaloceanspaces.com'
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
STATICFILES_STORAGE = 'saintexupery.aws.utils.StaticRootS3BotoStorage'




#------------------------

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}



DEFAULT_FILE_STORAGE = 'saintexupery.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'saintexupery.aws.utils.StaticRootS3BotoStorage'

