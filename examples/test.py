from bitpay.bitpay_exceptions import *
import bitpay.bitpay_key_utils as bku
from bitpay.bitpay_client import *
import pprint
import requests
import json
import re
import os.path

#API_HOST = "https://bitpay.com" #for production, live bitcoin
API_HOST = "https://test.bitpay.com" #for testing, testnet bitcoin
KEY_FILE = "/tmp/key.priv"
TOKEN_FILE = "/tmp/token.priv"

# check if there is a preexisting key file and token file
if os.path.isfile(KEY_FILE) and os.path.isfile(TOKEN_FILE):
    f = open(KEY_FILE, 'r')
    key = f.read()
    f.close()
    f = open(TOKEN_FILE, 'r')
    token = f.read()
    f.close()
else:
    key = bku.generate_pem()
    token = ""

f = open(KEY_FILE, 'w')
f.write(key)
f.close()

if token == "":
    client = Client(API_HOST, False, key)
    pairingCode = client.create_token("merchant")
    print "Please go to:  %s/dashboard/merchant/api-tokens  then enter \"%s\" then click the \"Find\" button, then click \"Approve\"" % (API_HOST, pairingCode)
    raw_input("When you've complete the above, hit enter to continue...")
    print "token is: %s" % client.tokens['merchant']
    f = open(TOKEN_FILE, 'w')
    f.write(client.tokens['merchant'])
    f.close()
else:
    print "Creating a bitpay client using existing tokens and private key from disk."
    client = Client(API_HOST, False, key, {'merchant': token})

print "Now we assume that the pairing code that we generated along with the crypto keys is paired with your merchant account"

print "We will create an invoice using the merchant facade"

invoice = client.create_invoice({"price": 1.00, "currency": "EUR", "token": client.tokens['merchant']})

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(invoice)


print "hopefully the above looks OK?"

print "continuing if we can..."

print "Attempting to get settlements..."

def get_stuff_from_bitpays_restful_api(client, uri, token):
    payload = "?token=%s" % token
    xidentity = bku.get_compressed_public_key_from_pem(client.pem)
    xsignature = bku.sign(uri + payload, client.pem)
    headers = {"content-type": "application/json",
                "X-Identity": xidentity,
                "X-Signature": xsignature, "X-accept-version": "2.0.0"}
    try:
        pp.pprint(headers)
        print uri + payload
        response = requests.get(uri + payload, headers=headers, verify=client.verify)
    except Exception as pro:
        raise BitPayConnectionError(pro.args)
    if response.ok:
        return response.json()['data']
    client.response_error(response)


"""
GET /settlements
https://bitpay.com/api#resource-Settlements
"""
settlements = get_stuff_from_bitpays_restful_api(client, client.uri + "/settlements/", token)
pp.pprint("These are your settlements: %s" % settlements)


print "Now that we have settlements, let's do ledger pages..."
"""
GET /ledgers
https://bitpay.com/api#resource-Ledgers
"""
ledgers = get_stuff_from_bitpays_restful_api(client, client.uri + "/ledgers/", token)
pp.pprint("These are your ledgers: %s" % ledgers)






