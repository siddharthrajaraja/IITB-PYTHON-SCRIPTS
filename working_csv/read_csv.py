import pandas as pd
import get_csv as getCsv
from elasticsearch import Elasticsearch

URLS=['http://127.0.0.1:9200']
es=Elasticsearch(URLS)

INDEX='test_csv'

#res=es.indices.create(index=INDEX,ignore=400)
#print(res)


inserted_docs=6467
for I in range(1,len(getCsv.address_csv)):
    print("Working on : ", getCsv.address_csv[I])
    print()
    data = pd.read_csv(getCsv.address_csv[I]).to_dict(orient="row")
    for ele in data:
        keys=list(ele.keys())
        
        new_keys=[]
        for i in range(0,len(keys)):
            keys[i]=keys[i].replace('.',' ')
            changedKey=keys[i].replace(':',' ')
            new_keys.append(changedKey.replace(' ','_').lower())
            ele[new_keys[i]]=ele.pop(keys[i])
        #print(ele)
        for key in ele.keys():
            ele[key]=str(ele[key])

        print(es.create(INDEX,'ok',inserted_docs,body=ele,request_timeout=3000))
        inserted_docs+=1



"""
inserted_docs=1



data = pd.read_csv('Amravati.csv').to_dict(orient="row")
for ele in data:
    keys=list(ele.keys())
    
    new_keys=[]
    for i in range(0,len(keys)):
        changedKey=keys[i].replace(':',' ')
        new_keys.append(changedKey.replace(' ','_').lower())
        ele[new_keys[i]]=ele.pop(keys[i])
    print(ele)
    for key in ele.keys():
        ele[key]=str(ele[key])

    print(es.create(INDEX,'ok',inserted_docs,body=ele,request_timeout=3000))
    inserted_docs+=1
"""
        
    