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
directory = ""
api = SugarCRMAPI(host, clientId, clientSecret)
result = api.oauth2_token(user_name, password)
# Validar access_token
uploaded = False
with open('result.csv', 'wb') as csvfile:
  spamwriter = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
  for dirname, dirnames, filenames in os.walk(directory):
    if uploaded :
      break
    for filename in filenames:
      if uploaded :
        break
      path = os.path.join(dirname, filename)
      filename, file_extension = os.path.splitext(path)
      if file_extension == ".pdf":
        data = {
            "name": basename(filename),
            }
        result = api.save('Documents',data)
        if result['id'] :
          document_id = result['id']
          file_content = open(path,'rb')
          result = api.upload("/Documents/{document_id}/file/filename?format=json&delete_if_fails=true&oauth_token={access_token}".format(access_token=api.access_token,document_id=result["id"]), file_content, 'application/pdf', 'filename')
          # Validar resultado
          url = "{host}#Documents/{document_id}".format(document_id=document_id, host=host) 
          file_name = "{0}{1}".format(basename(filename).encode('utf-8'),file_extension)
          spamwriter.writerow([document_id,file_name , url])
          print "{0} - {1}".format(document_id,file_name)
          uploaded = True
