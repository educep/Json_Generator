# Generator of json files
Generation of a json files from a Google Sheets in Drive using it's API.
By the moment there are 4 possible type fields ('char'=string, 'num'=float, 'bool'=boolean, 'list_int'=list (of list) of integers ).

Example for list int:

Write in the Google Sheet: 1,2 you obtain: [1,2]
Write in the Google Sheet: 1-2,1-3,6,5 you obtain: [ [1],[2,1],[3,6,5] ]

## Accessing Google APIs from Python
Download and install the library in your usual way, for example:
$ pip install -U google-api-python-client  # or pip3 for 3.x

## Reading .ods Files
pyexcel-ods is a tiny wrapper library to read, manipulate and write data in ods format using python 2.6 and python 2.7. You can install it via pip:

$ pip install pyexcel-ods

# What you need
In order to execute this code, you'll need:

- GDriveAPIKey: Drive API KEY to bet set in CallDriveAPI.py
- Set the SCOPES of your query (the more restrictive the best), for TourBlink use it suffices:
   'https://www.googleapis.com/auth/drive.apps.readonly'
- client_id.json: file with the Drive Project ID and your authentication (mandatory), downloadable from Drive.
- storage.json: file with the permission. If you don't have it, you'll need to allow permission directly on your browser (a window pop up).

**How to Use**
Once you have configured your Drive API (you have client_id.json at least and storage.json).
Set the API KEY in CallDriveAPI.

In the command window:
$ python GenAllFromDrive.py

It will produce two json files:
- monuments_model.json
- districts_model.json


## Licence
Use as you wish, not responsible for bad functioning outside the TourBlink framework.

**up to date: 12/02/2017**
 
Eduardo Cepeda, Ph.D.

edoo@melix.org