import pandas as pd

chunk_size=10**6

csv=pd.DataFrame(pd.read_csv('Facebook pan india - 800909.csv',sep=',',header=0,index_col=False,error_bad_lines=ignore))
print(csv.to_dict(orient='dict'))
#for chunk in pd.read_csv('Facebook pan india - 800909.csv',chunksize=chunk_size,encoding='utf-8'):
    #print(chunk['S.NO'])