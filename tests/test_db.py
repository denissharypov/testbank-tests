import psycopg
import pytest


@pytest.fixture
def db_params():
    return {
        "host": "localhost",
        "port": 5432,
        "dbname": "testbank",
        "user": "postgres",
        "password": "290705dd",
    }


def test_db_connection(db_params):
    with psycopg.connect(**db_params) as conn:
        row = conn.execute("SELECT now()").fetchone()

    assert row is not None


def test_wrong_password(db_params):
    with pytest.raises(psycopg.OperationalError, match="password authentication failed"):
        psycopg.connect(**{**db_params, "password": "wrong-password"})




