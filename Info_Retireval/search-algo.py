import pandas as  pd 
import csv

df = pd.read_csv('../Data/uni.csv')

comparison_file = input('Enter comparison file => ')
output_file = input('Enter output file => ')
data = input('Enter university list => ')


dflist = pd.read_csv('../Data/{}'.format(data))
comparison_frame = pd.read_csv('../Data/{}'.format(comparison_file))

unilist = []

for index, college in dflist.iterrows(): 
   college  =  college['College']
   unilist.append(college)


id_list = []

for college in unilist:
   for index, name in df.iterrows():
     if name.str.contains(college).any():
         id_list.append(name['id'])

with open('../Data/{}'.format(output_file), mode='a+') as output:
    comparison_frame.head(0).to_csv(output)
    for id in id_list:
        for index, row in comparison_frame.iterrows():
           if row.str.contains(id).any():
               row = pd.DataFrame(row).T
               row.to_csv(output, header=False)
                
       
             
