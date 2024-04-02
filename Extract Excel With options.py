
n1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
n2 = [18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40]

import pandas as pd

for i,j in zip(n1,n2):
    datai = pd.read_excel (fr'C:\Users\aniket.gupta\Downloads\atrangi-{j}.xlsx')

for i in n1:
    dfi = pd.DataFrame(datai, columns=['Q1 Answer'])

def replacetext(dataframename,insrtxt1="Default",insrtxt2="Default",insrtxt3="Default",insrtxt4="Default",insrtxt5="default",insrtxt6="default",insrtxt7="default",insrtxt8="default"):
    text_replace1 = insrtxt1
    text_replace2 = insrtxt2
    text_replace3 = insrtxt3
    text_replace4 = insrtxt4
    text_replace5 = insrtxt5
    text_replace6 = insrtxt6
    text_replace7 = insrtxt7
    text_replace8 = insrtxt8

    dataframename['Q1 Answer'] = dataframename['Q1 Answer'].replace(['A'], text_replace1)
    dataframename['Q1 Answer'] = dataframename['Q1 Answer'].replace(['B'], text_replace2)
    dataframename['Q1 Answer'] = dataframename['Q1 Answer'].replace(['C'], text_replace3)
    dataframename['Q1 Answer'] = dataframename['Q1 Answer'].replace(['D'], text_replace4)
    dataframename['Q1 Answer'] = dataframename['Q1 Answer'].replace(['E'], text_replace5)
    dataframename['Q1 Answer'] = dataframename['Q1 Answer'].replace(['F'], text_replace6)
    dataframename['Q1 Answer'] = dataframename['Q1 Answer'].replace(['G'], text_replace7)
    dataframename['Q1 Answer'] = dataframename['Q1 Answer'].replace(['H'], text_replace8)










