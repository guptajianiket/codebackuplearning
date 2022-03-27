import pandas as pd

#Reading the CSV report
data1 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP1.csv')
data2 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP2.csv')
data3 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP5.csv')
data4 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP6.csv')
data5 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP7.csv')
data6 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP8.csv')
data7 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP9.csv')


# creating data frame based on submitted answer column from the detailed report

df1 = pd.DataFrame(data1, columns=['Q1 Answer'])
df2 = pd.DataFrame(data2, columns=['Q1 Answer'])
df3 = pd.DataFrame(data3, columns=['Q1 Answer'])
df4 = pd.DataFrame(data4, columns=['Q1 Answer'])
df5 = pd.DataFrame(data5, columns=['Q1 Answer'])
df6 = pd.DataFrame(data6, columns=['Q1 Answer'])
df7 = pd.DataFrame(data7, columns=['Q1 Answer'])

#replacing the default option name with the actual option name. (A,B... to Harsh, Bharti....)

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

replacetext(df1,"Haarsh","Bharti","Nikki","Pratik","Punit Pathak","Gunjan","Garvit")
replacetext(df2,"Haarsh","Bharti","Nikki","Pratik","Punit Pathak","Gunjan","Garvit")
replacetext(df3,"Haarsh","Bharti","Munmun","Prateek","Umar")
replacetext(df4,"Haarsh","Bharti","Munmun","Prateek","Umar")
replacetext(df5,"Haarsh","Bharti","Umar","Rashmi","Prince","Yuvika")
replacetext(df6,"Bharti","Haarsh","Karan","Ankita","Pratik","Nikki")
replacetext(df7,"Bharti","Harsh","Harbhajan","Geeta","Pratik","Nikki","Rashmi","Umar")

# count of options submitted for each episode and question
count1 = df1['Q1 Answer'].value_counts()
count2 = df2['Q1 Answer'].value_counts()
count3 = df3['Q1 Answer'].value_counts()
count4 = df4['Q1 Answer'].value_counts()
count5 = df5['Q1 Answer'].value_counts()
count6 = df6['Q1 Answer'].value_counts()
count7 = df7['Q1 Answer'].value_counts()

# creating the data frame of count table

dff1 = pd.DataFrame(count1)
dff2 = pd.DataFrame(count2)
dff3 = pd.DataFrame(count3)
dff4 = pd.DataFrame(count4)
dff5 = pd.DataFrame(count5)
dff6 = pd.DataFrame(count6)
dff7 = pd.DataFrame(count7)

# Creating a data frame
dftotal1 = pd.DataFrame({'Q1 Answer':{'Total': len(df1)}})
dftotal2 = pd.DataFrame({'Q1 Answer':{'Total': len(df2)}})
dftotal3 = pd.DataFrame({'Q1 Answer':{'Total': len(df3)}})
dftotal4 = pd.DataFrame({'Q1 Answer':{'Total': len(df4)}})
dftotal5 = pd.DataFrame({'Q1 Answer':{'Total': len(df5)}})
dftotal6 = pd.DataFrame({'Q1 Answer':{'Total': len(df6)}})
dftotal7 = pd.DataFrame({'Q1 Answer':{'Total': len(df7)}})

dff1 = pd.concat([dff1,dftotal1],ignore_index=False,axis=0)
dff2 = pd.concat([dff2,dftotal2],ignore_index=False,axis=0)
dff3 = pd.concat([dff3,dftotal3],ignore_index=False,axis=0)
dff4 = pd.concat([dff4,dftotal4],ignore_index=False,axis=0)
dff5 = pd.concat([dff5,dftotal5],ignore_index=False,axis=0)
dff6 = pd.concat([dff6,dftotal6],ignore_index=False,axis=0)
dff7 = pd.concat([dff7,dftotal7],ignore_index=False,axis=0)

print(dff1)
print(dff2)
print(dff3)
print(dff4)
print(dff5)
print(dff6)
print(dff7)

# determining the name of the file
file_name1 = 'TKKS_episode1_Data.xlsx'
file_name2 = 'TKKS_episode2_Data.xlsx'
file_name3 = 'TKKS_episode5_Data.xlsx'
file_name4 = 'TKKS_episode6_Data.xlsx'
file_name5 = 'TKKS_episode7_Data.xlsx'
file_name6 = 'TKKS_episode8_Data.xlsx'
file_name7 = 'TKKS_episode9_Data.xlsx'




# saving the excel
dff1.to_excel(file_name1)
dff2.to_excel(file_name2)
dff3.to_excel(file_name3)
dff4.to_excel(file_name4)
dff5.to_excel(file_name5)
dff6.to_excel(file_name6)
dff7.to_excel(file_name7)

print('DataFrame is written to Excel File successfully.')