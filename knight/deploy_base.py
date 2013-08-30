import os
import sys


class DeployBase(object):

    def create_dhcp(self, args):
        pass

    def get_dhcp(self, id):
        pass

    def update_dhcp(self, id, args):
        pass
        
    def create_kickstart(self, args):
        pass

    def get_kickstart(self, id):
        pass
        
    def update_kickstart(self, id, args):
        pass

    def create_pxe(self, args):
        pass

    def get_pxe(self, id):
        pass

    def update_pxe(self, id, args):
        pass

    def get_service(self, id):
        pass
        
    def create_service(self, args):
        pass

    def update_service(self, id, args):
        pass
    
    def create_deploy(self, args):
        pass
    
    def get_hostname(self, id):
        pass

    def create_hostname(self, args):
        pass

    def update_hostname(self, id, args):
        pass

    def get_firewall(self, id):
        pass

    def create_firewall(self, args):
        pass

    def get_node(self, id):
        pass

    def update_node(self, id, args):
        pass
