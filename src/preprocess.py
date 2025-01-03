import pandas as pd
from sklearn.preprocessing import LabelEncoder
import requests

# Data preprocessing
def preprocess(input_file, output_file):
    data = pd.read_excel(input_file, sheet_name=0)
    data.columns = data.columns.str.lower()

    # Select relevant variables to use for the analysis
    columns_to_extract = ['cell_line_name', 'drug_name', 'putative_target', 'ln_ic50', 'auc', 'z_score']
    selected_data = data[columns_to_extract]
    # Filter outliers and NA values
    filtered_data = selected_data[
        (data['auc'] >= 0.2) & (data['auc'] <= 0.8) &
        (data['z_score'] >= -2) & (data['z_score'] <= 2)
    ]
    filtered_data = filtered_data.drop(columns=['auc', 'z_score'])
    filtered_data = filtered_data.dropna()

    # Encode categorical variables
    cell_line_encoder = LabelEncoder()
    drug_encoder = LabelEncoder()
    filtered_data['cell_line_encoded'] = cell_line_encoder.fit_transform(filtered_data['cell_line_name'])
    filtered_data['drug_encoded'] = drug_encoder.fit_transform(filtered_data['drug_name'])

    # Save the processed data and encoders
    filtered_data.to_csv("data/GDSC2_processed.csv", index=False)
    cell_line_encoder.classes_.tofile("data/cell_line_classes.txt", sep="\n")
    drug_encoder.classes_.tofile("data/drug_classes.txt", sep="\n")
    print(f"Processed data saved to {output_file}")



if __name__ == "__main__":
    preprocess("data/GDSC2_raw.xlsx", "data/GDSC2_processed.csv")