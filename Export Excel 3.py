import pandas as pd
#Reading the CSV/excel report
data1 = pd.read_csv (r'C:\Users\aniket.gupta\Downloads\grouptask.csv')


# creating data frame based on submitted answer column from the detailed report
df1 = pd.DataFrame(data1, columns=['Q1 Answer'])


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

replacetext(df1,"Option A", "Option B")

count1=pd.DataFrame(df1['Q1 Answer'].value_counts())

dftotal1=pd.DataFrame({'Q1 Answer':{'Total': len(df1)}})


df1=pd.concat([count1,dftotal1],ignore_index=False,axis=0)


print("Group Task",df1)


file_name1='Meet_Naagin_6_Char_episode21_Data.xlsx'
file_name2='Meet_Naagin_6_Char_episode22_Data.xlsx'
file_name3='Meet_Naagin_6_Char_episode23_Data.xlsx'
file_name4='Meet_Naagin_6_Char_episode24_Data.xlsx'
file_name5='TKKS_episode20_Data.xlsx'
file_name6='TKKS_episode21_Data.xlsx'
file_name7='TKKS_episode22_Data.xlsx'
file_name8='TKKS_episode23_Data.xlsx'
file_name9='TKKS_episode24_Data.xlsx'
file_name10='TKKS_episode25_Data.xlsx'
file_name11='TKKS_episode26_Data.xlsx'
file_name12='TKKS_episode27_Data.xlsx'
file_name13='TKKS_episode29_Data.xlsx'
file_name14='TKKS_episode30_Data.xlsx'
file_name15='TKKS_episode31_Data.xlsx'
file_name16='TKKS_episode32_Data.xlsx'
file_name17='TKKS_episode33_Data.xlsx'
file_name18='TKKS_episode34_Data.xlsx'
file_name19='TKKS_episode35_Data.xlsx'
file_name20='TKKS_episode36_Data.xlsx'
file_name21='TKKS_episode37_Data.xlsx'
file_name22='TKKS_episode38_Data.xlsx'
file_name23='TKKS_episode39_Data.xlsx'
file_name24='TKKS_episode40_Data.xlsx'
df1.to_excel(file_name1)