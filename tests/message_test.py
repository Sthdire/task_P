import pytest
from table_methods import TM
from models import message

tm = TM()

message_ = 'test'

def test_add_message_good():
    tm.add_message(message_)
    ml = message.query.filter_by(message=message_).first()
    assert ml.message == message_


def test_delete_message_NameError():
    tm.delete_message(message_)
    with pytest.raises(NameError):
        with pytest.raises(NoneType):
            message.query.filter_by(message=message_).first()
