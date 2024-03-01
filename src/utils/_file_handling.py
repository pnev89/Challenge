"""File Handling."""
from pathlib import Path
import pandas as pd


class FileHandling:
    """Handles Files."""

    def read_csv_file(self, path_to_file: str) -> pd.DataFrame:
        """Read csv files.

        Parameters
        ----------
        path_to_file : str
            path to file

        Returns
        -------
        pd.DataFrame
            File data
        """
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
        """Write csv files.

        Parameters
        ----------
        path_to_file : Path
            path to destination
        data : pd.DataFrame
            Dataframe to write
        """
        try:
            data.to_csv(path_to_file, index=False)
        except Exception as e:
            print(f"An error occurred while writing data to the CSV file: {e}")
