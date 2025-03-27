
import os, sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import linregress
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESOURCES_DIR = os.path.join(parent_dir, 'resources')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
from utilities.tools import draw_heat_label

from utilities.dict_cat import get_dict
from utilities.file_path import path_to_file
from utilities.load_dataset import load_data
from data_analysis.box_plot import box_plot_analyse
from utilities.CONSTANTS import *

def regression_analyse(df:pd.DataFrame,to_show:bool, x_name:str,y_name:str):
    binary_features =[
        "Single",
        "Married",
        "Widower",
        "Divorced",
        "Facto union",
        "Legally separated",
        "Daytime/evening attendance",
        "Displaced",
        "Educational special needs",
        "Debtor",
        "Tuition fees up to date",
        "Gender",
        "Scholarship holder",
        "International",
    ]

    labels = {
        "Marital status_1": "Single",
        "Marital status_2": "Married",
        "Marital status_3": "Widower",
        "Marital status_4": "Divorced",
        "Marital status_5": "Facto union",
        "Marital status_6": "Legally separated",
    }
    if y_name in binary_features:
        logistic_b = True
    else:
        logistic_b= False

    if (x_name in binary_features or x_name in numeric_features
        and y_name in binary_features or y_name in numeric_features):
        data_selected = df
        data_encoded = pd.get_dummies(data_selected, columns=[
            "Marital status",
        ])
        data_encoded.rename(columns=labels, inplace=True)


        fig,ax_name = plt.subplots(figsize=(13, 13))

        sns.regplot(data=data_encoded,x=x_name,y=y_name,ax=ax_name,logistic=logistic_b) # Logistic true if Y is 0/1
        X_predictor = data_encoded[x_name]  # Zmienna niezależna (predyktor)
        y_response = data_encoded[y_name]  # Zmienna zależna (odpowiedź)
        X_predictor = sm.add_constant(X_predictor)
        if logistic_b:
            model = sm.Logit(y_response, X_predictor).fit()
        else:
            model = sm.OLS(y_response, X_predictor).fit()

        desc = model.summary().as_text()


        ax_name.set_title(f'{y_name} ~ {x_name}')
        if to_show:
            plt.show()
        else:
            plt.close()
    else:
        raise "Error"
    return [(desc, fig)]

def run_regression(df,to_show):
    tuples = [
        ("Age at enrollment","Curricular units 1st sem (grade)"),
        ("Curricular units 1st sem (approved)","Curricular units 1st sem (grade)"),
        ("Gender", "Curricular units 1st sem (grade)"),
        ("Age at enrollment", "Married" ),
        ("GDP","Curricular units 1st sem (grade)")

    ]
    lst = []
    for i, (t1, t2) in enumerate(tuples):
        regression_fig = regression_analyse(df, to_show, t1, t2)
        lst.extend(regression_fig)
    return lst
if __name__ == '__main__':
    path = path_to_file()
    df = load_data(path)
    run_regression(df,False)