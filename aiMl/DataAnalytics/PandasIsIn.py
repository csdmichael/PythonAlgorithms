import pandas as pd
df = pd.DataFrame({'minutes': [30, 35, 40],
                  'points': [13, 21, 50],
                  'team': ['knicks', 'lakers', 'knicks']},
                 index = ['drose', 'lebron', 'kemba'])
#print(df)
print(df.isin({'team': ['knicks']}))

over20 = df.query('points > 20')
print(over20)