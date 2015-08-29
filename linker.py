#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SugarCRMAPI import SugarCRMAPI
import os
from os.path import basename
import csv
host = ""
user_name = ""
password = ""
clientId = ""
clientSecret = ""

api = SugarCRMAPI(host, clientId, clientSecret)
result = api.oauth2_token(user_name, password)

with open('products.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print row['producttemplate_id']
		result = api.create_link("ProductTemplates",row['producttemplate_id'] , "producttemplates_documents_1", row['document_id'])
		print result