f_logs=open('logs.txt','r')
logs=f_logs.readlines()

f_valid=open('valid.txt','r')
valid_headers=f_valid.read().split("\n")

def write_to_file(fileName,l):
    file=open(fileName,'w',encoding='utf-8')

    for item in l:
        file.write(str(item)+'\n')


if __name__=="__main__":
        
    solution_valid_files=[]
    solution_invalid_files=[]
    for line_logs in logs:
        invalid=0
        valid=0

        file_name=line_logs.split('--------->>>>>>')[0]
        headers_list=line_logs.split('--------->>>>>>')[1].split('\n')[0].split(',')
        #print(headers_list)
        for i in range(0,len(headers_list)):
            if headers_list[i] in valid_headers:
                valid+=1
            else:
                invalid+=1
        if valid>invalid:
            #print("--------->>>>>>".join([file_name,",".join(headers_list)]))
            solution_valid_files.append("--------->>>>>>".join([file_name,",".join(headers_list)]))
            #write_to_file('valid_files.txt',[])
        else:
            solution_invalid_files.append("--------->>>>>>".join([file_name,",".join(headers_list)]))
    write_to_file('invalid_files.txt',solution_invalid_files)
    write_to_file('valid_files.txt',solution_valid_files)

