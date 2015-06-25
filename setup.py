# coding=utf-8
from distutils.core import setup
setup(
    name="bitpay-py2",
    packages=["bitpay"],
    version="2.3.5",
    description="Accept bitcoin with BitPay",
    author="BitPay Integrations Team",
    author_email="integrations@bitpay.com",
    url="https://github.com/bitpay/bitpay-python-py2",
    download_url="https://github.com/bitpay/bitpay-python-py2/tarball/v2.3.5",
    keywords=["bitcoin", "payments", "crypto"],
    license="MIT License",
    classifiers=["Programming Language :: Python",
                 "Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 2 :: Only",
                 "Development Status :: 5 - Production/Stable",
                 "Environment :: Web Environment",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Topic :: Software Development :: Libraries :: Python Modules",
                 "Topic :: Office/Business :: Financial"],
    long_description="""\
Python Library for integrating with BitPay
-------------------------------------

This library is compatible with Python 2.7.8. It is not compatible with Python 3.

This library is a simple way to integrate your application with
BitPay for taking bitcoin payments. It exposes three basic
functions, authenticating with bitpay, creating invoices,
and retrieving invoices. It is not meant as a replacement for
the entire BitPay API. However, the key_utils module contains
all of the tools you need to use the BitPay API for other
purposes.

© 2015 BitPay, Inc.
"""
)
