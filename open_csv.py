import numpy as np
import csv

microdados=[]
fpath='MD_18/DADOS/MICRODADOS_ENEM_2018.csv'
counter=0
with open(fpath,newline='') as csv_file:
    file_md=csv.reader(csv_file,delimiter=';',quotechar='"')
    for row in file_md:
        microdados.append(row)
        counter += 1
print(len(microdados))

