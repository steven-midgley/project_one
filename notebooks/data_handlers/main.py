import pandas as pd


class DataHandler:
    def __init__(self, df):
        self.df = df

    def normalize_time(self):
        """
        It may be best to create new columns containing the seconds-since-midnight.
        This will let us numerically evaluate the data. As well as create pandas
        datetimestamps for other evaluation methods
        """

        # if not isinstance(df, pd.DataFrame):
        #     raise TypeError(f"Parameter {df} is not type DataFrame")

        datetime_columns = []
        for col in self.df.columns:
            if pd.api.types.is_integer_dtype(self.df[col].columns):
                datetime_columns.append(self.df[col].columns)
            elif pd.api.types.is_datetime64_any_dtype(self.df[col].columns):
                datetime_columns.append(self.df[col].columns)

        return datetime_columns

        # if pd.api.types.is_datetime64_any_dtype(df[col]):

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
