#Plotting Zika Virus Cases
#v.1 2020/2/5
#Armani Chien

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

#Understanding the csv file contents
df=pd.read_csv('Zika Cases.csv')
dfDesc = df.describe()
##print(df.info())

#For the second part *Countries Catplot*
df1 = df[['FDF','Country / territory', 'Cases']] #Cutting off rows
df1 = df1[1:].reset_index()
df1 = df1.loc[:,['FDF','Country / territory', 'Cases']] #Cutting off columns
df1.columns = ['FDF','Country_territory', 'Cases'] #Cleaning names
df1 = df1.sort_values(by="Country_territory")
##print(df1.head(2))
##print(df1.info())
#Checking if the csv file has any null values, structure type
'''print(df.columns.values)
print(df.info()) #Check data structure eg. Float
print(df.tail(5))
print(df.isnull().sum())
'''
#Extracting Critical Information for data visualisation
dfCritInfo = df[['EPI Week (outbreak)','Cases']]
dfCritInfo = dfCritInfo[1:]
##print(dfCritInfo)
##print(dfCritInfo.index)

#Changing structure type of the cases values, column names
dfCritInfo['Cases'] = dfCritInfo['Cases'].astype(int)
dfCritInfo['EPI Week (outbreak)'] = dfCritInfo['EPI Week (outbreak)'].astype(int)
dfCritInfo.columns = ['EPI_Week_outbreak','Cases']
##print(dfCritInfo.info()) #Check if structure type has changed
#Grouping Similar EPI Weeks and adding cases that happened in the same week
dfCritInfoGroup = dfCritInfo.groupby("EPI_Week_outbreak", as_index = False).aggregate('sum')

##print(dfCritInfoGroup)
##export_csv = dfCritInfoGroup.to_csv ('Zika_Graph_CritInfoGroup.csv', index = True, header = True)

##print(dfCritInfo.columns.values())
##print(dfCritInfo.info())
#Giving back dataframe index because groupby deletes it



##ax.figure.savefig('AscendingCaseCountToWeeks.png')


#Changing the structure type of df
df1['Cases'] = df1['Cases'].astype(int)
df1['FDF'] = df1['FDF'].astype(str)
df1['Country_territory'] = df1['Country_territory'].astype(str)
print(df1.head(5))
print(df1.info())
#plotting countries vs. cases
g = sns.catplot(x='Country_territory', y='Cases', hue='FDF', data=df1,
                kind='bar')
plt.show()
#g.savefig('CountriesToCasesConfirmed_Suspected_Dead.png')

print(df1.head(5))
#Printing out the line graph
f, axes = plt.subplots(2, 1)
sns.barplot(x='EPI_Week_outbreak',
            y='Cases',
            data=dfCritInfoGroup,
            ax = axes[0])
sns.barplot(x='Country_territory',
            y='Cases',
            data=df1,
            ax = axes[1])
plt.title("Cases relative to time progression in weeks")
plt.show()
