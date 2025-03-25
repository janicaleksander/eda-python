# return : [files.csv] [images]
import os,sys,csv,json

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from data_analysis.PCA import PCA_analyse
from data_analysis.heatmap import heatmap_analyse
from data_analysis.histograms import histogram_analyse
from data_analysis.regression import regression_analyse
from data_analysis.violin_plot import violin_plot_analyse

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESOURCES_DIR = os.path.join(parent_dir, 'resources')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from utilities.dict_cat import get_dict
from utilities.file_path import path_to_file
from utilities.load_dataset import load_data
from data_analysis.box_plot import box_plot_analyse
from data_analysis.error_bars import  *

def save_analysis():
    path = path_to_file()
    df = load_data(path)
    box_plots_fig = box_plot_analyse(df, True)
    for i,fig in enumerate(box_plots_fig):
        fig.savefig(f'wykres_box_{i}',dpi=300)

    violin_plots_fig = violin_plot_analyse(df,True)
    for i,fig in enumerate(violin_plots_fig):
        fig.savefig(f'wykres_violin_{i}',dpi=300)


    errors_bar_fig = error_bars_analyse(df,True)
    for i,fig in enumerate(errors_bar_fig):
        fig.savefig(f'wykres_error_{i}',dpi=300)

    histograms_fig = histogram_analyse(df,True)
    for i,fig in enumerate(histograms_fig):
        fig.savefig(f'wykres_hist_{i}',dpi=300)

    heatmap_fig = heatmap_analyse(df,True)
    for i,fig in enumerate(heatmap_fig):
        fig.savefig(f'wykres_heat_{i}',dpi=300)

#poprawić to zeby to wybieranie bylo jednak w srkypice regression
    tuples = [
        ("Age at enrollment","Curricular units 1st sem (grade)"),
        ("Curricular units 1st sem (approved)","Curricular units 1st sem (grade)"),
        ("Gender", "Curricular units 1st sem (grade)"),
        ("Age at enrollment", "Married" ),
        ("GDP","Curricular units 1st sem (grade)")

    ]
    for j, (t1, t2) in enumerate(tuples):
        regression_fig = regression_analyse(df, True, t1, t2)
        for i, pack in enumerate(regression_fig):
            pack[1].savefig(f'regression_{j}_{i}', dpi=300)
            name = f'model_summary{j}_{i}.txt'  # Usunięcie zbędnych cudzysłowów
            with open(name, "w") as f:
                f.write(pack[0])

    PCA_fig = PCA_analyse(df,True)
    for i,fig in enumerate(PCA_fig):
        fig.savefig(f'wykres_PCA_{i}',dpi=600)
if __name__ == '__main__':
    save_analysis()