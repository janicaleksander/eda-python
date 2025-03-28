import os
import pandas as pd

def load_data(path:str):
    if os.path.isfile(path):
        _, file_extension = os.path.splitext(path)
        if file_extension == ".csv":
            return pd.read_csv(path)
        elif file_extension == ".parquet":
            return pd.read_parquet(path)
        else:
            raise Exception("Wrong file type")
    else:
        raise Exception("Wrong path")

