import sys,os



parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESOURCES_DIR = os.path.join(parent_dir, 'resources')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)



def add_median_to_plot_by_cat(df,feature,group,ax):
    medians = df.groupby(group)[feature].median()
    categories = df[group].unique()
    for j, category in enumerate(categories):
        median_value = medians[category]
        draw_median(j, ax, median_value)
    ax.set_title(f"{feature} by Target",fontsize=7)

def draw_median(j,ax,median_value):
    ax.text(j, median_value + 1, f'{median_value:.1f}',
            horizontalalignment='center', color='black', weight='bold')



def draw_marital_status(ax,marital_status):
    ax.set_xticks(range(len(marital_status)))  # Określamy, gdzie mają być umieszczone etykiety
    ax.set_xticklabels(marital_status, rotation=45,fontsize=7)
    ax.set_title("Marital status by Target")


def draw_heat_label(ax,labels):
    ax.set_xticks(range(len(labels)))  # Określamy, gdzie mają być umieszczone etykiety
    ax.set_xticklabels(labels, rotation=45,fontsize=7)
    ax.set_title("Marital status by Target")



