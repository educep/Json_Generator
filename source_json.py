# -*- coding: utf-8 -*-
# coding: utf-8 
#05/02/2017
#@author: Eduardo Cepeda


import sys, json

#============================================================================
#                   Auxiliary Methods For Comments
#============================================================================

def read_file(file_name):
    #for writing a text file
    file_ = open(file_name, 'r')
    with file_:
        content = file_.readlines()
    #file_.flush()
    file_.close()
    return content

def retrieve_data(thisdata,thisline,thissep,dropquotes):
    nblines = len(thisdata);
    dataout = list()
    fieldsin = thisdata[thisline-1].split(thissep)
    nblines = len(fieldsin)
    countline = 0
    while countline < nblines:
    	#needed to delete the \n at the end of the line
        valsaux = fieldsin[countline].replace('\n','')
        if dropquotes:
            valsaux = valsaux.replace('"','') 
        dataout.append(valsaux)
        countline = countline + 1
    return dataout

def create_json_struc(thisline,fieldnames,datatypes):
    currentStruct = {}
    index = 0
    while index < len(thisline):
        #we have 3 options only: (char | bool | num)
        #print('%d,%s'%(index,thisline[index]))
        typeaux = datatypes[index].replace('"','') 
        if typeaux == 'char':
            currentStruct[fieldnames[index]] = thisline[index]
            #print('%s done'%fieldnames[index])
        elif typeaux == 'num':
            numval = thisline[index].replace('"','')
            currentStruct[fieldnames[index]] = float(numval.replace(',','.'))
            #print('%s done'%fieldnames[index])
        elif typeaux == 'list_int':
            listaux = thisline[index].replace('[','').replace(']','')
            currentStruct[fieldnames[index]] = [int(s) for s in listaux.split(',')]
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
    #print(currentStruct)
    return currentStruct
#============================================================================
#                           Main method
#============================================================================

def json_fromFileName(FileName,mysep):
    """
    #setting separator
    if mysep = 'tab':
        mysep = '\t'
    """
    
    #reading csv file
    MyData = read_file(FileName)

    #retrieving data type
    print('Retriving data types: \n(\'char\'=string,\'bool\'=boolean,\'num\'=numerical,\'list_int\'=list of ints)')
    DataTypes = retrieve_data(MyData,1,mysep,True)
    nbfields = len(DataTypes)
    print('retrived data: (number of fields = %d)'%nbfields)
    print(*DataTypes,sep=' , ')

    print('Retriving field names:')
    FieldsNames = retrieve_data(MyData,2,mysep,True)
    print(*FieldsNames,sep=' , ')

    namestructs = FieldsNames[0]; #we give the name to the structures
    print('we set name structures as field -> '+namestructs+'\n')

    nblines = len(MyData) 
    print('Creating json: %d structures (lines) defined'%(nblines-2)) #(2 first lines are specs)

    #initializing dict
    FinalStruct = {}
    #FinalStruct[FileName.replace('.csv','')] = {}

    countline = 3 #we begin at line 3 (2 first lines )

    while countline <= nblines:
        currentline = retrieve_data(MyData,countline,mysep,'')
        currentstrut = create_json_struc(currentline,FieldsNames,DataTypes)
        #FinalStruct[FileName.replace('.csv','')] [str(countline-2)] = currentstrut
        FinalStruct[int(currentstrut[namestructs])] = currentstrut
    	#jsonList.append(BasicJson)
        countline += 1

    return FinalStruct
    """
    JsonFileName = 	FileName.replace('.csv','')+'.json';
    with open(JsonFileName, 'w') as jsonfile:
        json.dump(FinalStruct, jsonfile,indent=4, sort_keys=True, ensure_ascii=False)
            
    print('file json <output.json> done')
    """
