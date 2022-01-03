from sqlalchemy import Column, Numeric, TEXT
from normbot.utils.sql import BASE, SESSION, INSERTION_LOCK

class Achn(BASE):
    __tablename__ = "achanls"
    id = Column(Numeric, primary_key=True)
    name = Column(TEXT)

    def __init__(self, chat_id):
        self.id = chat_id
        self.name = str(chat_id)

Achn.__table__.create(checkfirst=True)

def antichanl_on(chat_id):
    with INSERTION_LOCK:
        msg = SESSION.query(Achn).get(chat_id)
        if not msg:
            usr = Achn(chat_id)
            SESSION.add(usr)
            SESSION.commit()
        else:
            pass

def antichanl_off(chat_id):
    with INSERTION_LOCK:
        msg = SESSION.query(Achn).get(chat_id)
        if msg:
            SESSION.delete(msg)
            SESSION.commit()
        else:
            SESSION.close()

def is_antichannel(chat_id):
    with INSERTION_LOCK:
        msg = SESSION.query(Achn).get(chat_id)
        if msg:return True
        else:return False