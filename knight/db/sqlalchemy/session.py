'''
Created on 2013-9-1

@author: zhouyu
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from knight.common import cfg
from knight.common import logger


core_opts = [
    cfg.StrOpt('sql_conn', default='mysql://root:123456@localhost/battery',
                help=('The knight server listen address')),
]

CONF = cfg.CONF
CONF.register_opts(core_opts)

LOG = logger.get_logger(__name__)

def get_engine(echo=True):

    engine = None

    if engine is None:
        engine = create_engine(CONF.sql_conn, echo=echo)

    return engine

def get_session(autocommit=True, expire_on_commit=False,
                sqlite_fk=False):

    engine = get_engine()
    return scoped_session(sessionmaker(bind=engine,
                        autocommit=autocommit,
                        expire_on_commit=expire_on_commit))