from todoListApi.models import OutputEncoder


class _Config():
    DEBUG = False
    RESTFUL_JSON = {'cls': OutputEncoder}


class _DevelopmentConfig(_Config):
    RESTFUL_JSON = {'cls': OutputEncoder}
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://applaudo:123@localhost:5433/week3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = 8080


class _ProductionConfig(_Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'other uri'


class _TestingConfig(_Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'embedded db uri'


mode = dict(
    dev=_DevelopmentConfig,
    test=_TestingConfig,
    prod=_ProductionConfig
)
