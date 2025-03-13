import pandas as pd
import re

def clean_text(text):
    """Preprocess text by removing special characters, lowering case, and stripping spaces."""
    return re.sub(r"[^a-zA-Z0-9\s]", "", text.lower().strip()) if isinstance(text, str) else ""

def load_and_clean_data(file_path):
    """Loads dataset, removes duplicates, and cleans text fields."""
    df = pd.read_csv(file_path)
    df.drop_duplicates(inplace=True)
    df["resume_text"] = df["resume_text"].apply(clean_text)
    df["job_description"] = df["job_description"].apply(clean_text)
    return df

if __name__ == "__main__":
    df = load_and_clean_data("dataset/resumes.csv")
    print(df.head())
