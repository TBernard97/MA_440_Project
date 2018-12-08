import pandas as pd
import numpy as np
import multiprocessing as mp
from multiprocessing import Pool


def search_match(id):
    with open('{}'.format('../Data/{}'.format(output_file)), mode='a+') as output:
        for index, row in api_frame.iterrows():
            if row.str.contains(id).any():
                row = pd.DataFrame(row).T
                row.to_csv(output, header=False)
                return row 




if __name__ == "__main__":
    try:
        uni_set = pd.read_csv('../Data/uni.csv')
        api_file = input('Enter API REQUEST set => ')
        input_file = input('Enter input file => ')
        output_file = input('Enter output file => ')

    except KeyboardInterrupt:
        pass

    input_frame = pd.read_csv('../Data/{}'.format(input_file))
    api_frame = pd.read_csv('../Data/{}'.format(api_file))
    with open('{}'.format('../Data/{}'.format(output_file)), mode='a+') as output:
        api_frame.head(0).to_csv(output)


    id_list = []
    for index, university in uni_set.iterrows():
        if input_frame['College'].str.contains(university['name']).any():
            id_list.append(university['id'])

    with Pool(4) as p:
        print(p.map(search_match, id_list))
