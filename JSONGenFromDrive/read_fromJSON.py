# -*- coding: utf-8 -*-
# coding: utf-8 
#05/02/2017
#@author: Eduardo Cepeda


import sys, json

#============================================================================
#                   Auxiliary Methods For Comments
#============================================================================

def create_json_struc(thisline,fieldnames,datatypes):
    currentStruct = {}
    index = 0
    while index < len(thisline):
        #we have 3 options only: (char | bool | num)
        #print('%d,%s'%(index,thisline[index]))
        typeaux = datatypes[index].replace('"','') 
        if typeaux == 'char':
            valaux = str(thisline[index]).replace('\\n','\n')
            currentStruct[fieldnames[index]] = valaux
            #print('%s done'%fieldnames[index])
        elif typeaux == 'num':
            numval = thisline[index]
            currentStruct[fieldnames[index]] = numval
            #print('%s done**'%fieldnames[index])
        elif typeaux == 'list_int':
            listaux = str(thisline[index]).split('-')
            if len(listaux) > 1:
                thislist = list()
                for item in listaux:
                    thislist.append([int(s) for s in item.split(',')])
            else:
                thislist = [int(s) for s in listaux[0].split(',')]

            currentStruct[fieldnames[index]] = thislist
        elif typeaux == 'bool':
            #print(type(thisline[index].lower()))
            boolaux = thisline[index].lower().replace('"','')
            if boolaux == 'true':
                currentStruct[fieldnames[index]] = True
                #print('%s done'%fieldnames[index])
            elif boolaux == 'false':
                currentStruct[fieldnames[index]] = False
    		    #print('%s done'%fieldnames[index])
            else:
                print('%s is not boolean'%thisline[index].lower())
        else:
            print('data type *%s* not recognized'%typeaux)
        index += 1	    
    return currentStruct
#============================================================================
#                           Main method
#============================================================================

def json_fromFileName(MyData):
    """
    #setting separator
    if mysep = 'tab':
        mysep = '\t'
    """
    #reading csv file
    #MyData = read_file(FileName)
    #print(MyData)
    #retrieving data type
    print('Retriving data types: \n(\'char\'=string,\'bool\'=boolean,\'num\'=numerical,\'list_int\'=list of ints)')
    DataTypes = MyData[0]
    nbfields = len(DataTypes)
    print('retrived data: (number of fields = %d)'%nbfields)
    print(*DataTypes,sep=' , ')

    print('Retriving field names:')
    FieldsNames = MyData[1]
    print(*FieldsNames,sep=' , ')

    namestructs = FieldsNames[0]; #we give the name to the structures
    print('we set name structures as field -> '+namestructs+'\n')

    nblines = len(MyData) 
    
    #initializing dict
    FinalStruct = {}
    #FinalStruct[FileName.replace('.csv','')] = {}

    countline = 2 #we begin at line 3 (2 first lines )
    countstructs = 0

    while countline < nblines:
        currentline = MyData[countline]
        if currentline:
            currentstrut = create_json_struc(currentline,FieldsNames,DataTypes)
            #FinalStruct[FileName.replace('.csv','')] [str(countline-2)] = currentstrut
            FinalStruct[int(currentstrut[namestructs])] = currentstrut
            countstructs += 1
    	    #jsonList.append(BasicJson)
        countline += 1

    print('Creating json: %d structures (lines) generated'%(countstructs)) #(2 first lines are specs)
    return FinalStruct
    """
    JsonFileName = 	FileName.replace('.csv','')+'.json';
    with open(JsonFileName, 'w') as jsonfile:
        json.dump(FinalStruct, jsonfile,indent=4, sort_keys=True, ensure_ascii=False)
            
    print('file json <output.json> done')
    """
