"Dodge the Zombie Problem"
from heapq import heappush, heappop

class Zombie_problem(object):
    def __init__(self):
        self.people_cost = {'undergrad': 1, 'grad': 2, 'postdoc': 5, 'professor': 10}
        self.people = ['undergrad', 'grad', 'postdoc', 'professor']
        
    def start_node(self):
        """returns start node"""
        start = ('left', 'left', 'left', 'left', 'left') # Everyone on the left side of the bridge
        return (start)
    
    def is_goal(self, node):
        """is True if `node` is a goal"""
        return node == ('right', 'right', 'right', 'right', 'right') # Everyone on the right side of the bridge
    
    def neighbors(self, node):
        """returns a list of the arcs for the neighbors of `node`"""
        neighbors = []
        current_state = list(node) 
        flash_pos = current_state[-1] # Last element in  node is postion of flashlight
        if flash_pos == 'left': # select two people from left to go to right
            for i in range(len(current_state)-1):
                for j in range(i + 1, len(current_state)-1):
                    
                    if current_state[i] == flash_pos or current_state[j] == flash_pos: 
                            new_state = list(current_state)
                            new_state[i] = 'right' # changing their position to right
                            new_state[j] = 'right'
                            new_state[-1] = 'right'
                            neighbors.append(tuple(new_state))
        else : # select one person form right to go back to left
            for i in range(len(current_state)-1):
                curr_direction = 'right' 
                if current_state[i] == curr_direction:
                    new_state = list(current_state)
                    new_state[i] = 'left' # changing their position to left
                    new_state[-1] = 'left'
                    neighbors.append(tuple(new_state))
        return neighbors          
    
    def arc_cost(self, arc):
        """Returns the cost of `arc`"""
        # Handled in cost()
        return 

    def cost(self, path):
        """Returns the cost of `path`""" 
        cost = 0  

        for i in range(1, len(path)):  # arc number excluding first arc
            prev_arc = path[i-1] # setting previous arc
            cost_list = [] 
            for j in range(4):  # person number
                if path[i][j] != prev_arc[j]: # checking which person changed positions
                    cost_list.append(self.people_cost[self.people[j]])
            cost += max(cost_list)
                    
        return cost
    
    def heuristic(self, node):
        """Returns the heuristic value of `node`""" 
        current_state = node  
        h = 0
        for i in range(len(current_state)-1): 
            if current_state[i] == 'left': # for all persons on left check their estimate cost to move to right            
                    h += self.people_cost[self.people[i]]                      
        return h
    
    def search(self):
        """Return a solution path"""      
        start = self.start_node()
        frontier = Frontier()
        frontier.add([start], self.heuristic(start))
       
        while not frontier.is_empty():
            path = frontier.remove() # Removing f minimizing path        
            current_node = path[-1]
            if self.is_goal(current_node): 
                return path # goal node
            
            for neighbor in self.neighbors(current_node):
                new_path = list(path) 
                new_path.append(neighbor)
                new_prioity = self.cost(new_path) + self.heuristic(neighbor) 
                frontier.add(new_path, new_prioity) # Adding new path to frontier
 
        return None

class Frontier(object):
    """
    Convenience wrapper for a priority queue usable as a frontier
    implementation.
    """
    def __init__(self):
        self.heap = []

    def add(self, path, priority):
        """Add `path` to the frontier with `priority`"""
        # Push a ``(priority, item)`` tuple onto the heap so that `heappush`
        # and `heappop` will order them properly
        heappush(self.heap, (priority, path))

    def remove(self):
        """Remove and return the smallest-priority path from the frontier"""
        (priority, path) = heappop(self.heap)
        return path

    def is_empty(self):
        return len(self.heap) == 0


def unit_tests():
    """
    Some trivial tests to check that the implementation even runs.
    Feel free to add additional tests.
    """
    print("testing...")
    p = Zombie_problem()
    assert p.start_node() is not None
    
    assert not p.is_goal(p.start_node())
    
    assert p.heuristic(p.start_node()) >= 0
    

    ns = p.neighbors(p.start_node())
    assert len(ns) > 0
    

    soln = p.search()
    assert p.cost(soln) > 0
    
    print("tests ok")

def main():
    unit_tests()
    p = Zombie_problem()
    soln = p.search()
    if soln:
        print("Solution found (cost=%s)\n%s" % (p.cost(soln), soln))
    else:
        raise RuntimeError("Empty solution")

if __name__ == '__main__':
    main()