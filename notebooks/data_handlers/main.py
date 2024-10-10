import pandas as pd
from datetime import datetime


class DataHandler:
    def __init__(self, df):
        self.df = df

    def identify_time_columns(self):
        # Identify cols with timestamps
        datetime_columns = []
        for col in self.df:
            if pd.api.types.is_numeric_dtype(self.df[col]) and "Time" in str(
                self.df[col]
            ):
                datetime_columns.append(col)
        return datetime_columns

    def normalize_time(self, timestamp):
        """
        This will normalize time in two ways.
        1. It will create new columns for each time column with a human readable timestamp.
        2. it will also create new columns for minutes-since-minute.
          columns = datetime_cols (used to insert new column in correct location)
        """
        timestamp = pd.to_numeric(timestamp, downcast="integer")

        dt_seconds = pd.to_datetime(timestamp, unit="s", errors="coerce")
        dt_minutes = pd.to_datetime(timestamp, unit="m", errors="coerce")

        # Current time for comparison
        now = datetime.now()

        # Store the best guess results
        human_readable = []
        minutes_since_midnight = []

        # Iterate over the Series row by row
        for i in range(len(timestamp)):
            seconds_value = dt_seconds.iloc[i]
            minutes_value = dt_minutes.iloc[i]

            # Apply logic to choose the correct format based on what is plausible
            if pd.notna(seconds_value) and seconds_value <= now:
                human_readable.append(seconds_value)
                minutes_since_midnight.append(
                    seconds_value.hour * 60 + seconds_value.minute
                )
            elif pd.notna(minutes_value) and minutes_value <= now:
                human_readable.append(minutes_value)
                minutes_since_midnight.append(
                    minutes_value.hour * 60 + minutes_value.minute
                )
            else:
                human_readable.append(pd.NaT)
                minutes_since_midnight.append(None)

        # insert new columns
        self.df["readable"] = human_readable
        self.df["minutes_since_midnight"] = minutes_since_midnight

    # FOR TESTING!!
    def main():
        data_csv = pd.read_csv("data/arrivals.csv")
        df = pd.DataFrame(data_csv)
        dh = DataHandler(df)
        time_cols = dh.identify_time_columns()
        for index, tc in enumerate(time_cols):
            dh.normalize_time(df[f"{tc}"])
            print(index)
        print(df.sample(n=5))


if __name__ == "__main__":
    DataHandler.main()

    # # clean & normalize time columns
    # df.dep_time = df.dep_time.astype(int)  # whole int for minutes
    # df.dep_time = df.dep_time.astype(str).str.zfill(
    #     4
    # )  # zfill(4) is to ensure that all timestamps have 4 digits

    # df.sched_dep_time = df.sched_dep_time.astype(str).str.zfill(4)

    # df.dep_delay = df.dep_delay.astype(int)

    # df.arr_time = df.arr_time.astype(int)
    # df.arr_time = df.arr_time.astype(str).str.zfill(4)

    # df.sched_arr_time = df.sched_arr_time.astype(str).str.zfill(4)

    # df.arr_delay = df.arr_delay.astype(int)

    # df.air_time = df.air_time.astype(int)

    # # Convert columns to datetime
    # df.dep_time = pd.to_datetime(df.dep_time, format="%H%M%S").dt.strftime(
    #     "%H:%M:%S"
    # )

    # df.sched_dep_time = pd.to_datetime(
    #     df.sched_dep_time, format="%H%M%S"
    # ).dt.strftime("%H:%M:%S")

    # df.arr_time = pd.to_datetime(df.arr_time, format="%H%M%S").dt.strftime(
    #     "%H:%M:%S"
    # )
    # df.sched_arr_time = pd.to_datetime(
    #     df.sched_arr_time, format="%H%M%S"
    # ).dt.strftime("%H:%M:%S")

    # # Create minutes columns
    # df.insert(
    #     4,
    #     "dt_min",
    #     pd.to_datetime(df.dep_time).dt.hour * 60
    #     + pd.to_datetime(df.dep_time).dt.minute,
    # )  # this is to keep the original str formate in the df.dep_time column

    # df.insert(
    #     6,
    #     "sdt_min",
    #     pd.to_datetime(df.sched_dep_time).dt.hour * 60
    #     + pd.to_datetime(df.sched_dep_time).dt.minute,
    # )

    # df.insert(
    #     8,
    #     "rt_min",
    #     pd.to_datetime(df.arr_time).dt.hour * 60
    #     + pd.to_datetime(df.arr_time).dt.minute,
    # )  # this is to keep the original str formate in the df.dep_time column

    # df.insert(
    #     10,
    #     "srt_min",
    #     pd.to_datetime(df.sched_arr_time).dt.hour * 60
    #     + pd.to_datetime(df.sched_arr_time).dt.minute,
    # )
