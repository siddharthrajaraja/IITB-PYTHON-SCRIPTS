import json
import re

#print(headers_json)

valid_headers=[]
invaid_headers=[]

def numbersCount(ele):   # This function checks total number of digits <=2 in a key using Counting sort algorithm
    z=list(map(int,('0'*10)))
    for i in range(0,len(ele)):
        if ord(ele[i]) in range(ord('0'),ord('9')+1):
            z[abs(ord('0')-ord(ele[i]))]+=1
    if sum(z)>2:
        return 0
    return 1

def write_to_file(fileName,l):
    file=open(fileName,'w',encoding='utf-8')

    for item in l:
        file.write(str(item)+'\n')



if __name__=="__main__":
    numbersCount("5")
    file=open('headers.txt','r')

    headers=file.read()

    headers_json=json.loads(headers)

    # Basics of separation  --->
    # 1) Key length <15 and key length>3
    # 2) key matches with pattern (\w)*
    # 3) unnamed should not be involved in headers
    # 4) numberCount() gives True 
    for key in headers_json.keys():
        flag=0
            
        if "unnamed" not in key and len(key)>1:
                if numbersCount(key)==1:
                    if "@" not in key:
                        if "<b>" not in key:
                            if "<p>" not in key:
                                if "<br />" not in key:
                                    if re.findall("http://",key)==[]:
                                        if re.findall("https://",key)==[]:
                                            if headers_json[key]>1:
                                                flag=1

        if flag==0:
            invaid_headers.append(key)
        else:
            valid_headers.append(key)

    write_to_file('invalid.txt',invaid_headers)
    write_to_file('valid.txt',valid_headers)
