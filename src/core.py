# /usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'horimislime'

import subprocess
from .redmine import Redmine
from .cli import parser
from .config import GitConfig
from .util.git import *


def main():
    args = parser.parse_args()
    redmine = Redmine(GitConfig())

    ticket_no = args.branch_name if args.branch_name else current_branch_ticket_no()

    if args.subcommand == 'info':
        print 'Issue title => %s' % redmine.issue_title(ticket_no)

    elif args.subcommand == 'go':
        subprocess.call(['open', redmine.issue_url(ticket_no)])

