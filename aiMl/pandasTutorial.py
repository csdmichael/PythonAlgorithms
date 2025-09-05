import pandas as pd

data = {'A': [25,56,93], 'B': ['str1', 'str2', 'str3']}

'''
df = pd.DataFrame(data)
print(df)


df = df.set_index('A')
print(df)

df = pd.DataFrame(data, index=['row1', 'row2', 'row3'])
print(df)

fileName = 'aiMl\data\celebrity-heights.csv'
dfFile = pd.read_csv(fileName)

print(dfFile)

dfFileFullName = dfFile.set_index('fullname')
print(dfFileFullName)

# Url: 'https://data.ca.gov/dataset/educational-attainment/resource/6b0251cf-1512-4d01-a6bd-0d2cf146ffb3'

url = 'https://data.chhs.ca.gov/dataset/91f51139-e3e2-4cbe-ae7d-fe15b01b86f4/resource/ad8277be-9e97-4904-9954-006ba8e35dd8/download/hci_educational_attainment_355_ca_re_co_cd_pl_ct_total2018-06-12-ada_bh.csv'
dfFileUrl = pd.read_csv(url)
print(dfFileUrl.info())
'''

fileName = 'aiMl\data\celebrity-heights.csv'
dfFile = pd.read_csv(fileName)

#print(dfFile)
#print(dfFile.info())
#print(dfFile.describe())
print(dfFile.head())
print(dfFile.tail(10))