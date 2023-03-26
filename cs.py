# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 21:20:16 2023

Connected sequential algorithm

@author: tymot
"""

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import queue

def connected_sequential(G):
    """
    Parameters
    ----------
    G : Graph
        Graph G from nx library.

    Returns
    -------
    colors : List
        List of colors (non-negative integers), representing good coloring 
        of Graph G. Coloring is generated by the Connected Sequential algorithm

    """
    nodes = list(G.nodes())
    m = len(nodes)


    # TODO - check if graph is connected
    
    colors = [-1] * m
    
    forbidden_colors = []
    q = queue.Queue()
    q.put(random.randint(0, m-1)) # put random first vertex
    
    while not q.empty():
        v = q.get()
        if colors[v] == -1: 
            # if the actual vertex is uncolored
            neighbors = G.neighbors(v)
            forbidden_colors = []
            for neighbor in neighbors:
                if colors[neighbor] == -1:
                    q.put(neighbor)
                else:
                    forbidden_colors.append(colors[neighbor])
            
            # now we find the smallest color that we can use
            color = 0
            while color in forbidden_colors:
                color += 1
            colors[v] = color # color the choosen vertex
            
    return colors