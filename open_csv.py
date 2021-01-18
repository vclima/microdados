import numpy as np
import csv

microdados=[]
fpath='MD_18/DADOS/MICRODADOS_ENEM_2018.csv'
counter=0
pos=0
with open(fpath,newline='') as csv_file:
    file_md=csv.reader(csv_file,delimiter=';',quotechar='"')
    for row in file_md:
        if counter == 0:
            microdados.append(row)
            counter += 1          
        else:
            if(row[22]=='Mogi Guaçu'):
                microdados.append(row)
                counter += 1
        pos += 1
print(len(microdados))
m=np.array(microdados)

dump_file=open('2018.npy','wb')
np.save(dump_file,m)
dump_file.close()
