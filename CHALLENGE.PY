import pandas as pd
from datetime import timedelta
from pandasql import sqldf

# Read change_events.csv and convert timestamps to datetime objects
change_events_df = pd.read_csv('./input_files/change_events.csv')
change_events_df['triggered_at_timestamp'] = pd.to_datetime(change_events_df['timestamp'])


# Read incident_events.csv and convert timestamps to datetime objects
incident_events_df = pd.read_csv('./input_files/incident_events.csv')
incident_events_df['triggered_at_timestamp'] = pd.to_datetime(incident_events_df['triggered_at'])


time_interval = timedelta(minutes=60).total_seconds()

query = f"""SELECT 
    '(' || incident_events_df.title || ',' || change_events_df.title || ')' as key,
    COUNT(*) AS value
             
FROM 
    incident_events_df
JOIN 
    change_events_df ON incident_events_df.account_id = change_events_df.account_id
    AND incident_events_df.service_id = change_events_df.service_id
WHERE 
    change_events_df.triggered_at_timestamp >= DATETIME(incident_events_df.triggered_at_timestamp, '-{time_interval} seconds')
        AND change_events_df.triggered_at_timestamp < incident_events_df.triggered_at_timestamp
GROUP BY 
    incident_events_df.title, change_events_df.title;
        """
incident_caused_by_change_df = sqldf(query)


print(incident_caused_by_change_df)

# Write the results to a new CSV file
#incident_caused_by_change_df.to_csv('incident_caused_by_change.csv', index=False)



