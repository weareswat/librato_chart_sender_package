from unittest2 import TestCase
import os
from chart_sender.lib.email_maker import HTMLEmailMaker
from chart_sender.lib.email_maker import NotUrlError



class HTMLEmailMakerTests(TestCase):

    def test_existing_file(self):
        html_email_maker = HTMLEmailMaker()
        template = os.path.isfile(os.path.join(html_email_maker.TEMPLATE_DIR_NAME, html_email_maker.TEMPLATE_NAME))
        self.assertTrue(template)

    def test_checking_existing_links_in_template(self):
        html_email_maker = HTMLEmailMaker()
        snapshot_urls = ["http://chart/link/1", "http://chart/link/2"]
        html_email = html_email_maker.insert_snapshots(snapshot_urls)
        for snapshot_url in snapshot_urls:
            self.assertTrue(snapshot_url in html_email)

    def test_checking_non_existing_links_in_template(self):
        html_email_maker = HTMLEmailMaker()
        snapshot_urls = ["http://chart/link/1", "http://chart/link/2"]
        html_email = html_email_maker.insert_snapshots(snapshot_urls)
        self.assertFalse("http://chart/link/3" in html_email)

    def test_no_links_in_template(self):
        html_email_maker = HTMLEmailMaker()
        html_email = html_email_maker.insert_snapshots([])
        self.assertFalse('alt="Librato chart"' in html_email)

    def test_wrong_input_returns_error(self):
        html_email_maker = HTMLEmailMaker()
        self.assertRaises(NotUrlError, html_email_maker.insert_snapshots, ['some shit '])
