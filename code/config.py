REDIS_URL = 'redis://:ln_pwd_123@redis:6379/0'
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL