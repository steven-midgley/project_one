import pandas as pd
from datetime import datetime


class DataHandler:
    def __init__(self, df):
        self.df = df

    def determine_time_unit(self, timestamp="0"):
        timestamp = pd.to_numeric(timestamp, errors="coerce")
        # Assuming milliseconds
        dt_milli = pd.to_datetime(timestamp, unit="ms")
        dt_seconds = pd.to_datetime(timestamp, unit="s")
        dt_minutes = pd.to_datetime(timestamp, unit="m")

        # Current time
        is_now = datetime.now()

        match (dt_milli, dt_seconds, dt_minutes):
            case (dt, _, _) if pd.notna(dt) and dt <= is_now:
                return "milliseconds", dt_milli
            case (_, dt, _) if pd.notna(dt) and dt <= is_now:
                return "seconds", dt_seconds
            case (_, _, dt) if pd.notna(dt) and dt <= is_now:
                return "minutes", dt_minutes
            case _:
                return "Unknown format", None

    def normalize_time(self):
        """
        This will normalize time in two ways.
        It will create new columns for each time column with a human readable timestamp.
        it will also create new columns for minutes-since-minute.
        Purpose:
          I ( as human ) want to be able to see the dates of the events and having
          minutes-since-midnight will allow for better plotting and correlation tracking
        """

        # Identify cols with timestamps
        datetime_columns = []
        for col in self.df:
            if pd.api.types.is_numeric_dtype(self.df[col]) and "Time" in str(
                self.df[col]
            ):
                datetime_columns.append(col)
                DataHandler.determine_time_unit(self.df[col])
        print(datetime_columns)
        return datetime_columns

    # FOR TESTING!!
    def main():
        data_csv = pd.read_csv("data/arrivals.csv")
        df = pd.DataFrame(data_csv)
        dh = DataHandler(df)
        dh.normalize_time()


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
