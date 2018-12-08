"""
@Author: Joris van Vugt, Moira Berens, Leonieke van den Bulk

Class for the implementation of the variable elimination algorithm.

"""

from factor_indetification import factor_identification
from read_bayesnet import BayesNet


class VariableElimination():

    def __init__(self, network: BayesNet):
        """
        Initialize the variable elimination algorithm with the specified network.
        Add more initializations if necessary.

        """
        self.network = network

    def run(self, query, observed, elim_order):
        """
        Use the variable elimination algorithm to find out the probability
        distribution of the query variable given the observed variables

        Input:
            query:      The query variable
            observed:   A dictionary of the observed variables {variable: value}
            elim_order: Either a list specifying the elimination ordering
                        or a function that will determine an elimination ordering
                        given the network during the run

        Output: A variable holding the probability distribution
                for the query variable

        """

        # CHANGE from original code:
        # Here is where my code begins

        # Step 1 Call elim_order() and run it to get the specified elimination order
        ordered_list = elim_order()
        print("Nodes after sorting: ", ordered_list)

        # Step 2: indentifying and reducing observables
        factor_identification(self.network.nodes, self.network.probabilities, observed)

        # Step 3: Variable elimination!!
        # oh no, no time, k, bye






