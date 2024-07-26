import pygame
import sys
import a_star as A_Star


# d=[ [0,0,0,5,5,5,0,0,0,0,0],
#     [0,0,0,0,2,5,0,0,0,0,0],
#     [0,0,0,5,5,5,5,5,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,1,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0]
#     ];



# c1=A_Star.A_Star_Algorithm(d,len(d),len(d[0]),(4,7),(1,4))
# if(c1.find_ShortPath()==None):
#     print("No path");
# else:
#     print(c1.find_ShortPath())

pygame.init()

window_size = (800, 800)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pygame Maze')



rect_size = 50
border_color = (0, 0, 0)  # BLack color

rects_clicked=[[(255,255,255) for _ in range(window_size[0]//rect_size)] for _ in range(window_size[1]//rect_size) ]
start_point=(4,3);
final_point=(10,8);
rects_clicked[start_point[0]][start_point[1]]=(255,0,0);
rects_clicked[final_point[0]][final_point[1]]=(0,0,255);

matrix_AStar_PAth=[[0 for _ in range(window_size[0]//rect_size) ] for _ in range(window_size[1]//rect_size) ];
matrix_AStar_PAth[start_point[0]][start_point[1]]=1;
matrix_AStar_PAth[final_point[0]][final_point[1]]=2;

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
        #     print(event.button)
        #     print(pygame.mouse.get_pos())
        #     mouse_x, mouse_y = pygame.mouse.get_pos()
        #     rowCell_clicked=mouse_y//rect_size
        #     columnCell_clicked=mouse_x//rect_size
        #     rects_clicked[rowCell_clicked][columnCell_clicked]=(0,255,0); 
        elif pygame.mouse.get_pressed()[0]:  #pygame.mouse.get_pressed()[0] for left click (PAINT)
                #print(event.pos)
                #print()
                mouse_x, mouse_y =event.pos;
                rowCell_clicked=mouse_y//rect_size
                columnCell_clicked=mouse_x//rect_size
                
                check_values_mouse=(mouse_x>window_size[0] or mouse_y>window_size[1] or mouse_x<0 or mouse_y<0);
                start_point_check=(start_point[0]==rowCell_clicked and start_point[1]==columnCell_clicked)
                final_point_check=(final_point[0]==rowCell_clicked and final_point[1]==columnCell_clicked)

                #print(rowCell_clicked,columnCell_clicked)
                if(rowCell_clicked>(window_size[1]//rect_size-1) or columnCell_clicked>(window_size[0]//rect_size-1) or check_values_mouse or start_point_check or final_point_check ):
                    break;
                rects_clicked[rowCell_clicked][columnCell_clicked]=(0,255,0);
                matrix_AStar_PAth[rowCell_clicked][columnCell_clicked]=5;
        elif pygame.mouse.get_pressed()[2]:  #pygame.mouse.get_pressed()[0] for left click (ERASE)
                #print(event.pos)
                #print()
                mouse_x, mouse_y =event.pos;
                rowCell_clicked=mouse_y//rect_size
                columnCell_clicked=mouse_x//rect_size
                #print(rowCell_clicked,columnCell_clicked)

                check_values_mouse=(mouse_x>window_size[0] or mouse_y>window_size[1] or mouse_x<0 or mouse_y<0);
                start_point_check=(start_point[0]==rowCell_clicked and start_point[1]==columnCell_clicked)
                final_point_check=(final_point[0]==rowCell_clicked and final_point[1]==columnCell_clicked)

                if(rowCell_clicked>(window_size[1]//rect_size-1) or columnCell_clicked>(window_size[0]//rect_size-1) or check_values_mouse or start_point_check or final_point_check ):
                    break;
                rects_clicked[rowCell_clicked][columnCell_clicked]=(255,255,255);
                matrix_AStar_PAth[rowCell_clicked][columnCell_clicked]=0;
                
                #pass

    
    #window.fill((255, 255, 255))  # White background
    c1=A_Star.A_Star_Algorithm(matrix_AStar_PAth,len(matrix_AStar_PAth),len(matrix_AStar_PAth[0]),start_point,final_point);
    path=c1.find_ShortPath();



    # Draw the rectanglem
    for i in range(window_size[1]//rect_size):
        for j in range(window_size[0]//rect_size):
            #print(j,i)
            rectangle_dim=(j*rect_size,i*rect_size,rect_size,rect_size)   
            pygame.draw.rect(window, rects_clicked[i][j] , rectangle_dim)
            pygame.draw.rect(window, border_color, rectangle_dim,width=1)
            
    if(path!=None):
        for i in range(len(path)):
            if( ( path[i][0]==start_point[0] and path[i][1]==start_point[1] ) or  ( path[i][0]==final_point[0] and path[i][1]==final_point[1] ) ):
                continue;
            rectangle_dim=(path[i][1]*rect_size,path[i][0]*rect_size,rect_size,rect_size);
            pygame.draw.rect(window, (125,0,125) , rectangle_dim);
                                              
    #pygame.draw.rect(window, rect_color, (0,0,50,50))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30) 













