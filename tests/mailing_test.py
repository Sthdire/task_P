import pytest
from table_methods import TM

ml_name = 'test'

tm = TM()

def test_add_mailing_good():
    phone_n = '88005553535'
    message = 'test'
    tm.add_mailing_list(ml_name=ml_name, phone_n=phone_n, message=message)
    ml = tm.get_date(ml_name=ml_name)
    assert ml == (message, phone_n)


def test_change_ml_attributes_good():
    phone_n = '99999'
    message = 'test2'
    tm.change_ml_attributes(ml_name=ml_name, phone_n=phone_n, message_=message)
    ml = tm.get_date(ml_name=ml_name)
    assert ml == (message, phone_n)


def test_delete_mailing_NameError():
    tm.delete_mailing_list(ml_name)
    with pytest.raises(NameError):
        with pytest.raises(NoneType):
            tm.get_date(ml_name=ml_name)
