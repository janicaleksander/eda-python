import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utilities.tools import add_median_to_plot_by_cat, draw_marital_status

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESOURCES_DIR = os.path.join(parent_dir, 'resources')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from utilities.file_path import path_to_file
from utilities.load_dataset import load_data

def violin_plot_analyse(df: pd.DataFrame, to_show: bool):
    marital_status = [
            "Single",
            "Married",
            "Widower",
            "Divorced",
            "Facto union",
            "Legally separated",
    ]
    features_to_plot = [
        "Age at enrollment",
        "Curricular units 1st sem (grade)",
        "GDP"
    ]
# Gender x Grade
# Gender x approved
# Gedner x Application order
    plots = []

    for feature in features_to_plot:
        fig_single, ax_single = plt.subplots(figsize=(6, 5))
        sns.violinplot(data=df, x="Target", y=feature, ax=ax_single)
        ax_single.set_title(f"{feature} by Target")
        add_median_to_plot_by_cat(df, feature, "Target", ax_single)
        plots.append(fig_single)

    fig_single, ax_single = plt.subplots(figsize=(6, 5))
    sns.violinplot(data=df, x="Marital status", y="Age at enrollment", ax=ax_single)
    ax_single.set_title("Marital Status by Age at Enrollment")
    add_median_to_plot_by_cat(df, "Age at enrollment", "Marital status", ax=ax_single)
    draw_marital_status(ax_single, marital_status)
    plots.append(fig_single)

    plt.tight_layout()
    if to_show:
        for p in plots:
            p.show()
        plt.show()
    return plots


if __name__ == '__main__':
    path = path_to_file()
    df = load_data(path)
    violin_plot_analyse(df, True)
