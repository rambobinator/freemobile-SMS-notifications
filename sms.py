# -*- coding: utf8 -*-

import json
import requests

from config import USER, PASS

class SMS:

	headers = {'content-type': 'application/json'}

	errors = {	200: "Le SMS a été envoyé sur votre mobile.",
				400: "Un des paramètres obligatoires est manquant.",
				402: "Trop de SMS ont été envoyés en trop peu de temps.",
				403: "Le service n'est pas activé sur l'espace abonné, ou login / clé incorrect.",
				500: "Erreur côté serveur. Veuillez réessayer ultérieurement."}

	url = "https://smsapi.free-mobile.fr/sendmsg"

	def __init__(self):
		self.credentials = { "user": USER, "pass": PASS}

	def send(self, message):
		data = self.credentials
		data.update({"msg": message})
		json_data = json.dumps(data)
		r = requests.post(url=self.url, data=json_data, headers=self.headers)
		return (self.errors.get(r.status_code, "Unknow error !"))


if __name__ == '__main__':

	import sys

	if len(sys.argv) == 2:
		sms = SMS()
		print(sms.send(str(sys.argv[1])))
	else:
		print("Usage: ./sms.py message")
