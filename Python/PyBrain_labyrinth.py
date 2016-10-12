"""
Needed Installations:
=====================

sudo pip install pybrain
sudo pip install numpy
sudo apt-get install libblas-dev liblapack-dev libatlas-base-dev gfortran
sudo pip install scipy
sudo apt-get install pylab
pip install matplotlib
"""

from scipy import *
import sys, time

from pybrain.rl.environments.mazes import Maze, MDPMazeTask
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q, SARSA
from pybrain.rl.experiments import Experiment
from pybrain.rl.environments import Task
import pylab

pylab.gray()
pylab.ion()

structure = array([[1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 1, 0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 0, 0, 1, 0, 1],
                   [1, 0, 0, 1, 0, 0, 1, 0, 1],
                   [1, 0, 0, 1, 0, 1, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 1, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1]])

environment = Maze(structure, (7, 7))
controller = ActionValueTable(81, 4)
controller.initialize(1.)

learner = Q()
agent = LearningAgent(controller, learner)

task = MDPMazeTask(environment)

experiment = Experiment(task, agent)

while True:
    experiment.doInteractions(100)
    agent.learn()
    agent.reset()

    pylab.pcolor(controller.params.reshape(81,4).max(1).reshape(9,9))
    pylab.draw()
