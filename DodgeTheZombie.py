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
    pass

def main():
    pass

if __name__ == '__main__':
    main()