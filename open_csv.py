import csv
import numpy as np


m=[]
fpath='MD_19/DADOS/MICRODADOS_ENEM_2019.csv'
counter=0
pos=0
with open(fpath,newline='') as csv_file:
    file_md=csv.reader(csv_file,delimiter=';',quotechar='"')
    for row in file_md:
        if counter == 0:
            m.append(row)
            counter += 1        
        else:
            if row[22]=='Mogi Guaçu':
                m.append(row)
                counter += 1
        pos += 1
print(len(m))
microdados=np.array(m)

dump_file=open('2019.npy','wb')
np.save(dump_file,microdados)
dump_file.close()
