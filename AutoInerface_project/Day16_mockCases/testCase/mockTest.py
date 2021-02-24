#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : mockTest.py
# @Author  : CHIN
# @Time    : 2021-01-23

from Day16_mockCases.testCase import client
from unittest import mock
import unittest

class MockTest(unittest.TestCase):
	def setUp(self):
		self.remove = client.Remove

	def test_fail_send(self):
		fail_send = mock.Mock(return_value='404')
		client.send_request = fail_send
		self.assertEqual(client.visit_ustack(), fail_send())

	def test_success_send(self):
		success_send = mock.Mock(return_value='200')
		client.send_request = success_send
		self.assertEqual(client.visit_ustack(), success_send())

	def test_remove_success(self):
		remove_success = mock.Mock(return_value='success')
		self.remove.rmdir = remove_success
		self.assertEqual(self.remove.exist_get_rmdir(), remove_success())

	def test_remove_fail(self):
		remove_fail = mock.Mock(return_value='fail')
		self.remove.rmdir = remove_fail
		self.assertEqual(self.remove.exist_get_rmdir(), remove_fail())



if __name__ == '__main__':
    unittest.main(verbosity=2)