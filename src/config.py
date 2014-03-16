import os
from git.config import GitConfigParser

__author__ = 'horimislime'

DEFAULT_GITCONFIG_PATH = '/'.join([os.path.expanduser('~'), '.gitconfig'])


class GitConfig(object):
    def __init__(self, config_location=None):

        path = config_location if config_location else DEFAULT_GITCONFIG_PATH
        try:
            config = GitConfigParser(open(path))
            self.base_url = config.get_value('garnet', 'apiurl')

        except:
            raise '[ERROR] error in .gitconfig'
