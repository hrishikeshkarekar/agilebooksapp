import pytest
import unittest
import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'Application'))
from python_webapp_flask import app

class ViewTest(unittest.TestCase):

	def setUp(self):
		app.config['TESTING'] = True
		self.app = app.test_client()

	def test_unit_home(self):
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)

	def test_unit_search(self):
		response = self.app.get('/search')
		response = self.app.get('/search', {'searchterm': 'kanban'})
		self.assertEqual(response.status_code, 200)
