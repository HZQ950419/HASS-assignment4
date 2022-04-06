import pandas as pd
import json

data_path = 'population2021.csv'
save_path = 'population2021.json'

def reader(data_path):
    df = pd.read_csv(data_path)
    pop_dict = {}
    pop_area_dict = {}
    pop_list = []
    for i in range(len(df['Subzone'])):
        pop_dict[df['Subzone'][i].upper()] = {'Population': df['Population'][i], 'Planning Area': df['Planning Area'][i]}
        if df['Population'][i] != '-':
            pop_list.append(int(df['Population'][i]))
    print("The minimal population is: {}\nThe maximal population is: {}".format(min(pop_list), max(pop_list)))
    for i in range(len(df['Planning Area'])):
        if df['Planning Area'][i] not in pop_area_dict:
            pop_area_dict[df['Planning Area'][i].upper()] = {'Population': [df['Population'][i]], 'Subzone': [df['Subzone'][i]]}
        else:
            pop_area_dict[df['Planning Area'][i].upper()]['Population'].append(df['Population'][i])
            pop_area_dict[df['Planning Area'][i].upper()]['Subzone'].append(df['Subzone'][i])
    pop_dict['area_dict'] = pop_area_dict

    return pop_dict

pop_dict = reader(data_path)
with open(save_path, 'w') as f:
    json.dump(pop_dict, f, indent=1)