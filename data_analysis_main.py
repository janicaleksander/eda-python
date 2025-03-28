# return : [files.csv] [images]
import os,sys,csv,json


from data_analysis.PCA import PCA_analyse
from data_analysis.heatmap import heatmap_analyse
from data_analysis.histograms import histogram_analyse
from data_analysis.regression import regression_analyse, run_regression
from data_analysis.violin_plot import violin_plot_analyse

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESOURCES_DIR = os.path.join(parent_dir, 'resources')
this_dir = os.path.dirname(__file__)

BOXPLOT_DIR = os.path.join(this_dir, 'generated_png/box_plot')
ERROR_DIR = os.path.join(this_dir, 'generated_png/error_bars')
HEATMAP_DIR = os.path.join(this_dir, 'generated_png/heatmap')
HISTOGRAM_DIR = os.path.join(this_dir, 'generated_png/histogram')
MODELSUM_DIR = os.path.join(this_dir, 'generated_png/model_summary')
PCA_DIR = os.path.join(this_dir, 'generated_png/pca')
REGRESSION_DIR = os.path.join(this_dir, 'generated_png/regression')
VIOLIN_DIR = os.path.join(this_dir, 'generated_png/violin_plot')
if parent_dir  or this_dir not in sys.path:
    sys.path.append(parent_dir)

from data_analysis.box_plot import box_plot_analyse
from data_analysis.error_bars import  *

def save_analysis(t_shw):
    path = path_to_file()
    df = load_data(path)


    box_plots_fig = box_plot_analyse(df, t_shw)
    for i,fig in enumerate(box_plots_fig):
        fig.savefig(os.path.join(BOXPLOT_DIR, f'wykres_box_{i}'),dpi=300)

    violin_plots_fig = violin_plot_analyse(df,t_shw)
    for i,fig in enumerate(violin_plots_fig):
        fig.savefig(os.path.join(VIOLIN_DIR, f'wykres_violin_{i}'),dpi=300)


    errors_bar_fig = error_bars_analyse(df,t_shw)
    for i,fig in enumerate(errors_bar_fig):
        fig.savefig(os.path.join(ERROR_DIR, f'wykres_error_{i}'),dpi=300)

    histograms_fig = histogram_analyse(df,t_shw)
    for i,fig in enumerate(histograms_fig):
        fig.savefig(os.path.join(HISTOGRAM_DIR, f'wykres_hist_{i}'),dpi=300)

    heatmap_fig = heatmap_analyse(df,t_shw)
    for i,fig in enumerate(heatmap_fig):
        fig.savefig(os.path.join(HEATMAP_DIR, f'wykres_heat_{i}'),dpi=300)


    regression_fig = run_regression(df,t_shw)
    for i, (desc, fig) in enumerate(regression_fig):
        fig.savefig(os.path.join(REGRESSION_DIR, f'regression_{i}'), dpi=300)
        name = os.path.join(MODELSUM_DIR, f'model_summary{i}.txt')
        with open(name, "w") as f:
            f.write(desc)

    PCA_fig = PCA_analyse(df,t_shw)
    for i,fig in enumerate(PCA_fig):
        fig.savefig(os.path.join(PCA_DIR, f'wykres_pca_{i}'),dpi=300)
if __name__ == '__main__':
    to_show = True
    save_analysis(to_show)