import em
import pkgutil
from rocker.core import RockerExtension
from rocker_extensions import name_to_argument


class DevTools(RockerExtension):

    name = 'am_devtools'
    @classmethod
    def get_name(cls):
        return cls.name

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

    @staticmethod
    def register_arguments(parser, defaults={}):
        parser.add_argument(name_to_argument(DevTools.get_name()),
                            action='store_true',
                            default=defaults.get(DevTools.get_name(), None),
                            help="add development tools")
