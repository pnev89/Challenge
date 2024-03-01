"""Build query."""
import pandas as pd
from datetime import timedelta


class BuildQuery:
    """Build query."""

    def run_query(
        self, incidents_table: pd.DataFrame, change_events_table: pd.DataFrame
    ):
        """Run query.

        Parameters
        ----------
        incidents_table : pd.DataFrame
            incidents table
        change_events_table : pd.DataFrame
            change events table

        Returns
        -------
        pd.Dataframe
            Aggregation results
        """
        time_interval = timedelta(minutes=60).total_seconds()

        # Perform the join
        merged_df = pd.merge(
            incidents_table,
            change_events_table,
            on=["account_id", "service_id"],
            suffixes=("_incident", "_change"),
        )

        # Filter the merged DataFrame based on the time condition 
        # triggered_at_timestamp_change in 
        # [triggered_at_timestamp_incident - 60 min ; triggered_at_timestamp_incident]
        filtered_df = merged_df[
            (
                merged_df["triggered_at_timestamp_change"]
                >= merged_df["triggered_at_timestamp_incident"]
                - timedelta(seconds=time_interval)
            )
            & (
                merged_df["triggered_at_timestamp_change"]
                < merged_df["triggered_at_timestamp_incident"]
            )
        ]

        # Group by incident and change titles, and count occurrences
        result_df = (
            filtered_df.groupby(["title_incident", "title_change"])
            .size()
            .reset_index(name="value")
        )

        # Construct the key column
        result_df["key"] = (
            "("
            + result_df["title_incident"]
            + "," + result_df["title_change"] + ")"
        )

        # Reorder the columns
        return result_df[["key", "value"]]
