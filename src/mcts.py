import numpy as np
import copy
from operator import itemgetter


class TreeNode(object):
    """
    A node in the MCTS tree.
    """

    def __init__(self, parent, prior_p):
        self._parent = parent
        self._children = {}  # a map from action to TreeNode
        self._n_visits = 0
        self._Q = 0
        self._u = 0
        self._P = prior_p
