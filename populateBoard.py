import numpy as np
boardSize = int(np.random.uniform(4, 7))

board = [['x' for _ in range(boardSize)] for _ in range(boardSize)]


def populateColours(count):
    totalBlocks = boardSize ** 2
    for i in range(boardSize):
        for j in range(boardSize):
            probability = int(np.random.uniform(0, 100))
                
                
        
        