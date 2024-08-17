
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Function to summarize text into 5 key words
def summarize_to_keywords(text, n=10):
    if pd.isna(text) or not text:
        return ""
    if not isinstance(text, str):
        text = str(text)
    vectorizer = TfidfVectorizer(stop_words='english', max_features=n)
    try:
        X = vectorizer.fit_transform([text])
        keywords = np.array(vectorizer.get_feature_names_out())
        if len(keywords) == 0:
            return ""
        sorted_indices = X.toarray().argsort()[0][-n:][::-1]
        return ' '.join(keywords[sorted_indices])
    except ValueError:
        return ""

# Load the Excel file
file_path = '/Users/callanhollenbach/Documents/AA Solve Hub Content/CARE Hack Data and code//CARE Hack - IP DATA.xlsx'  # Replace with your actual file path
excel_data = pd.ExcelFile(file_path)

# Load the data from the first sheet
data_sheet1 = pd.read_excel(file_path, sheet_name='Sheet1')

# Apply the function to each cell in the dataframe
summarized_data_sheet1 = data_sheet1.applymap(summarize_to_keywords)

# Save the summarized data to a CSV file
output_file_path = 'summarized_data.csv'
summarized_data_sheet1.to_csv(output_file_path, index=False)

print(f"Summarized data saved to {output_file_path}")