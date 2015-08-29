#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SugarCRMAPI import SugarCRMAPI
import os
from os.path import basename
import csv
import mimetypes
host = ""
user_name = ""
password = ""
clientId = ""
clientSecret = ""
directory = ""
field_name = ""
csv_import = ""
module_name = ""



api = SugarCRMAPI(host, clientId, clientSecret)
result = api.oauth2_token(user_name, password)

with open(csv_import, 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		url = "{module_name}/{1}/file/{3}?format=json&delete_if_fails=true&oauth_token={2}".format(module_name=module_name,row['producttemplate_id'], api.access_token, )
		path = "{1}/{0}".format(row['path'],directory)
		file_content = open(path,'rb')
		filename, file_extension = os.path.splitext(path)
		content_type = mimetypes.types_map[file_extension]
		result = api.upload(url, file_content, content_type, field_name)
		print "{0}#ProductTemplates/{1}".format(host,row['producttemplate_id'])

		