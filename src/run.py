"""Run all."""
from utils._file_handling import FileHandling
from src.utils._build_query import BuildQuery
import pandas as pd

fh = FileHandling()

# Reading incidents
incidents = fh.read_csv_file('input_files/incident_events.csv')
incidents['triggered_at_timestamp'] = pd.to_datetime(incidents['triggered_at'])

# Reading change events∏
change_events = fh.read_csv_file('input_files/change_events.csv')
change_events['triggered_at_timestamp'] = (
    pd.to_datetime(change_events['timestamp']))
change_events['title'] = change_events['title'].str.replace('\n', '')

# Building the query
bq = BuildQuery()
results = bq.run_query(incidents_table=incidents,
                       change_events_table=change_events)

# Writing results
fh.write_file("output_files/results.csv", results)
