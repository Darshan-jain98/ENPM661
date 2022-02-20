# 8 Puzzle Problem
Instructions to run the code:
Download the zip file and follow the steps below
This programme follows BFS for solving 8 Puzzle Problem
1.  Open the file Puzzle_Solver.py. Use the start and goal variables to specify the start and end for the 8 puzzle  problem.
2.  Provide the start and goal in the form of a numpy array as a normal matrix. 
    For example give np.array([[1,2,3],[4,5,6],[7,8,0]]) for
        1   2   3
        4   5   6
        7   8   0
3.  After editing the sand g variables, run the code.
4.  It will edit 3 file(Which has to be present in the folder which contains the code) namely Nodes.txt,NodesInfo.txt,nodePath.txt.
5.  Open and run plot_path.py to visualize the result. It will use the nodePath.txt file to see the list of nodes 
    visited from start to goal node.

NOTE: This programme will only give proper output if the output state is [[1,2,3],[4,5,6],[7,8,0]].
        1   2   3
        4   5   6
        7   8   0