import logging.config
import os

def setup_logging(name):
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s|%(name)8s|%(levelname)-7s|%(message)s',
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'filename': os.path.join(os.path.dirname(__file__), 'master_curriculum.log',)
            },
        },
        'loggers': {
            name: {
                'level': 'DEBUG',
                'handlers': ['console', ],
            },
        },
    })
    return logging.getLogger(name)
