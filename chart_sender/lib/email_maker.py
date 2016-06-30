from jinja2 import Template
import os
import re

class NotUrlError(Exception):
    pass

class HTMLEmailMaker():

    TEMPLATE_DIR_NAME = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
    TEMPLATE_NAME = 'email_template.html'

    def insert_snapshots(self, snapshot_urls):
        url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        for url in snapshot_urls:
            if not re.match(url_regex, url.strip()):
                raise NotUrlError('{url} This should be an url'.format(url=url))

        read_html_file = open(os.path.join(self.TEMPLATE_DIR_NAME, self.TEMPLATE_NAME), "r").read()
        template = Template(read_html_file)
        return template.render(charts = snapshot_urls)