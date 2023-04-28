import random
import time

from VCG import VCG

def generate(num_agents, num_items):
    """
    This function generates different values for every subset of num_items for 
    every agent. It returns the generated data as a nested dictionary.
    """
    agents = {} # agent : num_items
    for i in range(1, num_agents + 1):
        dct = {} # num_items : value
        for j in range(num_items + 1):
            dct[j] = j * random.uniform(0, 1)
        agents[i] = dct
    return agents

         
def print_results(allocations, payments):
    """
    This function prints the results of the VCG algorithm.
    """
    print("allocations:")
    print(allocations)
    print("payments:")
    print(payments)


def main():
    random.seed(42)

    # n agents
    n = [2, 4, 5, 6]

    # m items
    m = [4, 6, 8, 10, 12, 14, 16, 18, 20]

    print("\nn is the number of agents")
    print("m is the number of items\n")
    for i in n:
        for j in m:
            print(f"n = {i}, m = {j}")
            agents = generate(i, j)
            #print("agents\n", agents)

            start = time.time()
            vcg = VCG(agents, i, j)
            allocations, payments = vcg.calc_allocations_payments()
            time_elapsed = time.time() - start
            # allocations form is [[agent number], [num_items]], the indicies 
            # correspond which agent gets allocated how many items
            # payment is a dictionary with this form- agent number : payment
            print_results(allocations, payments)
            #time elapsed is in seconds
            print("time_elapsed:", time_elapsed)
            print()


if __name__ == "__main__":
    main()