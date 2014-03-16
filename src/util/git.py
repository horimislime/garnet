__author__ = 'horimislime'

import re
from legit.scm import get_repo

branch_name_pattern = re.compile('[a-z]+\/([0-9]+)')


def ticket_no(branch_name):
    m = branch_name_pattern.search(branch_name)
    return m.group(1) if m else None


def current_branch_ticket_no():
    r = get_repo()
    return ticket_no(r.head.ref.name) if r else None
