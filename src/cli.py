import pkg_resources
import argparse

__author__ = 'horimislime'
__version__ = pkg_resources.require('garnet')[0].version

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='subcommand')

infoparser = subparser.add_parser('info')
infoparser.add_argument(
    'branch_name',
    action='store_true',
    help='show related ticket info')
infoparser.add_argument('branch_name', nargs='?', default='')

goparser = subparser.add_parser('go')
goparser.add_argument(
    'branch_name',
    action='store_true',
    help='Open related redmine ticket page')
goparser.add_argument('branch_name', nargs='?', default='')

parser.add_argument('--version',
                    action='version',
                    version=__version__)

parser.add_argument('--debug')
