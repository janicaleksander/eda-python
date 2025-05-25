# Exploratory Data Analysis (EDA) with Python

This project demonstrates a basic exploratory data analysis (EDA) approach using Python tools such as Seaborn and Matplotlib. It covers data loading, calculating statistics, and visualizing numerical and categorical features.
Also, here it is implemented multiclass logistic regression from scratch.
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

