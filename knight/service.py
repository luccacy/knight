import inspect
import logging as std_logging
import os
import random
import time
from knight.paste.deploy.loadwsgi import loadapp

import wsgi
from knight.common import cfg
from knight.common import logger
from threading import Thread, Event, Lock
from knight import task_scheduler
from knight import timer_scheduler

core_opts = [
    cfg.StrOpt('listen_addr', default='0.0.0.0',
                help=('The knight server listen address')),
    cfg.StrOpt('port', default='8989',
                help=('The knight server listen port')),
    cfg.StrOpt('paste_file', default='/etc/knight/api-paste.ini',
                help=('The knight server paste file')),
]

CONF = cfg.CONF
CONF.register_opts(core_opts)

LOG = logger.get_logger(__name__)


class WsgiService(object):
    """Base class for WSGI based services.

    For each api you define, you must also define these flags:
    :<api>_listen: The address on which to listen
    :<api>_listen_port: The port on which to listen

    """

    def __init__(self, app_name):
        self.app_name = app_name
        self.wsgi_app = None

    def start(self):
        self.wsgi_app = _run_wsgi(self.app_name)
        
    def wait(self):
        self.wsgi_app.wait()


class DeployApiService(WsgiService):
        
    @classmethod
    def create(cls):
        app_name = "knight"
    
        # Setup logging early, supplying both the CLI options and the
        # configuration mapping from the config file
        # We only update the conf dict for the verbose and debug
        # flags. Everything else must be set up in the conf file...
        # Log the options used when starting if we're in debug mode...
                                                                                                                                             
        # Dump the initial option values
        service = cls(app_name)
        return service


def serve_wsgi(cls):
    try:
        service = cls.create()
    except Exception:
        LOG.exception(('In WsgiService.create()'))
        raise 
        
    service.start()
        
    return service
        
def task_loop():
    while True:
        LOG.error('task loop')
        time.sleep(2)
    
def _run_wsgi(app_name):

    configfile=CONF.paste_file
    #configfile = '/etc/knight/api-paste.ini'
    port = CONF.port
    listen_addr = CONF.listen_addr
    appname="knight"
    
    '''
    start tasks scheuler thread
    '''
    thr_custom = Thread(target=task_scheduler.custum_task_scheduler, name='task scheduler')
    thr_custom.start()
    
    '''
    start timer scheduler thread
    '''
    thr_timer = timer_scheduler.TimerThread()
    thr_timer.start()
 
    app = loadapp("config:%s" % os.path.abspath(configfile), appname)
    if not app:
        LOG.error(('No known API applications configured.'))
        return
    
    server = wsgi.Server(appname)    
    server.start(app, port, listen_addr)
    

    return server
