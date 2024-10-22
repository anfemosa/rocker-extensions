# Copyright 2019 Open Source Robotics Foundation

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import em
from packaging.version import Version
import pkgutil

from rocker.extensions import name_to_argument
from rocker.core import get_docker_client
from rocker.core import RockerExtension


def get_docker_version():
    docker_version_raw = get_docker_client().version()['Version']
    # Fix for version 17.09.0-ce
    return Version(docker_version_raw.split('-')[0])


class DevTools(RockerExtension):
    @staticmethod
    def get_name():
        return 'am_devtools'

    def __init__(self):
        self._env_subs = None
        self.name = DevTools.get_name()

    def get_environment_subs(self):
        if not self._env_subs:
            self._env_subs = {}
        return self._env_subs

    def get_snippet(self, cliargs):
        snippet = pkgutil.get_data('rocker_extensions', 'templates/devtools_snippet.Dockerfile.em').decode('utf-8')
        return em.expand(snippet, self.get_environment_subs())

    def get_docker_args(self, cliargs):
        return " -e EDITOR"

    @staticmethod
    def register_arguments(parser, defaults={}):
        parser.add_argument(name_to_argument(DevTools.get_name()),
                            action='store_true',
                            default=defaults.get(DevTools.get_name(), None),
                            help="add development tools")
