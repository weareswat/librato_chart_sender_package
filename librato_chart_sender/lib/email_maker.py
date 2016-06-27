from jinja2 import Template
import os

class HTMLEmailMaker():

    TEMPLATE_DIR_NAME = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
    TEMPLATE_NAME = 'email_template.html'

    def insert_snapshots(self, snapshot_urls):
        read_html_file = open(os.path.join(self.TEMPLATE_DIR_NAME, self.TEMPLATE_NAME), "r").read()
        template = Template(read_html_file)
        return template.render(charts = snapshot_urls)