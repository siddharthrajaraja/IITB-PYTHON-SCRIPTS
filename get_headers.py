import search_files as searchFiles
import pandas as pd
import xlrd
import datetime
import json
#import pymongo

#from elasticsearch import Elasticsearch
#URLS=['http://127.0.0.1:9200']
#es=Elasticsearch(URLS)
#INDEX='newtest'
#res=es.indices.create(index=INDEX,ignore=400)
#print(res)



#client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb")


def store_the_headers_in_file(headers):
    print()
    print("File_Path \t Tuples")
    Final_to_display=list(zip(searchFiles.address,headers))

    f= open('logs.txt','w+')

    # This will print the headers of every file in terminal : [(file_name, [list_of_headers])]
    for i in range(0,len(Final_to_display)):
        f.write("--------->>>>>>".join([Final_to_display[i][0], ",".join(Final_to_display[i][1])]))
        f.write("\n")
        print(Final_to_display[i][0], "\t" , Final_to_display[i][1])

    f.close()

def display_skipped_files_path(list_of_path):
    print("Files Skipped : ")
    print("Sr.No \t File_PATH")
    
    f=open('skipped_files.txt','w+')

    for i in range(0,len(list_of_path)):
        f.write(str(list_of_path[i]))
        f.write("\n")

        print(i+1,"\t",list_of_path[i])

    f.close()



headers=[]
files_skipped=[]
elements=0

get_Headers_Dictionary={}

if __name__=="__main__":
    #db = client.test

    print(searchFiles.address)
    print("Total number of xlsx files : ",len(searchFiles.address))
    print("Sr.No \t File_path \t \t \t \t Start time \t \t \t \t \t \t End time")
    for I in range(0,len(searchFiles.address)):
        try:
            
            print(I+1,"\t",searchFiles.address[I],"\t \t \t",datetime.datetime.now(),"\t \t \t",end=" " )
            
            #This is one Method to read xlsx file using xlrd
            """
            wb=xlrd.open_workbook(searchFiles.address[i])
            sheet=wb.sheet_by_index(0)
            sheet.cell_value(0,0)
            for i in range(sheet.ncols):
                print(sheet.cell_value(0,i))
            """

            #This is other method to read xlsx file using pandas (more efficient) though takes same time
            # Data can be parsed in chunks -- But data in frames has to be read everytime completely .. 

            df=pd.read_excel(searchFiles.address[I],encoding="utf8",errors='ignore')
            print(datetime.datetime.now())
            cols_per_file=list(map(str,df.columns))
            for each_in_list in range(0,len(cols_per_file)):
                cols_per_file[each_in_list]=str(cols_per_file[each_in_list]).replace(".","_").strip().lower()
                if cols_per_file[each_in_list] in get_Headers_Dictionary:
                    get_Headers_Dictionary[cols_per_file[each_in_list]]+=1
                else:
                    get_Headers_Dictionary[cols_per_file[each_in_list]]=1
                #print(get_Headers_Dictionary)

            headers.append(cols_per_file)

            c=0
            parent_dictionary_array=[]

            for row in df.itertuples():
                i=0
                row_data =list(map(str,row))
                child_dictionary={}
                for j in range(0,len(row_data)):
                    if j==0 and i==0:
                        child_dictionary[cols_per_file[i]]=c
                        c=c+1
                    else:
                        if i!=0:
                            child_dictionary[cols_per_file[i]]=row_data[j]
                            #print(l[i]," : ",row_data[j])
                        i=i+1
                    
                    #print("Child is ",child_dictionary)
                #print(es.create(INDEX,'data_set_newTest',elements,body=child_dictionary))
                #elements+=1

                #parent_dictionary_array.append(child_dictionary)
            #print(parent_dictionary_array)
            
            #db.test.insert_many(parent_dictionary_array)





            
        except:
            
            files_skipped.append([I,searchFiles.address[I]])


    store_the_headers_in_file(headers)
    display_skipped_files_path(files_skipped)    
    print()

    print('Headers are :')
    print(get_Headers_Dictionary)
    with open('headers.txt','w') as outfile:
        json.dump(get_Headers_Dictionary,outfile)
        
    