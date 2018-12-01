import pandas as  pd 

df = pd.read_csv('../Data/uni.csv')


list = input('Enter university list => ')
dflist = pd.read_csv('../Data/{}'.format(list))

unilist = []

for index, college in dflist.iterrows(): 
   college  =  college['College']
   unilist.append(college)


results = []

for college in unilist:
   for index, name in df.iterrows():
      if college in name['name']:
       results.append(name['id'])

print(results)