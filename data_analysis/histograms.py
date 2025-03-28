import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESOURCES_DIR = os.path.join(parent_dir, 'resources')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from utilities.file_path import path_to_file
from utilities.load_dataset import load_data



def histogram_analyse(df:pd.DataFrame,to_show:bool):
    df['Gender'] = df['Gender'].map({
        1: "Male",
        0: "Female"
    })
    fig1 = sns.displot(data=df, x="Age at enrollment")
    fig2 = sns.displot(data=df, x="Age at enrollment",hue="Gender")
    fig3 = sns.displot(data=df, x="Age at enrollment", col="Gender")

    fig4 = sns.displot(data=df, x="Curricular units 1st sem (grade)")
    fig5 = sns.displot(data=df, x="Curricular units 1st sem (grade)",hue="Gender")
    fig6 = sns.displot(data=df, x="Curricular units 1st sem (grade)", col="Gender")

    fig7 = sns.displot(data=df, x="Curricular units 1st sem (enrolled)")
    fig8 = sns.displot(data=df, x="Curricular units 1st sem (enrolled)",hue="Gender")
    fig9 = sns.displot(data=df, x="Curricular units 1st sem (enrolled)", col="Gender")


    if to_show:
        plt.show()
    else:
        plt.close()
    df['Gender'] = df['Gender'].map({
        "Male": 1,
        "Female": 0,
    })
    return [fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8,fig9]

if __name__ == '__main__':
    path = path_to_file()
    df = load_data(path)
    histogram_analyse(df, True)