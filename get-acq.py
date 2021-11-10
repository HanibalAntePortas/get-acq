#!/usr/bin/python3
import requests
import json
import argparse

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-d', '--domains', help='Specify the list with  domains')
parser.add_argument('-a', '--apikey', help='Provide securitytrails API key')
parser.add_argument('-o', '--output', help='Specify output filename')


args = parser.parse_args()
apikey = args.apikey
output = args.output


with open(args.domains, 'r') as f:
	for domain in f:
		domain = domain.strip()
		url = "https://api.securitytrails.com/v1/domain/"+domain+"/acquisitions"
		headers = {"apikey": apikey}
		response = requests.get(url, headers=headers)
		json_data = json.loads(response.text)

with open(output, "a") as o:
	o.write(str(json_data))
