import pandas as pd
import time
import pymongo
import search_files as search


#from excel2json import convert_from_file
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb")

if __name__=="__main__":
    print("Before",time.time())
    db = client.test

    df=pd.read_excel('new.xlsx',encoding="utf8",errors='ignore')
    l=list(map(str,df.columns))
    for i in range(0,len(l)):
        if  "." in list(l[i]):
            L=list(l[i])
            #print(L,"yaha toda")
            ind=L.index(".")
            L[ind]="_"
            L="".join(L)
            l[i]=L
            #print("yaha joda",L)


    c=0
    parent_dictionary_array=[]
    for row in df.itertuples():
        child_dictionary={}
        row_data=list(map(str,row))
        i=0
        for j in range(0,len(row_data)):
            if j==0 and i==0:
                child_dictionary[l[i]]=c
                #print(l[i]," : ",c)
                c=c+1
            else:
                if i!=0:
                    child_dictionary[l[i]]=row_data[j]
                    #print(l[i]," : ",row_data[j])
                i=i+1
            print("Child is",child_dictionary)
                
        parent_dictionary_array.append(child_dictionary)
        #print()
    #for i in range(0,len(parent_dictionary_array)):
    #    print(parent_dictionary_array[i])  
    #    print("\n")  #professions_dict = {}
    
    #db.test.insert_many(parent_dictionary_array)    
    
    #print(l)


    print("After",time.time())
