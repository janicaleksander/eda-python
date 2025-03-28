# return : [maybe other information] [images]
import os,sys,csv,json
import seaborn as sns
import matplotlib.pyplot as plt

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESOURCES_DIR = os.path.join(parent_dir, 'resources')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from utilities.dict_cat import get_dict
from utilities.file_path import path_to_file
from utilities.load_dataset import load_data
from utilities.CONSTANTS import *
def f_entry_data_analysis():
    path = path_to_file()
    df = load_data(path)
    calc_numeric_data(df)
    calc_category_data(df)
    show_proportions_data(df)


def calc_numeric_data(df):


    header = ["Numeric features"] + [label for label in numeric_features]
    mean_row = [ "MEAN" ]
    for v in numeric_features:
        mean_row.append(df[v].mean())
    median_row = [ "MEDIAN" ]
    for v in numeric_features:
        median_row.append(df[v].median())

    min_row = [ "MIN" ]
    for v in numeric_features:
        min_row.append(df[v].min())

    max_row = [ "MAX" ]
    for v in numeric_features:
        max_row.append(df[v].max())

    standard_row = [ "STANDARD_D" ]
    for v in numeric_features:
        standard_row.append(df[v].std())

    quantile_5_row = ["QUANTILE_5"]
    for v in numeric_features:
        quantile_5_row.append(df[v].quantile(0.05))

    quantile_95_row = ["QUANTILE_95"]
    for v in numeric_features:
        quantile_95_row.append(df[v].quantile(0.95))

    empty_row = ["EMPTY"]
    for v in numeric_features:
        empty_row.append(df[v].isnull().sum())
    rows = [mean_row,median_row,min_row,max_row,standard_row,quantile_5_row,quantile_95_row,empty_row]

    output_path = os.path.join(RESOURCES_DIR, "basic_information_num.csv")
    with open(output_path, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


def calc_category_data(df):

    header = ["Categorical features"] + [label for label in categorical_features]

    unique_row = ["Unique"]
    for v in categorical_features:
        unique_row.append(df[v].unique().sum())

    empty_row = ["Empty"]
    for v in categorical_features:
        empty_row.append(df[v].isnull().sum())
    rows = [unique_row,empty_row]

    output_path = os.path.join(RESOURCES_DIR, "basic_information_cat.csv")
    with open(output_path, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)




def show_proportions_data(df):
    json_mock = {}
    for v in categorical_features:
        dct = {'name': v}
        dct2 = df[v].value_counts(normalize=True).to_dict()
        dct3 = {}
        print("name from table:",v)
        helperd = get_dict(v)
        for k2,v2 in dct2.items():
            dct3[helperd[k2]]=v2
        dct.update(dct3)
        json_mock[v] = dct

    json_data = json.dumps(json_mock)
    output_path = os.path.join(RESOURCES_DIR, "cat_proportions.json")
    with open(output_path, 'w') as f:
        f.write(json_data)





if __name__ == '__main__':
    f_entry_data_analysis()