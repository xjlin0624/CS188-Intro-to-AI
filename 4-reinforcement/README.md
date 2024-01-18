## Introduction
In this project, students implement value iteration and Q-learning. The agents are tested first on Gridworld (from class), then apply them to a simulated robot controller (Crawler) and Pacman.
## File Directory
- `valueIterationAgents.py`	A value iteration agent for solving known MDPs.
- `qlearningAgents.py`	Q-learning agents for Gridworld, Crawler and Pacman.
- `analysis.py`	A file to put your answers to questions given in the project.
- `mdp.py`	Defines methods on general MDPs.
- `learningAgents.py`	Defines the base classes ValueEstimationAgent and QLearningAgent, which your agents will extend.
- `util.py`	Utilities, including util.Counter, which is particularly useful for Q-learners.
- `gridworld.py`	The Gridworld implementation.
- `featureExtractors.py`	Classes for extracting features on (state, action) pairs. Used for the approximate Q-learning agent (in qlearningAgents.py).
- `environment.py`	Abstract class for general reinforcement learning environments. Used by gridworld.py.
- `graphicsGridworldDisplay.py`	Gridworld graphical display.
- `graphicsUtils.py`	Graphics utilities.
- `textGridworldDisplay.py`	Plug-in for the Gridworld text interface.
- `crawler.py`	The crawler code and test harness. You will run this but not edit it.
- `graphicsCrawlerDisplay.py`	GUI for the crawler robot.
- `autograder.py`	Project autograder
- `testParser.py`	Parses autograder test and solution files
- `testClasses.py`	General autograding test classes
- `test_cases/`	Directory containing the test cases for each question
- `reinforcementTestClasses.py`	Project 4 specific autograding test classes
