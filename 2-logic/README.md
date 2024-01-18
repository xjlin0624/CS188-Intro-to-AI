## Introduction
In this project, students use/write simple Python functions that generate logical sentences describing Pacman physics, aka pacphysics. Then with a SAT solver, pycosat, students solve the logical inference tasks associated with planning (generating action sequences to reach goal locations and eat all the dots), localization (finding oneself in a map, given a local sensor model), mapping (building the map from scratch), and SLAM (simultaneous localization and mapping).
## File Directory
- `logicPlan.py`	Where you will put your code for the various logical agents.
- `logic.py`	Propsitional logic code originally from aima-python with modifications for our project. There are several useful utility functions for working with logic in here.
- `logicAgents.py`	The file that defines in logical planning form the two specific problems that Pacman will encounter in this project.
- `pycosat_test.py`	Quick test main function that checks that the pycosat module is installed correctly.
- `game.py`	The internal simulator code for the Pacman world. The only thing you might want to look at in here is the Grid class.
- `test_cases/`	Directory containing the test cases for each question.
- `pacman.py`	The main file that runs Pacman games.
- `logic_util.py`	Utility functions for logic.py.
- `util.py`	Utility functions primarily for other projects.
- `logic_planTestClasses.py`	Project specific autograding test classes.
- `graphicsDisplay.py`	Graphics for Pacman.
- `graphicsUtils.py`	Support for Pacman graphics.
- `textDisplay.py` ASCII graphics for Pacman.
- `ghostAgents.py`	Agents to control ghosts.
- `keyboardAgents.py`	Keyboard interfaces to control Pacman.
- `layout.py`	Code for reading layout files and storing their contents.
- `autograder.py`	Project autograder.
- `testParser.py`	Parses autograder test and solution files.
- `testClasses.py`	General autograding test classes.
