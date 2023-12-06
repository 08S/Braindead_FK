DATABASES = {
  'FK_prod': {
        'ENGINE': 'django.db.backends.sql',
        'NAME': 'FK_Data_All',
        'USER': 'FK_Admin',
        'PASSWORD': 'FK@12345',
        'HOST': 'endpoint.fk-host.com',
        'PORT': '1337',
    }
}

ACCESS_TOKEN_URL = "REDACTED"

BASIC_URL = "https://REDACTED"
BACKEND_URL = "https://REDACTED"


ENVIRONMENT_TYPE = "production"
MAIL_NOTIFICATION_API = "http://REDACTED"
STORE_MASTER_SYNC_ENDPOINT = "http://REDACTED"

AWS_BUCKET_NAME = "s3-bucket-prod-name"

# Sensitive FK Environment Information can be leaked on github

# Developers often clone repositories into their personal accounts
# Repositories are made Public instead of Private

# All these things should be kept in mind before commit

# Critical secrets should not be stored in code. AWS secrets manager should be used ALWAYS

Here is your flag - Braindead_FK{Commit_cautiously}
