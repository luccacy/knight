#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 Nicira Neworks, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# If ../quantum/__init__.py exists, add ../ to Python search path, so that
# it will override what happens to be installed in /usr/(local/)lib/python...

import sys

from knight import service
from knight.common import cfg

core_opts = [
    cfg.StrOpt('port', default='8989',
               help=("The host IP to bind to")),
]

def main():

    cfg.CONF(args=sys.argv[1:], project='artisan')

    try:
        deploy_service = service.serve_wsgi(service.DeployApiService)
        deploy_service.wait()
    except RuntimeError, e:
        sys.exit(_("ERROR: %s") % e)


if __name__ == "__main__":
    main()

