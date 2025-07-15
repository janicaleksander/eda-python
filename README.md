# Exploratory Data Analysis (EDA) with Python

This project demonstrates a full-cycle data science workflow — from in-depth exploratory data analysis (EDA) to implementing multiclass logistic regression **from scratch**, followed by **efficiency boosting techniques** and the construction of **Mixture of Experts** models.

The codebase not only illustrates strong fundamentals in data analysis and statistical modeling, but also emphasizes **clean code**, **modular design**, and **visual interpretability**, making it a strong demonstration of real-world applied machine learning.

---

##  Project Highlights

- Exploratory Data Analysis using Seaborn & Matplotlib
- Multiclass Logistic Regression implemented manually (no `scikit-learn`)
- Model efficiency boosting strategies
- Building and training a Mixture of Experts model
- Configurable visualization output (save or show plots)
- Focus on readability and extensibility for research or production

---
## Requirements
- Python >= 3.12
- Git

## Installation
Clone the repository:
```bash
git clone "repository link"
cd repository-folder
```

### On Linux/macOS:
Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv_name
source venv_name/bin/activate
```

### On Windows:
Create and activate a virtual environment:
```powershell
python -m venv venv_name
venv_name\Scripts\activate
```

Install dependencies:
```bash
pip install --no-cache-dir -r requirements.txt
```

## Usage
Run the main analysis script. In this script, you can configure whether you want to only generate and save images or also display the generated visualizations.

If you want to display generated visualizations, modify `data_analysis_main.py`:
```python
to_show = True
```
Then run:
```bash
python data_analysis_main.py
```

If you want to run specific script e.g only for heatmap 
you have to:
```bash
cd data_analysis
python "script_name"
```
If you have problem with showing  plots you have to install python3-tkinter (especially when you are working on Linux)
## Libraries Used
- Pandas
- Seaborn
- Matplotlib

## License
This project is licensed under the MIT License.

