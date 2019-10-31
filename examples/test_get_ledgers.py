
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

# check if there is a preexisting key file
if os.path.isfile(KEY_FILE):
    f = open(KEY_FILE, 'r')
    key = f.read()
    f.close()
    print("Creating a bitpay client using existing private key from disk.")
else:
    key = bku.generate_pem()
    f = open(KEY_FILE, 'w')
    f.write(key)
    f.close()

client = Client(API_HOST, False, key)

def fetch_token(facade):
    if os.path.isfile(TOKEN_FILE + facade):
        f = open(TOKEN_FILE + facade, 'r')
        token = f.read()
        f.close()
        print("Reading " + facade + " token from disk.")
        #global client
        #client = Client(API_HOST, False, key, {facade: token})
        client.tokens[facade] = token
    else:
        pairingCode = client.create_token(facade)
        print("Creating " + facade + " token.")
        print("Please go to:  %s/dashboard/merchant/api-tokens  then enter \"%s\" then click the \"Find\" button, then click \"Approve\"" % (API_HOST, pairingCode))
        raw_input("When you've complete the above, hit enter to continue...")
        print("token is: %s" % client.tokens[facade])
        f = open(TOKEN_FILE + facade, 'w')
        f.write(client.tokens[facade])
        f.close() 

def get_from_bitpay_api(client, uri, token):
    if "?" in uri:    
        payload = "&token=%s" % token
    else:
        payload = "?token=%s" % token
    xidentity = bku.get_compressed_public_key_from_pem(client.pem)
    xsignature = bku.sign(uri + payload, client.pem)
    headers = {"content-type": "application/json",
                "X-Identity": xidentity,
                "X-Signature": xsignature, "X-accept-version": "2.0.0"}
    try:
        pp.pprint(headers)
        print(uri + payload)
        response = requests.get(uri + payload, headers=headers, verify=client.verify)
    except Exception as pro:
        raise BitPayConnectionError(pro.args)
    if response.ok:
        response = response.json()
        return response
    client.response_error(response)

"""
POST to any resource
Make sure to include the proper token in the params
"""
def post_to_bitpay_api(client, uri, resource, params):
    payload = json.dumps(params)
    print("payload = " + payload)
    uri = uri + "/" + resource
    xidentity = key_utils.get_compressed_public_key_from_pem(client.pem)
    xsignature = key_utils.sign(uri + payload, client.pem)
    headers = {"content-type": "application/json",
               "X-Identity": xidentity,
               "X-Signature": xsignature, "X-accept-version": "2.0.0"}
    try:
        response = requests.post(uri, data=payload, headers=headers,
                                 verify=client.verify)
    except Exception as pro:
        raise BitPayConnectionError(pro.args)
    if response.ok:
        return response.json()['data']
    client.response_error(response)

fetch_token("merchant")

pp = pprint.PrettyPrinter(indent=4)

#Now we assume that the pairing code that we generated along with the crypto keys is paired with your merchant account

print("reading ledger balances")
token = client.tokens['merchant']
ledger_balances = get_from_bitpay_api(client, client.uri + "/ledgers/", token)
pp.pprint(ledger_balances)

print("reading ledger entries")
token = client.tokens['merchant']
ledger_entries = get_from_bitpay_api(client, client.uri + "/ledgers/USD?startDate=2017-09-01&endDate=2017-09-20", token)
pp.pprint(ledger_entries)
