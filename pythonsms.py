
# -*- coding: utf-8 -*-
import requests
import sys
import getopt
import json


def main():
	contacts = {
		#key value pairs, for example:
		#'me': number,
		#'someone': anothernumber
	}
	args = sys.argv[1:]
	try:
		payload = {
			'msisdn':contacts[args[0]],
			'message': ' '.join(args[1:])
		}
	except KeyError: #unknown contact or a number, probaly a number
		payload = {
			'msisdn':args[0],
			'message': ' '.join(args[1:])
		}
	length = len(payload['message'])
#	if length > 110:
#		print 'ERROR message is too long!'
#		return

#	url = "http://www.nova.is/services/SupportService.asmx/sendSMS"
	url = "http://www.vodafone.is/kerfi/sms-kubbur/redirects.php?phone="+args[0]+"&text="+str(payload['message'])
	headers = {'content-type': 'application/x-www-form-urlencoded', 'Referer': 'http://www.vodafone.is/minar/vefsms'}

#	r = requests.post(url, data=json.dumps(payload), headers=headers)
	r = requests.post(url, headers=headers)

	if r.status_code == 200:
		print 'SMS sent to ' + str(payload['msisdn'])
	else:
		print 'Some error!'

if __name__ == "__main__":
	main()