#scp -r  d:/projects/iitb-project/search_files.py tejalt@10.119.2.18:
import os
import re 

address=[]
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
 
        if os.path.join(root,name).lower().endswith('.xlsx') or  os.path.join(root,name).lower().endswith('.xls'):
            address.append(os.path.join(root, name))
            
   #for name in dirs:
      #print(os.path.join(root, name))

#print(address)