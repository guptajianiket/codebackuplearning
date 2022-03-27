import pandas as pd
data1 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP1.csv')
data2 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP2.csv')
data3 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP5.csv')
data4 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP6.csv')
data5 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP7.csv')
data6 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP8.csv')
data7 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\TKKS-EP9.csv')

# creating data frame based on q1 answer column from the detailed report
df1 = pd.DataFrame(data1, columns=['Q1 Answer'])
df2 = pd.DataFrame(data2, columns=['Q1 Answer'])
df3 = pd.DataFrame(data3, columns=['Q1 Answer'])
df4 = pd.DataFrame(data4, columns=['Q1 Answer'])
df5 = pd.DataFrame(data5, columns=['Q1 Answer'])
df6 = pd.DataFrame(data6, columns=['Q1 Answer'])
df7 = pd.DataFrame(data7, columns=['Q1 Answer'])

df1['Q1 Answer'] = df1['Q1 Answer'].replace(['A'],'Bharti')

count1 = df1['Q1 Answer'].value_counts()
print(df1)