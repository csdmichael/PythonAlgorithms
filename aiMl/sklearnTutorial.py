from sklearn import datasets

X = datasets.load_iris(as_frame=True)
df = X.frame
#print(df)
df.plot(kind='hist', y=['sepal length (cm)', 'sepal width (cm)'])
df.plot(kind='scatter', x='sepal length (cm)', y='sepal width (cm)')