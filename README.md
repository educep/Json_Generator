# Generator of json files
Generation of a json files from a csv table, there are two methods.
The table structure must be respected, each line will be a structure, the specifications in the file are:
    line 1 : data type
    line 2 : fields names
	line n > 2: data in fields
	
By the moment there are 4 possible type fields ('char'=string, 'num'=float, 'bool'=boolean, 'list_int'=list of integers ).

## Case 1: From CSV providing file names
We generate them from a table .csv. The used separator is ';'.

	
**How to Use**

`python gen_json.py filename.csv`

- Reads filename.csv (which must be in the same folder) and writes filename.json

## Case 2: From CSV file names in script (adapted for TourBlink)
The folder must contain 5 csv files whose separator is tab ('\t', this allows to copy-paste directly from the google docs and avoid further treatment):

- monuments_eng = 'monuments_eng.csv'
- monuments_esp = 'monuments_esp.csv'
- districts_eng = 'districts_eng.csv'
- districts_esp = 'districts_esp.csv'
- nbofdays = 'nbdays.csv'

It will produce two json files:
- monuments_model.json
- districts_model.json

**How to Use**

`python generate_all.py`

## Licence
Use as you wish, not responsible for bad functioning outside the TourBlink framework.

**up to date: 05/02/2017**
 
Eduardo Cepeda, Ph.D.
edoo@melix.org