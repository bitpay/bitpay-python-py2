import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bitpay')))
from bitpay_exceptions import *
from bitpay_client import Client
from httmock import urlmatch, HTTMock
import requests
import unittest

class TestClient(unittest.TestCase):
  def test_pair_code_check(self):
    """tests whether the pairing code is syntatically correct"""
    new_client = Client()
    with self.assertRaisesRegexp(BitPayArgumentError, "pairing code is not legal"):
      new_client.pair_pos_client("abcd")

  def test_passes_errors_when_pairing(self):
    """web errors should be gracefully passed to the client"""
    new_client = Client()
    def a_request(url, request):
      return {'status_code': 403, 'content': b'{"error": "this is a 403 error"}'}
    with HTTMock(a_request):
      with self.assertRaisesRegexp(BitPayBitPayError, "403: this is a 403 error"):
        new_client.pair_pos_client("a1B2c3d")

  def test_passes_errors_when_creating_invoice(self):
    """web errors should be gracefully passed to the client"""
    new_client = Client()
    def a_request(url, request):
      return {'status_code': 403, 'content': b'{"error": "this is a 403 error"}'}
    with HTTMock(a_request):
      with self.assertRaisesRegexp(BitPayBitPayError, "403: this is a 403 error"):
        new_client.create_invoice({"price": 20, "currency": "USD"})


