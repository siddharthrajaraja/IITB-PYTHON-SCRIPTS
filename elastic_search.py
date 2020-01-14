from elasticsearch import Elasticsearch
import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb")
URLS=['http://127.0.0.1:9200']
es=Elasticsearch(URLS)
INDEX='test'
#res=es.indices.create(index=INDEX,ignore=400)
#print(res)

db=client.test
i=2
for x in db.test.find({},no_cursor_timeout=True):
    try:
        del x['_id']
    except Exception as e:
        print(e)
    finally:

        print(es.create(INDEX,'data_set',i,body=x))
        i=i+1