import os, sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.core.display_functions import display

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESOURCES_DIR = os.path.join(parent_dir, 'resources')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from utilities.dict_cat import get_dict
from utilities.file_path import path_to_file
from utilities.load_dataset import load_data
from data_analysis.box_plot import box_plot_analyse


def error_bars_analyse(df: pd.DataFrame, to_show: bool):
    features_to_plot = [
        "Curricular units 1st sem (grade)",
        "Curricular units 1st sem (approved)",
        "Application order",
        "Age at enrollment"
    ]
    df['Gender'] = df['Gender'].map({
        1:"Male",
        0:"Female"
    })

    plots_to_return = []
    plots_to_show = []

    # Gender X Grade
    fig_main_1, ax_single_1 = plt.subplots(1, 2, figsize=(10, 8))
    ax_main_1 = ax_single_1.flatten()

    fig1_1, ax1_1 = plt.subplots(figsize=(5, 8))
    sns.barplot(data=df, x="Gender", y=features_to_plot[0], errorbar="se", ax=ax1_1)
    sns.barplot(data=df, x="Gender", y=features_to_plot[0], errorbar="se", ax=ax_main_1[0])
    plots_to_return.append(fig1_1)
    plt.close(fig1_1)

    fig1_2, ax1_2 = plt.subplots(figsize=(5, 8))
    sns.barplot(data=df, x="Gender", y=features_to_plot[0], errorbar="sd", ax=ax1_2)
    sns.barplot(data=df, x="Gender", y=features_to_plot[0], errorbar="sd", ax=ax_main_1[1])
    plots_to_return.append(fig1_2)
    plt.close(fig1_2)

    plots_to_show.append(fig_main_1)

    # Gender X Approved

    fig_main_2, ax_single_2 = plt.subplots(1, 2, figsize=(10, 8))
    ax_main_2 = ax_single_2.flatten()

    fig2_1, ax2_1 = plt.subplots(figsize=(5, 8))
    sns.barplot(data=df, x="Gender", y=features_to_plot[1], errorbar="se", ax=ax2_1)
    sns.barplot(data=df, x="Gender", y=features_to_plot[1], errorbar="se", ax=ax_main_2[0])
    plots_to_return.append(fig2_1)
    plt.close(fig2_1)

    fig2_2, ax2_2 = plt.subplots(figsize=(5, 8))
    sns.barplot(data=df, x="Gender", y=features_to_plot[1], errorbar="sd", ax=ax2_2)
    sns.barplot(data=df, x="Gender", y=features_to_plot[1], errorbar="sd", ax=ax_main_2[1])
    plots_to_return.append(fig2_2)
    plt.close(fig2_2)

    plots_to_show.append(fig_main_2)

    #Gender x Application order
    fig_main_3, ax_single_3 = plt.subplots(1, 2, figsize=(10, 8))
    ax_main_3 = ax_single_3.flatten()

    fig3_1, ax3_1 = plt.subplots(figsize=(5, 8))
    sns.barplot(data=df, x="Gender", y=features_to_plot[2], errorbar="se", ax=ax3_1)
    sns.barplot(data=df, x="Gender", y=features_to_plot[2], errorbar="se", ax=ax_main_3[0])
    plots_to_return.append(fig3_1)
    plt.close(fig3_1)

    fig3_2, ax3_2 = plt.subplots(figsize=(5, 8))
    sns.barplot(data=df, x="Gender", y=features_to_plot[2], errorbar="sd", ax=ax3_2)
    sns.barplot(data=df, x="Gender", y=features_to_plot[2], errorbar="sd", ax=ax_main_3[1])
    plots_to_return.append(fig3_2)
    plt.close(fig3_2)

    plots_to_show.append(fig_main_3)

    fig_main_4, ax_single_4 = plt.subplots(1, 2, figsize=(10, 8))
    ax_main_4 = ax_single_4.flatten()

    fig4_1, ax4_1 = plt.subplots(figsize=(5, 8))
    sns.barplot(data=df, x="Gender", y=features_to_plot[3], errorbar="se", ax=ax4_1)
    sns.barplot(data=df, x="Gender", y=features_to_plot[3], errorbar="se", ax=ax_main_4[0])
    plots_to_return.append(fig3_1)
    plt.close(fig3_1)

    fig4_2, ax4_2 = plt.subplots(figsize=(5, 8))
    sns.barplot(data=df, x="Gender", y=features_to_plot[3], errorbar="sd", ax=ax4_2)
    sns.barplot(data=df, x="Gender", y=features_to_plot[3], errorbar="sd", ax=ax_main_4[1])
    plots_to_return.append(fig4_2)
    plt.close(fig4_2)

    plots_to_show.append(fig_main_4)



    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5, wspace=0.4)

    if to_show:
        for p in plots_to_show:
            p.show()
        plt.show()
    else:
        plt.close()

    df['Gender'] = df['Gender'].map({
        "Male":1,
        "Female":0,
    })
    return plots_to_return


if __name__ == '__main__':
    path = path_to_file()
    df = load_data(path)

    error_bars_analyse(df, True)