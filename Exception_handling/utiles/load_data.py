import pandas as pd
import json

def load_data(files):
    base_path = "Files/"
    all_data = []

    for file in files:
        with open(base_path + file, "r", encoding="utf-8") as f:
            data = json.load(f)
        all_data.append(data)

    return pd.DataFrame(all_data)
