import json
f=open('headers.txt','r')
f1=open('valid.txt','r')
valid=f1.read()
valid_keys=valid.split('\n')

string=f.read()
headers_dict=json.loads(string)

valid_key_dict={}

for key in headers_dict:
    if key in valid_keys:
        valid_key_dict[key]=headers_dict[key]
        #print(valid_key_dict)

with open('final_valid_headers_for_chart.txt', 'w') as outfile:
    json.dump(valid_key_dict, outfile)