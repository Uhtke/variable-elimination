"""
@Author Janneke Grooters
@Studentnumber s4739108
"""


class FactorTable:
    def __init__(self, name, dataframe):
        self.name = name
        self.dataframe = dataframe
        self.values = dataframe.values
        self.columns = dataframe.columns
        self.observed_column = None

    def locate_and_change_observed(self, observed_name, observed_value):
        print("\nBefore filtering observed:")
        print(self.dataframe)
        self.dataframe = self.dataframe[self.dataframe[observed_name] != observed_value]
        print("\nAfter filtering observed:")
        print(self.dataframe)
        print("\n")
