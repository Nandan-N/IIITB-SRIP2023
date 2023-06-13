import pandas as pd
from googletrans import Translator

def transliterate_excel(input_file, output_file):
    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(input_file)

    # Initialize the translator
    translator = Translator()

    # Transliterate the text in all columns
    for column in df.columns:
        df[column] = df[column].apply(lambda x: translator.translate(x, src='en', dest='en').text)

    # Save the translated DataFrame to a new Excel file
    df.to_excel(output_file, index=False)

    print("Translation complete. Translated file saved as:", output_file)

# Usage example
input_file = 'path_to_input_excel_file.xlsx'
output_file = 'path_to_save_translated_excel_file.xlsx'

transliterate_excel(input_file, output_file)
