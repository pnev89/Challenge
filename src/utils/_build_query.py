import pandas as pd
from datetime import timedelta
from pandasql import sqldf

class BuildQuery:
    
    def build_query(self, incidents_table: pd.DataFrame, change_events_table: pd.DataFrame):

        time_interval = timedelta(minutes=60).total_seconds()

        self.query = f"""SELECT 
                    '(' || {incidents_table}.title || ',' || {change_events_table}.title || ')' as key,
                    COUNT(*) AS value
                            
                FROM 
                    {incidents_table}
                JOIN 
                    {change_events_table} ON {incidents_table}.account_id = {change_events_table}.account_id
                    AND {incidents_table}.service_id = {change_events_table}.service_id
                WHERE 
                    {change_events_table}.triggered_at_timestamp >= DATETIME({incidents_table}.triggered_at_timestamp, '-{time_interval} seconds')
                        AND {change_events_table}.triggered_at_timestamp < {incidents_table}.triggered_at_timestamp
                GROUP BY 
                    {incidents_table}.title, {change_events_table}.title;
                        """
    
    
    def run_query(self) -> pd.DataFrame:

        try:
            return sqldf(self.query)

        except Exception as e:

            print("An error occurred:", e)
        
    def print_query(self):
        print(self.query)

