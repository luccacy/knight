import os
import sys

from knight.deploy_base import DeployBase
from knight.driver import default_driver

class DeployAgent(DeployBase):

    def __init__(self):
        self._driver = default_driver.DefaultDriver()

    def create_dhcp(self, args):
        return self._driver.create_dhcp(args)

    def get_dhcp(self, id):
        return self._driver.get_dhcp(id) 

    def update_dhcp(self, id, args):
        return self._driver.update_dhcp(id, args)
        
    def create_kickstart(self, args):
        return self._driver.create_kickstart(args)

    def get_kickstart(self, id):
        return self._driver.get_kickstart(id) 
        
    def update_kickstart(self, id, args):
        return self._driver.update_kickstart(id, args)

    def create_pxe(self, args):
        return self._driver.create_pxe(args)

    def get_pxe(self, id):
        return self._driver.get_pxe(id) 

    def update_pxe(self, id, args):
        return self._driver.update_pxe(id, args)

    def get_service(self, id, **kwargs):
        return self._driver.get_service(id, **kwargs)
        
    def create_service(self, args):
        return self._driver.create_service(args) 

    def update_service(self, id, args):
        return self._driver.update_service(id, args) 
    
    def create_deploy(self, args):
        return self._driver.create_deploy(args) 
    
    def get_hostname(self, id):
        return self._driver.get_hostname(id)

    def create_hostname(self, args):
        return self._driver.create_hostname(args)

    def update_hostname(self, id, args):
        return self._driver.update_hostname(id, args)

    def get_firewall(self, id):
        return self._driver.get_firewall(id)

    def create_firewall(self, args):
        return self._driver.create_firewall(args) 

    def get_node(self, id):
        return self._driver.get_node(id)

    def update_node(self, id, args):
        return self._driver.update_node(id, args)

    def get_system(self, id):
        return self._driver.get_system(id)

    def create_interface(self, args):
        return self._driver.create_interface(args)
