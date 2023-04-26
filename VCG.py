from itertools import combinations_with_replacement, permutations

class VCG:

    def __init__(self, agents, num_agents, num_items):
        self.agents = agents
        self.num_agents = num_agents
        self.num_items = num_items
    
    def _calculate_winner(self, agents, num_agents, num_items):
        item_combinations = self._calc_item_combinations(num_items, num_agents)
        #calculate the combos of agents per num item combo
        agent_item_allocations = self._calc_item_agent_allocations(num_agents, item_combinations) 

        print("welfare")
        max_welfare = 0
        win_allocation = None
        for agents_items in agent_item_allocations:
            print(agents_items)
            agents_combo = agents_items[0]
            item_allocation = agents_items[1]
            print("agents_combo", agents_combo)
            print("item_allocation", item_allocation)
            total_welfare = 0
            for i in range(len(agents_combo)):
                agent_num = agents_combo[i]
                items_num = item_allocation[i]
                print("agent_num", agent_num)
                print("items_num", items_num)
                value = agents[agent_num][items_num]
                total_welfare += value
            if total_welfare > max_welfare:
                max_welfare = total_welfare
                win_allocation = agents_items
            print()

 
    # Calculates all possible ways the items can be divided into at most num_agents/n subsets
    def _calc_item_combinations(self, num_items, num_agents):
        possible_num_items = [x for x in range(1, 1 + num_items)]
        greater = num_items + 1
        if num_items + 1 > num_agents + 1:
            greater = num_agents + 1
        item_combinations = {}
        for r in range(1, greater):
            item_combos = combinations_with_replacement(possible_num_items, r)
            for item_combo in item_combos:
                #all possible item combinations (not just those that have a total of num_items)
                item_combo = list(item_combo)
                if sum(item_combo) == num_items:
                    item_combo.sort()
                    item_combo_str = " ".join(str(x) for x in item_combo)
                    item_combinations[item_combo_str] = item_combo
        print("item combinations:", item_combinations)
        return item_combinations
    
    # Calculates all possible item-agent allocations
    def _calc_item_agent_allocations(self, num_agents, item_combinations):
        possible_agents = [x for x in range(1, num_agents + 1)]
        print("possible_agents:", possible_agents)
        agent_item_allocations = []
        for item_combo in item_combinations.values():
            print("item allocation", item_combo)
            agent_combinations = permutations(possible_agents, len(item_combo))
            for agent_combo in agent_combinations:
                agent_combo = list(agent_combo)
                print("agents", agent_combo)
                #pairs of agents and allocations
                agents_items_pair = [agent_combo, item_combo]
                agent_item_allocations.append(agents_items_pair)
        print(agent_item_allocations)
        return agent_item_allocations

    def allocation():
        pass
    
    def payments():
        pass
