# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]



def depthFirstSearch(problem: SearchProblem): 
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***" 
    visited = []                                # arr of coords
    stx = util.Stack()                          # stack of tuples
    parent = dict()                             # dictionary of { current tuple : parent tuple }
    
    curr = (problem.getStartState(), None, 0)
    stx.push(curr)
    
    while not stx.isEmpty():  
        curr = stx.pop()
        # print(curr)
        if problem.isGoalState(curr[0]):
            break
        else: 
            if curr[0] not in visited:
                visited.append(curr[0])             # coords
                suc = problem.getSuccessors(curr[0])
                for item in suc:                    # tuples
                    if item[0] not in visited:
                            parent[item] = curr     # dict item { current tuple : parent tuple }
                            stx.push(item)         
    
    actions = [curr[1]]                                         # last action
    while not parent[curr] == (problem.getStartState(), None, 0):          # while not origin
        actions.append(parent[curr][1])                         # append parent action
        curr = parent[curr]                                     # update to parent
    return actions[::-1]


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    actions = []
    visited = []
    q = util.Queue()                            # queue of tuples                         # dictionary of { current tuple : depth }

    curr = (problem.getStartState(), [], 0)
    q.push(curr)
    
    while not q.isEmpty(): 
        curr = q.pop()
        if problem.isGoalState(curr[0]):
            return actions + curr[1]
        else: 
            if curr[0] not in visited:
                visited.append(curr[0])
                suc = problem.getSuccessors(curr[0])
                for item in suc:
                    if item[0] not in visited:
                        act = curr[1] + [item[1]]                   # dict item { current tuple : depth }
                        q.push((item[0], act, item[2]))


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    actions = []
    visited = []
    pq = util.PriorityQueue()                   # priority queue of tuples

    curr = (problem.getStartState(), [], 0)
    pq.push(curr, curr[2])
    
    while not pq.isEmpty(): 
        curr = pq.pop()
        if problem.isGoalState(curr[0]):
            return actions + curr[1]
        else: 
            if curr[0] not in visited:
                visited.append(curr[0])
                suc = problem.getSuccessors(curr[0])
                for item in suc:
                    if item[0] not in visited:
                        act = curr[1] + [item[1]]                   # dict item { current tuple : depth }
                        cost = curr[2] + item[2]
                        pq.push((item[0], act, cost), cost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    actions = []
    visited = []
    func = lambda x : heuristic(x[0], problem) + x[2]
    pqf = util.PriorityQueueWithFunction(func)
    curr = (problem.getStartState(), [], 0)
    pqf.push(curr) 

    while not pqf.isEmpty(): 
        curr = pqf.pop()
        #print(curr)
        #print(func(curr))
        if problem.isGoalState(curr[0]):
            return actions + curr[1]
        else: 
            if curr[0] not in visited:
                visited.append(curr[0])
                suc = problem.getSuccessors(curr[0])
                for item in suc:
                    if item[0] not in visited:
                        act = curr[1] + [item[1]]                 
                        cost = curr[2] + item[2]
                        pqf.push((item[0], act, cost))
    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
