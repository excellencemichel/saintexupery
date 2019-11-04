import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




SECRET_KEY = 'VtQw@;vh7QE#D^^*%\x0c+3>"d]-uLBoM#[\r(5uR:?mn\nl)8S/Bdt#R@{GfS1Su:%-+@R)>)YBX|^ 0k'




AWS_ACCESS_KEY_ID = "BCVX7TOBI6K3BNFVMO4X"
AWS_SECRET_ACCESS_KEY = "4L8aszYhMkhs/4GbA33QuDDOqn4uRm3NcemPUKTeCgc"




DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': "saintexupery",
    'USER': "michel",
    'PASSWORD': "SaintMichel",
    'HOST': "localhost",
    'PORT': '',
    }
}



EMAIL_HOST="smtp.gmail.com"
EMAIL_HOST_USER= "topub33@gmail.com"
EMAIL_PORT=587
EMAIL_HOST_PASSWORD="To_Pub_33_Passe_$"
EMAIL_USE_TLS=True

DEFAULT_FROM_EMAIL = "Saint Exupéry <topub33@gmail.com>"
