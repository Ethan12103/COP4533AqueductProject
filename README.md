# COP4533AqueductProject
Programming algorithm written in python to solve the following problem.
## Problem
"You are in charge of directing water through an aqueduct from a source to several bath houses. The aqueduct consists of stations connected by ramps that carry water. The stations are laid out in an m x n grid, in which the source station S is located at position (0,0). From any station located at position (x,y), where 0 <= x < m and 0 <= y < n, there is a ramp leading to the station at position (x-1,y), (x+1,y), (x,y-1), and (x,y+1), so long as the target station lies inside the grid. Each station is at some height above the ground, and the time it takes for water to move along a ramp from station (x,y) to station (x’,y’) is time((x,y),(x’,y’)) = max(-1, 1 + (height(x’,y’) - height(x,y))). Given a set B = {b_1 = (x_1,y_1),...,b_n = (x_n,y_n)} of positions of stations that supply water to baths, a supply path is a (not necessarily simple) path in the aqueduct that starts from the source station S, visits every station in B, and ends at when it reaches the last station in B that it has not yet visited. The cost of a supply path is the total time it takes water to move along this path. Note that if such a path visits station (x,y), followed by station (x+1,y), followed by station (x,y), then the time it takes for water to move
between these stations is time((x,y),(x+1,y)) + time((x+1,y),(x,y))
Goal: given the set B, compute the minimum cost of any supply path.
Note: The path should end in one of the stations"
## How to run the program
The program will read a file called “grid.txt” in the root directory. The file should contain the following information:
1. Number of rows and columns in the grid - e.g. 5, 5
2. Station height, x-coordinate, and y-coordinate - e.g., 5, 1, 2. Each station is
written on its own line. The stations are listed row by row, starting with the
station at position (0,0). For example:
2, 0, 0
4, 1, 0
...
1, m, 0
7, 0, 1
...
3. x-coordinate and y-coordinate of the station “S” on its own line.
4. x-coordinate and y-coordinate of the stations in B, each written on their own line.
For example:
3, 2
4, 5
...

The program will then write the path length as an integer to the pathLength.txt file.