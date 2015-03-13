# BitPay Library for Python 2

Powerful, flexible, lightweight interface to the cryptographically secure BitPay Bitcoin Payment Gateway API.

[![Supported Python versions](https://pypip.in/py_versions/bitpay_py2/badge.svg)](https://pypi.python.org/pypi/bitpay-py2/)
[![Latest Version](https://pypip.in/version/bitpay_py2/badge.svg)](https://pypi.python.org/pypi/bitpay-py2/)
[![](https://travis-ci.org/bitpay/bitpay-python-py2.svg?branch=master)](https://travis-ci.org/bitpay/bitpay-python-py2)

This library is only compatible with Python 2. If you're using Python 3.x, please use our separate [bitpay-python](https://github.com/ionux/bitpay-python) library.

## Getting Started
To get up and running with this library quickly, see the GUIDE here: (https://github.com/bitpay/bitpay-python-py2/blob/master/GUIDE.md)

## API Documentation

API Documentation is available on the [BitPay site](https://bitpay.com/api).

## Running the Tests

Before running the behavior tests, you will need a test.bitpay.com account and you will need to set the local constants. 

To set constants:
    > source tasks/set_constants.sh "https://test.bitpay.com" your@email yourpassword

To run unit tests:
    > nosetests

To run behavior tests:
    > behave
    
## Found a bug?
Let us know! Send a pull request or a patch. Questions? Ask! We're here to help. We will respond to all filed issues.
