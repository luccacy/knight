'''
Created on 2013-9-4

@author: zhouyu
'''

from distutils.core import setup
import py2exe

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # for the versioninfo resources
        self.version = "0.5.0"
        self.company_name = "No Company"
        self.copyright = "no copyright"
        self.name = "knight"
        
manifest_template = '''
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
<assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="x86"
    name="%(prog)s"
    type="win32"
/>
<description>%(prog)s Program</description>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
</dependency>
</assembly>
'''
knightservice = Target(
    # used for the versioninfo resource
    description = "knight service",
    # what to build.  For a service, the module name (not the
    # filename) must be specified!
    modules = ["knight.win_service"],
    cmdline_style = 'pywin32',
    )

includes = ['eventlet', 'webob', 'iso8601', 'pkg_resources','knight', 'pyparsing','netaddr', 'requests','routes', 'SocketServer', 'BaseHTTPServer', 'sqlalchemy.util.queue','serial']

options = {'py2exe':
           {'compressed': 1,
            'optimize': 2,
            'includes' : includes        
            }
           }

setup(
      options = options,
      zipfile = 'lib/share.zip',
      service = [knightservice],      
      )
