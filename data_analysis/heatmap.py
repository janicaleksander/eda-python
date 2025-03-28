
import os, sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESOURCES_DIR = os.path.join(parent_dir, 'resources')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from utilities.file_path import path_to_file
from utilities.load_dataset import load_data



def heatmap_analyse(df:pd.DataFrame, to_show:bool):
    selected_columns = [
        "Application order",
        "Age at enrollment",
        "Curricular units 1st sem (grade)",
        "Curricular units 2nd sem (grade)",
        "Curricular units 1st sem (credited)",
        "Curricular units 2nd sem (credited)",
        "Unemployment rate",
        "GDP",
        "Inflation rate",
        "Daytime/evening attendance",
        "Displaced",
        "Educational special needs",
        "Debtor",
        "Tuition fees up to date",
        "Gender",
        "Scholarship holder",
        "International",
        "Marital status",
        "Target"
    ]
    labels = {
        "Marital status_1"  :"Single",
        "Marital status_2" :"Married",
        "Marital status_3":"Widower",
        "Marital status_4" :"Divorced",
        "Marital status_5" :"Facto union",
        "Marital status_6" :"Legally separated",
        "Target_1" :"Dropout",
        "Target_2" :"Graduate",
        "Target_3" :"Enrolled",
        "Daytime/evening attendance_0":"Evening attendance",
        "Daytime/evening attendance_1":"Daytime attendance",
    }

    data_selected = df[selected_columns]
    data_selected.loc[:, "Target"] = data_selected["Target"].map({
        "Dropout": 1,
        "Graduate": 2,
        "Enrolled": 3
    })

    data_encoded = pd.get_dummies(data_selected,columns=[
        "Marital status",
        "Target",
        "Daytime/evening attendance",
    ])
    data_encoded.rename(columns=labels, inplace=True)


    fig,ax = plt.subplots(figsize=(15, 15))
    sns.heatmap(data_encoded.corr(),cmap = sns.color_palette("hls", 8), vmin=-1, vmax=1, center=0, fmt=".2f", square=True, linewidths=.5,ax=ax)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.41)

    if to_show:
        plt.show()
    else:
        plt.close()
    return [fig]


if __name__ == '__main__':
    path = path_to_file()
    df = load_data(path)
    heatmap_analyse(df, True)