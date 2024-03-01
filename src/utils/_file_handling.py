"""File Handling."""
from pathlib import Path
import pandas as pd

class FileHandling:
    """Handles Files."""

    def read_csv_file(self, path_to_file: str) -> pd.DataFrame:
    
        try:
            return pd.read_csv(path_to_file)
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except pd.errors.EmptyDataError:
            print("The file is empty.")
        except pd.errors.ParserError:
            print("There was an error parsing the file.")
        except Exception as e:
            print("An error occurred:", e)

    def write_file(self, path_to_file: Path, data: pd.DataFrame):

        try:
            data.to_csv(path_to_file, index=False)
        except Exception as e:
            print(f"An error occurred while writing data to the CSV file: {e}")


