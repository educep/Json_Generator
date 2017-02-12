
from pyexcel_ods import get_data
import json, read_fromJSON, CallDriveAPI

#---------------------------------------------------------------
#            Retrieving Google Sheets from Drive
#---------------------------------------------------------------
FILENAME = ['monuments_espX','monuments_engX','districts_model']
for item in FILENAME:
	CallDriveAPI.DownLoadGoogleSheets(item)

#---------------------------------------
#    generating monuments_model
#---------------------------------------
monumentsjson = 'monuments_model.json'
Monuments = {}

File2Read = 'monuments_espX'
SheetName = 'monuments_espX'
DataInXL = json.loads(json.dumps(get_data('%s.ods'%File2Read)))
Monuments['esp'] = read_fromJSON.json_fromFileName(DataInXL[SheetName])

File2Read = 'monuments_engX'
SheetName = 'monuments_engX'
DataInXL = json.loads(json.dumps(get_data('%s.ods'%File2Read)))
Monuments['eng'] = read_fromJSON.json_fromFileName(DataInXL[SheetName])

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
File2Read = 'districts_model'
SheetName1 = 'districts_esp'
SheetName2 = 'districts_eng'
SheetName3 = 'days'
DataInXL = json.loads(json.dumps(get_data('%s.ods'%File2Read)))

DistrictsModel['districts']['esp'] = read_fromJSON.json_fromFileName(DataInXL[SheetName1])
DistrictsModel['districts']['eng'] = read_fromJSON.json_fromFileName(DataInXL[SheetName2])
DistrictsModel['days'] = read_fromJSON.json_fromFileName(DataInXL[SheetName1])

with open(districtsjson, 'w') as jsonfile:
	json.dump(DistrictsModel, jsonfile,indent=4, sort_keys=True, ensure_ascii=False)
            
print('\n************************************')            
print('file json for districts and days done')
print('*************************************\n')      