# Using the BitPay Python Client Library


## Prerequisites
You must have BitPay or test.bitpay merchant account to use this library. [Signing up for a merchant account](https://bitpay.com/start) is free.

## Quick Start
### Installation

BitPay's python library was developed in Python 2.7.8. The recommended method of installion is using pip.

`pip install 'bitpay-py2'`

### Basic Usage

The bitpay library allows authenticating with BitPay, creating invoices, and retrieving invoices.
  
add the "bitpay" folder to the Python path:

    >>> import sys
    >>> sys.path.append("bitpay")

#### Pairing with Bitpay.com

Before pairing with BitPay.com, you'll need to log in to your BitPay account and navigate to /api-tokens. Generate a new pairing code and use it in the next step. You can try out various functions using the Python REPL. In this example, it's assumed that we are working against the bitpay test server and have generated the pairing code "abcdefg".

    > from bitpay_client import Client
    > client = Client(api_uri="https://test.bitpay.com") #if api_uri is not passed, it defaults to "https://bitpay.com"
    > client.pair_pos_client("abcdefg")

#### To create an invoice with a paired client:

Using the same web client from the last step:

    > client.create_invoice({"price": 20, "currency": "USD", "token": client.tokens['pos']})

That will return the invoice as JSON. Other parameters can be sent, see the [BitPay REST API documentation](https://bitpay.com/api#resource-Invoices) for details.

