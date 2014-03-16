__author__ = 'horimislime'

import json
import requests


class Redmine(object):
    def __init__(self, config):
        self.base_url = config.base_url

    def issue_title(self, ticket_no):
        if not ticket_no:
            return

        api_url = '%s/issues/%s.json' % (self.base_url, ticket_no)
        response = requests.get(api_url)
        if response.status_code is not 200:
            raise 'Invalid http status: %d' % response.status_code

        return json.loads(response.text)['issue']['subject']

    def issue_url(self, issue_no):
        return '%s/issues/%s' % (self.base_url, str(issue_no))
