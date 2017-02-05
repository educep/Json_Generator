# -*- coding: utf-8 -*-
# coding: utf-8 
#05/02/2017
#@author: Eduardo Cepeda

import sys, json, source_json

#---------------------------------------
#        csv + json  file names
#---------------------------------------

monuments_eng = 'monuments_eng.csv'
monuments_esp = 'monuments_esp.csv'
districts_eng = 'districts_eng.csv'
districts_esp = 'districts_esp.csv'
nbofdays = 'nbdays.csv'

#we set the separator to "tab" in
#order to avoid to work further on 
#csv files
myseparator = '\t'

#---------------------------------------
#    generating monuments_model
#---------------------------------------
monumentsjson = 'monuments_model.json'
Monuments = {}

Monuments['esp'] = source_json.json_fromFileName(monuments_esp,myseparator)
Monuments['eng'] = source_json.json_fromFileName(monuments_eng,myseparator)

with open(monumentsjson, 'w') as jsonfile:
	json.dump(Monuments, jsonfile,indent=4, sort_keys=True, ensure_ascii=False)
            
print('\n*****************************')            
print('file json for monuments done')
print('*****************************\n')      

#---------------------------------------
#    generating districts_model
#---------------------------------------
districtsjson = 'districts_model.json'
DistrictsModel = {}
DistrictsModel['districts'] = {}

DistrictsModel['districts']['esp'] = source_json.json_fromFileName(districts_esp,myseparator)
DistrictsModel['districts']['eng'] = source_json.json_fromFileName(districts_eng,myseparator)
DistrictsModel['days'] = source_json.json_fromFileName(nbofdays,myseparator)

with open(districtsjson, 'w') as jsonfile:
	json.dump(DistrictsModel, jsonfile,indent=4, sort_keys=True, ensure_ascii=False)
            
print('\n************************************')            
print('file json for districts and days done')
print('*************************************\n')         