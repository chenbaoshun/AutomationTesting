#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : client_mock_test.py
# @Author  : CHIN
# @Time    : 2021-01-23

from client_mock import *
import unittest
from unittest import mock

class WebTest(unittest.TestCase):
	def test_success(self):
		success = mock.Mock(return_value=200)
		send_web = success
		self.assertEqual(visit_web(), success())

	def test_fail(self):
		fail = mock.Mock(return_value=404)
		send_web = fail
		self.assertEqual(visit_web(), success())

if __name__ == '__main__':
    unittest.main()