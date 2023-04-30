import os
import pandas as pd

dataset_path = "./dataset"

csvs = sorted(os.listdir(dataset_path))
dataframes = []
for csv in csvs:
    file_path = os.path.join(dataset_path, csv)
    try:
        df = pd.read_csv(file_path, encoding='UTF-16LE', sep='\t')
    except Exception as e:
        print(f"Error reading file '{csv}': {e}")
        exit(1)
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

combined_df = combined_df.drop(combined_df.columns[0], axis=1)
combined_df = combined_df.rename(columns={combined_df.columns[8]: "Number Of Students"})
combined_df.to_csv('composite.csv', index=False)