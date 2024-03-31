import pandas as pd

def load(path:str):
    df = pd.read_csv(path)
    data = df.to_string()

    return data