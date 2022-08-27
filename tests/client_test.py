import pytest
from table_methods import TM
from models import client

tm = TM()

phone_n = 'test'

def test_add_client_good():
    timezone = 'test'
    TM.add_client(phone_n, timezone)
    ml = client.query.filter_by(phone_n=phone_n).first()
    assert (ml.phone_n, ml.timezone) == (phone_n, timezone)


def test_change_client_attributes_good():
    timezone = 'test2'
    tm.change_client_attributes(phone_n, timezone)
    ml = client.query.filter_by(phone_n=phone_n).first()
    assert (ml.phone_n, ml.timezone) == (phone_n, timezone)


def test_delete_client_NameError():
    tm.delete_client(phone_n)
    with pytest.raises(NameError):
        with pytest.raises(NoneType):
            client.query.filter_by(phone_n=phone_n).first()
