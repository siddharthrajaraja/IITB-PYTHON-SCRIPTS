import search_files as searchFiles
import pandas as pd
import xlrd
import datetime

def store_the_headers_in_file(headers):
    print()
    print("File_Path \t Tuples")
    Final_to_display=list(zip(searchFiles.address,headers))
    for i in range(0,len(Final_to_display)):
        print(Final_to_display[i][0], "\t" , Final_to_display[i][1])




headers=[]
if __name__=="__main__":
    print(searchFiles.address)
    print("Total number of xlsx files : ",len(searchFiles.address))
    print("Sr.No \t File_path \t \t \t \t Start time \t \t \t \t \t \t End time")
    for i in range(0,len(searchFiles.address)):
            print(i+1,"\t",searchFiles.address[i],"\t \t \t",datetime.datetime.now(),"\t \t \t",end=" " )
            
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

            df=pd.read_excel(searchFiles.address[i],encoding="utf8",errors='ignore')
            print(datetime.datetime.now())
            cols_per_file=list(map(str,df.columns))
            for each_in_list in range(0,len(cols_per_file)):
                cols_per_file[each_in_list]=str(cols_per_file[each_in_list]).replace(".","_").strip()

            headers.append(cols_per_file)
    store_the_headers_in_file(headers)
        