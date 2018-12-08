"""
@Author Janneke Grooters
@Studentnumber s4739108
"""


from factor_table import FactorTable
from typing import Dict


class FactorIdentifier:

    def __init__(self, nodes: list, probabilities: dict, observed: dict):
        """
        Initialize the class

        :param nodes:
        all the nodes in the given network

        :param probabilities:
        all the probabilites in the given network

        :param observed:
        all the evidence that is assigned in run.py
        """
        self.nodes = nodes
        self.observed = observed
        self.probabilities = probabilities

    def create_factors(self) -> Dict[str, FactorTable]:
        """
        This function create factors from the given probabiliteis in the network.

        :return:
        A dictionary with FactorTable objects used to represent the probailities
        in a slightly different manner outside of the dataframe
        """

        factors = {}
        for key, value in self.probabilities.items():
            factors[key] = FactorTable(key, value)
        return factors

    def filter_observed(self, factors: Dict[str, FactorTable]) -> None:
        """
        This function filters out observed values out of the Factors (FactorTable objects)

        :param factors:
        A dictionary with FactorTable objects containing data from the given network
        """

        if self.observed:
            for observed_name, observed_value in self.observed.items():
                for key, factor_table in factors.items():
                    if observed_name in factor_table.columns:
                        print("------------------------------------------------------------")
                        print("Found a FactorTable (" + key + ") with the observed Value")
                        factor_table.locate_and_change_observed(observed_name, observed_value)
            print("------------------------------------------------------------")

    def factor_identification(self) -> None:
        factors = self.create_factors()
        self.filter_observed(factors)

        print("\nCheck if data truly is removed from all factors:\n")

        for key, factor_table in factors.items():

            print(factor_table.dataframe, "\n")

