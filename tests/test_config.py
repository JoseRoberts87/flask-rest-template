from src import config


def test_dev_config():
    assert config.DevelopmentConfig.DEBUG is True
    assert config.DevelopmentConfig.TESTING is True
    assert config.DevelopmentConfig.SQLALCHEMY_DATABASE_URI == 'sqlite://'


def test_prod_config():
    assert config.ProductionConfig.DEBUG is False
    assert config.ProductionConfig.TESTING is False
    assert config.ProductionConfig.SQLALCHEMY_DATABASE_URI == 'sqlite://'


def test_stage_config():
    assert config.StagingConfig.DEBUG is False
    assert config.StagingConfig.TESTING is True
    assert config.StagingConfig.SQLALCHEMY_DATABASE_URI == 'sqlite://'
