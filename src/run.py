#import utils.BuildQuery as BuildQuery
from utils._file_handling import FileHandling



fh = FileHandling()


# Reading incidents

incidents = fh.read_csv_file('../input_files/change_events.csv')

#/Users/pedroneves/Documents/GitHub/Challenge/input_files/incident_events.csv
#/Users/pedroneves/Documents/GitHub/Challenge/src/run.py




# Reading change events
change_events = fh.read_csv_file('../input_files/change_events.csv')

print(incidents)

# Querying 

# Writing results