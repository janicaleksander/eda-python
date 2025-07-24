# Exploratory Data Analysis & Logistic Regression from Scratch

[](https://choosealicense.com/licenses/mit/)

This project provides a comprehensive Exploratory Data Analysis (EDA) using Python's data science stack (**Pandas**, **Seaborn**, and **Matplotlib**). It also features a from-scratch implementation of **multiclass logistic regression**, complete with performance enhancements.

-----

## ✨ Features

  * **Full EDA**: In-depth analysis with visualizations for numerical and categorical features.
  * **Custom Model**: Multiclass logistic regression implemented from scratch based on its underlying mathematical formulas.
  * **Performance Boost**: Techniques to improve the efficiency of the regression model.

-----



## 📂 Project Structure

```
.
├── data_analysis/          # Contains individual scripts for specific visualizations
│   ├── box_plot.py
│   └── ...
├── final_report.pdf        # Detailed report summarizing the project's findings and analysis.
├── data_analysis_main.py   # Main script to run the entire EDA pipeline
├── ablation_study.ipynb    # Notebook for conducting model ablation studies
├── linear_regression.ipynb   # Notebook for Linear Regression analysis
├── logistic_regression.ipynb # Notebook with the from-scratch Logistic Regression
├── requirements.txt        # Project dependencies
└── README.md
```

-----
## 🛠️ Installation

To get a local copy up and running, follow these steps.

1.  **Clone the repository:**

    ```bash
    git clone "https://github.com/janicaleksander/eda-python.git"
    cd repository-folder
    ```

2.  **Create and activate a virtual environment:**

      * On **macOS/Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
      * On **Windows**:
        ```powershell
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

-----

## 🚀 Usage

You can run the entire analysis pipeline or execute specific scripts individually.

### Run the Main Analysis

The main script `data_analysis_main.py` runs the complete workflow.

1.  To control whether plots are displayed on-screen, open `data_analysis_main.py` and set the `to_show` variable:

    ```python
    # Set to True to display plots, False to only save them as image files
    to_show = True 
    ```

2.  Execute the script from the root directory:

    ```bash
    python data_analysis_main.py
    ```

### Run a Specific Script

To run an individual analysis script (e.g., to generate only the heatmap), navigate to the `data_analysis` directory and run the desired file.

```bash
cd data_analysis
python your_script_name.py
```


## 📜 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.