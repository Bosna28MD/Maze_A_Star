# Maze(A* Algorithm)

## Description
In this project is printed a board 2D(16x16) for finding(printing) the shortest-path between two points using **A\* Algorithm**. The boxes in board can be of following color:
1. white   -> free point
2. red     -> start point
3. blue    -> end point
4. green   -> obstacle point
5. purple  -> path

The point of start and point of end is setted hard-coded. As action user can use click-left and click-right. CLick-left is for the event of coloring the white box in green color(printing the obstacle-point) 
and click-right is used for coloring a green box into a white box(removing the obstacle-point). 

The goal of this program is anytime user color  a white-box(free-box) into a green-box(obstacle box) or vice-versa is called A* algorithm for finding the shortest path(green) between start-point and end-point.
<p>The path can be traversed in 8 direction: up, down, left, right, up-left, up-right, down-left and down-right.When it's traversed into a near box up,down,left and right the value is 10, 
  but in up-left, up-right, down-left and down-right value is 14.    </p>

## File
- a_star.py --> in this file is algorithm A* implemented;
- maze.py   --> in this file is main file of the program where is printed board and all functionality of this project;

## Prerequisites
- install python
- install pygame ```pip install pygame```



## Running project:
1. Go to repository folder ```cd <Repository-Name>```
2. Run script maze.py ```python3 maze.py```(Linux or Mac) or ```python maze.py```(Windows)

## Image


![Maze_a_star_photo3](https://github.com/user-attachments/assets/086d59ad-a011-4ddd-8ade-3730c87dc1e8)
![Maze_a_star_photo2](https://github.com/user-attachments/assets/53662592-2e8b-4f40-bbab-c20bb16929a4)
