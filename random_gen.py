from VCG import VCG
import sys
import random

def generate(num_agents, num_items):
    agents = {} # agent : num_items
    for i in range(1, num_agents + 1):
        dct = {} # num_items : value
        for j in range(num_items + 1):
            dct[j] = j * random.uniform(0, 1)
        agents[i] = dct
    return agents
            

def main():
    random.seed(42)

    agents = generate(2, 4)
    print("agents", agents)
    vcg = VCG(agents, 2, 4)
    vcg._calculate_winner(agents, 2, 4)
    sys.exit(0)


    # n agents
    n = [2, 4, 5, 6]

    # m items
    m = [4, 6, 8, 10, 12, 14, 16, 18, 20]

    for i in n:
        for j in m:
            print(i, j)
            agents = generate(i, j)
            print(agents)
            vcg = VCG(agents, j)
            if j == 6:
                break
        sys.exit(0)

if __name__ == "__main__":
    main()