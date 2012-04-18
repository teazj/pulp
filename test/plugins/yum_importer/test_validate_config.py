# -*- coding: utf-8 -*-
#
# Copyright © 2011 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)) + "/../../../src/")
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)) + "/../../../plugins/importers/yum_importer/")
import mock
import unittest
from importer import YumImporter
import importer_mocks
from pulp.server.content.plugins.model import Repository

class TestValidateConfig(unittest.TestCase):

    def setUp(self):
        super(TestValidateConfig, self).setUp()
        self.repo = mock.Mock(spec=Repository)
        self.importer = YumImporter()
        self.init()

    def tearDown(self):
        super(TestValidateConfig, self).tearDown()

    def init(self):
        self.data_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "../data"))

    def test_config_feed_url(self):

        # test bad feed_url
        feed_url = "fake://example.redhat.com/"
        config = importer_mocks.get_basic_config(feed_url=feed_url)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        feed_url = "http://example.redhat.com/"
        config = importer_mocks.get_basic_config(feed_url=feed_url)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_ssl_verify(self):
        feed_url = "http://example.redhat.com/"
        ssl_verify = "fake"
        config = importer_mocks.get_basic_config(feed_url=feed_url, ssl_verify=ssl_verify)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        ssl_verify = True
        config = importer_mocks.get_basic_config(feed_url=feed_url, ssl_verify=ssl_verify)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)


    def test_config_ssl_ca_cert(self):
        feed_url = "http://example.redhat.com/"
        ssl_ca_cert = "fake_path_to_ca"
        config = importer_mocks.get_basic_config(feed_url=feed_url, ssl_ca_cert=ssl_ca_cert)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        ssl_ca_cert = os.path.join(self.data_dir, "ca.key")
        config = importer_mocks.get_basic_config(feed_url=feed_url, ssl_ca_cert=ssl_ca_cert)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_ssl_client_cert(self):
        feed_url = "http://example.redhat.com/"
        ssl_client_cert = "fake_path_to_client_cert"
        config = importer_mocks.get_basic_config(feed_url=feed_url, ssl_client_cert=ssl_client_cert)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        ssl_client_cert = os.path.join(self.data_dir, "cert.crt")
        config = importer_mocks.get_basic_config(feed_url=feed_url, ssl_client_cert=ssl_client_cert)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_ssl_client_key(self):
        feed_url = "http://example.redhat.com/"
        ssl_client_key = "fake_path_to_client_key"
        config = importer_mocks.get_basic_config(feed_url=feed_url, ssl_client_key=ssl_client_key)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        ssl_client_key = os.path.join(self.data_dir, "cert.key")
        config = importer_mocks.get_basic_config(feed_url=feed_url, ssl_client_key=ssl_client_key)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_proxy_url(self):
        feed_url = "http://example.redhat.com/"
        proxy_url = "fake://proxy"
        config = importer_mocks.get_basic_config(feed_url=feed_url, proxy_url=proxy_url)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        proxy_url = "http://proxy"
        config = importer_mocks.get_basic_config(feed_url=feed_url, proxy_url=proxy_url)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_max_speed(self):
        feed_url = "http://example.redhat.com/"
        max_speed = "fake_speed"
        config = importer_mocks.get_basic_config(feed_url=feed_url, max_speed=max_speed)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        max_speed = 100
        config = importer_mocks.get_basic_config(feed_url=feed_url, max_speed=max_speed)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_max_speed(self):
        feed_url = "http://example.redhat.com/"
        verify_checksum = "fake_bool"
        config = importer_mocks.get_basic_config(feed_url=feed_url, verify_checksum=verify_checksum)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        verify_checksum = True
        config = importer_mocks.get_basic_config(feed_url=feed_url, verify_checksum=verify_checksum)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_verify_size(self):
        feed_url = "http://example.redhat.com/"
        verify_size = "fake_bool"
        config = importer_mocks.get_basic_config(feed_url=feed_url, verify_size=verify_size)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        verify_size = True
        config = importer_mocks.get_basic_config(feed_url=feed_url, verify_size=verify_size)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_newest(self):
        feed_url = "http://example.redhat.com/"
        newest = "fake_bool"
        config = importer_mocks.get_basic_config(feed_url=feed_url, newest=newest)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        newest = True
        config = importer_mocks.get_basic_config(feed_url=feed_url, newest=newest)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_remove_old(self):
        feed_url = "http://example.redhat.com/"
        remove_old  = "fake_bool"
        config = importer_mocks.get_basic_config(feed_url=feed_url, remove_old=remove_old)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        remove_old  = True
        config = importer_mocks.get_basic_config(feed_url=feed_url, remove_old=remove_old)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_num_threads(self):
        feed_url = "http://example.redhat.com/"
        num_threads = "fake_int"
        config = importer_mocks.get_basic_config(feed_url=feed_url, num_threads=num_threads)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        num_threads = 5
        config = importer_mocks.get_basic_config(feed_url=feed_url, num_threads=num_threads)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_num_old_packages(self):
        feed_url = "http://example.redhat.com/"
        num_old_packages = "fake_int"
        config = importer_mocks.get_basic_config(feed_url=feed_url, num_old_packages=num_old_packages)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        num_old_packages = 4
        config = importer_mocks.get_basic_config(feed_url=feed_url, num_old_packages=num_old_packages)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_purge_orphaned(self):
        feed_url = "http://example.redhat.com/"
        purge_orphaned = "fake_bool"
        config = importer_mocks.get_basic_config(feed_url=feed_url, purge_orphaned=purge_orphaned)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        purge_orphaned = True
        config = importer_mocks.get_basic_config(feed_url=feed_url, purge_orphaned=purge_orphaned)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_checksum_type(self):
        feed_url = "http://example.redhat.com/"
        checksum_type ="fake_checksum"
        config = importer_mocks.get_basic_config(feed_url=feed_url, checksum_type=checksum_type)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        checksum_type ="sha"
        config = importer_mocks.get_basic_config(feed_url=feed_url, checksum_type=checksum_type)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)

    def test_config_skip(self):
        feed_url = "http://example.redhat.com/"
        skip = ""
        config = importer_mocks.get_basic_config(feed_url=feed_url, skip=skip)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertFalse(state)

        skip = {}
        config = importer_mocks.get_basic_config(feed_url=feed_url, skip=skip)
        state, msg = self.importer.validate_config(self.repo, config, [])
        self.assertTrue(state)
