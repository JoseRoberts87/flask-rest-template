
import pytest
from src.common.db import alembic_downgrade, alembic_upgrade


@pytest.mark.skip(reason="Not implemented yet")
def test_db_alembic_upgrade(app):
    alembic_upgrade(app)

    assert True


@pytest.mark.skip(reason="Not implemented yet")
def test_db_alembic_downgrade(app):
    alembic_downgrade(app)

    assert True
