"""
@Author Janneke Grooters
@Studentnumber s4739108
"""


from factor_table import FactorTable


def factor_identification(nodes: list, probabilities: dict, observed: dict):

    # Step 1: cycle trough each node and push their values into a FactorTable object
    factors = {}
    for key, value in probabilities.items():
        factors[key] = FactorTable(key, value)

    # Step 2 filter out observed from factors (thus removing them from any furhter calculations)
    if observed:
        for observed_name, observed_value in observed.items():
            for key, factor_table in factors.items():
                if observed_name in factor_table.columns:
                    print("\n========================")
                    print("Found a FactorTable ("+key+") with the observed Value")
                    factor_table.locate_and_change_observed(observed_name, observed_value)

