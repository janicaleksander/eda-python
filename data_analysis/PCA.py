import os, sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESOURCES_DIR = os.path.join(parent_dir, 'resources')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from utilities.file_path import path_to_file
from utilities.load_dataset import load_data
from utilities.CONSTANTS import *


def PCA_analyse(df: pd.DataFrame, to_show: bool):
    selected_data = numeric_features + [
        "Displaced",
        "Educational special needs",
        "Debtor",
        "Tuition fees up to date",
        "Gender",
        "Scholarship holder",
        "International",
        "Marital status"
    ]

    data_selected = df[selected_data]
    labels = {
        "Marital status_1": "Single",
        "Marital status_2": "Married",
        "Marital status_3": "Widower",
        "Marital status_4": "Divorced",
        "Marital status_5": "Facto union",
        "Marital status_6": "Legally separated",
    }
    data_encoded = pd.get_dummies(data_selected, columns=["Marital status"])
    data_encoded.rename(columns=labels, inplace=True)

    feature_names = list(data_encoded.columns)

    x = data_encoded.values
    x = StandardScaler().fit_transform(x)
    pca = PCA(n_components=2)

    principal_components = pca.fit_transform(x)

    principal_df = pd.DataFrame(data=principal_components,
                               columns=['principal component 1', 'principal component 2'])

    final_df = pd.concat([principal_df, df[['Target']]], axis=1)

    plt.figure(figsize=(12, 10))

    ax1 = plt.subplot(1, 1, 1)

    ax1.set_xlabel('Principal Component 1', fontsize=15)
    ax1.set_ylabel('Principal Component 2', fontsize=15)
    ax1.set_title('2 component PCA with Loadings', fontsize=20)

    targets = df['Target'].unique()
    colors = ['r', 'g', 'b']

    for target, color in zip(targets, colors):
        indicesToKeep = final_df['Target'] == target
        ax1.scatter(final_df.loc[indicesToKeep, 'principal component 1'],
                    final_df.loc[indicesToKeep, 'principal component 2'],
                    c=color, s=50, alpha=0.6)

    ax1.legend(targets)
    ax1.grid()
    fig1 = plt.gcf()

    # Get the loadings
    loadings = pca.components_.T * np.sqrt(pca.explained_variance_)


    scaling = 5

    for i, (x, y) in enumerate(loadings[:, 0:2]):
        ax1.arrow(0, 0, scaling * x, scaling * y, color='k', alpha=0.5,
                  head_width=0.1, head_length=0.2)
        ax1.text(scaling * x * 1.15, scaling * y * 1.15, feature_names[i],
                 color='k', ha='center', va='center', fontsize=8)

    circle = plt.Circle((0, 0), radius=scaling, fill=False, color='gray', linestyle='--')
    ax1.add_patch(circle)

    plt.figure(figsize=(10, 8))
    ax2 = plt.subplot(1, 1, 1)
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_xlabel('PC1 Loadings', fontsize=15)
    ax2.set_ylabel('PC2 Loadings', fontsize=15)
    ax2.set_title('PCA Loadings Biplot', fontsize=20)
    fig2 = plt.gcf()

    loadings_norm = loadings.copy()
    for i in range(2):
        loadings_norm[:, i] = loadings[:, i] / np.sqrt(pca.explained_variance_[i])

    for i, (x, y) in enumerate(loadings_norm[:, 0:2]):
        ax2.arrow(0, 0, x, y, color='r', alpha=0.5, head_width=0.05, head_length=0.1)
        ax2.text(x * 1.15, y * 1.15, feature_names[i],
                 color='r', ha='center', va='center', fontsize=10)


   # print('Explained variance ratio of the 2 principal components:')
   # print(pca.explained_variance_ratio_)

    if to_show:
        plt.tight_layout()
        plt.show()

    else:
        plt.close()
    loadings_df = pd.DataFrame(loadings[:, 0:2],
                               index=feature_names,
                               columns=['PC1', 'PC2'])
 #   print(loadings_df.sort_values('PC1',ascending=False))
    return [fig1,fig2]


if __name__ == '__main__':
    path = path_to_file()
    df = load_data(path)
    PCA_analyse(df, True)

