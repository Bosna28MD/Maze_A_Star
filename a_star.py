#a=[[ 0 for _ in range(8)] for _ in range(8)]

a=[ [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,5,5,5,5,0,0],
    [0,0,5,0,0,0,0,0],
    [0,0,5,0,0,0,0,0],
    [0,0,5,0,0,2,0,0],
    [0,0,0,0,0,0,0,0]
    ]

point_start=(2,1);
point_final=(5,6);

#a[point_start[0]][point_start[1]]=1
#a[point_final[0]][point_final[1]]=2



# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j],end=" ")
#     print("");        

def h_cost(x_current,y_current,x_final,y_final): #Heuristic Cost
    x=x_current;
    y=y_current;
    val=0;
    incrementor=14;
    while ( not (x==x_final and y==y_final) ):
        if(x==x_final or y==y_final):
            if(x==x_final):
                if(y>y_final):
                    y-=1;
                else:
                    y+=1;
            elif(y==y_final):
                if(x>x_final):
                    x-=1;
                else:
                    x+=1;
            val+=10;
            #continue;
        else:
            if(x>x_final and y>y_final):
                x-=1;
                y-=1;
            elif(x>x_final and y<y_final):
                x-=1;
                y+=1;
            elif(x<x_final and y>y_final):
                x+=1;
                y-=1;
            elif(x<x_final and y<y_final):
                x+=1;
                y+=1;
            val+=14;
    return val;


#print( h_cost(point_start[1],point_start[0],point_final[1],point_final[0]) )        
#print( h_cost(0,0,3,2) )


# def A_Star_Algorithm(matrix):
#     obstacle=5;
#     start_point=1;
#     final_point=2;
    
class A_Star_Algorithm:
    obstacle=5;
    start_point_val=1;
    final_point_val=2;
    free_space=0
    direction=( (-1,-1) , (-1,0) , (-1,1) , (0,1) , (1,1) , (1,0) , (1,-1) , (0,-1) ) #  up-left , up-middle , up-right , middle-right , down-right , down-middle , down-left , middle-left
    
    def __init__(self,matrix,row,column,start_point,finish_point):
        self.matrix=matrix;
        self.row=row;
        self.column=column;
        self.start_point=start_point; #(y,x)
        self.finish_point=finish_point; #(y,x)


    def find_neighbors(self,node): #node=(y,x) coordonate
        neighbors=[];

        for i in range(len(A_Star_Algorithm.direction)):
            y=node[0]+A_Star_Algorithm.direction[i][0];
            x=node[1]+A_Star_Algorithm.direction[i][1];
            limit_intervals=( x<0  or  y<0  or  x>(self.column-1)  or  y>(self.row-1) );
            if( not limit_intervals ):
                if(self.matrix[y][x]!=A_Star_Algorithm.obstacle):
                    neighbors.append( (y,x) );    
        
        return neighbors; #return a tuple of neighbors


    
    def Algorithm(self):
        matrix_traversed=[ [ [0,0,0] for _ in range(self.column)] for _ in range(self.row) ];  #( value_traversed , G , H );
        current_node=( self.start_point[0] , self.start_point[1] ); #(y,x)


        for i in range(self.row):
            for j in range(self.column):
                if(self.matrix[i][j]==A_Star_Algorithm.obstacle):
                    matrix_traversed[i][j][1]=-1;  #Obstacle  
                matrix_traversed[i][j][2]=A_Star_Algorithm.h_cost(j,i,self.finish_point[1],self.finish_point[0]);
                matrix_traversed[i][j][0]=-1; # At start all nodes are untraversed and untouched


        """ for i in range(self.row):
            for j in range(self.column):
                print(matrix_traversed[i][j],end=" ")
            print("");

        print('\n') """  

        while True:
            neighbors_currentNodes=self.find_neighbors(current_node);
            if( len(neighbors_currentNodes)==0 ): #no neighbors
                #print("No neighbors");
                return None;

            matrix_traversed[current_node[0]][current_node[1]][0]=1; # 1-node traversed , 0 touched , -1-untraversed and untouched

            
            
            # print(current_node)
            # print(neighbors_currentNodes)
            # print("\n")


            for i in range( len(neighbors_currentNodes) ):
                mat_neighborData=matrix_traversed[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]];
                mat_currentData=matrix_traversed[current_node[0]][current_node[1]]
                if(matrix_traversed[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]][0]!=1):
                    if( neighbors_currentNodes[i][0]==current_node[0]  or  neighbors_currentNodes[i][1]==current_node[1] ):
                        #G_new=matrix_traversed[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]][1]+10;
                        G_new=mat_currentData[1]+10;
                        if(matrix_traversed[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]][0]==-1):
                            matrix_traversed[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]][1]=G_new;
                        elif(matrix_traversed[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]][0]==0 and mat_neighborData[1]>G_new):
                            matrix_traversed[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]][1]=G_new;

                    else:
                        #G_new=matrix_traversed[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]][1]+14
                        #matrix_traversed[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]][1]+=14;
                        G_new=mat_currentData[1]+14;
                        if(mat_neighborData[0]==-1):
                            matrix_traversed[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]][1]=G_new;
                        elif(mat_neighborData[0]==0 and mat_neighborData[1]>G_new):
                            matrix_traversed[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]][1]=G_new;
                    
                    if(matrix_traversed[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]][0]==-1):
                        matrix_traversed[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]][0]=0;
            
            # for i in range(self.row):
            #     for j in range(self.column):
            #         print(matrix_traversed[i][j],end=" ")
            #     print("");
            # print("\n")

            next_node=self.find_nextCurrentValueMin(matrix=matrix_traversed) #min
            if(next_node==None): #All next_node are used
                #print("All next_node are used") 
                return None;
            current_node=( next_node[0] , next_node[1]);

            


            if(current_node[0]==self.finish_point[0] and current_node[1]==self.finish_point[1]):
                break;

        return matrix_traversed;

        

        #print(current_node)

    def find_ShortPath(self):
        matrix=self.Algorithm();
        if(matrix==None):
            #print("NO path!!!")
            return None;

        # for i in range(self.row):
        #     for j in range(self.column):
        #         print(matrix[i][j],end=" ")
        #     print("");
        # print("\n");

        listNodes=[];
        curent_node=(self.finish_point[0],self.finish_point[1]);
        listNodes.append(curent_node);
        while True:
            if(curent_node[0]==self.start_point[0] and curent_node[1]==self.start_point[1]):
                break;

            neighbors_currentNodes=self.find_neighbors(curent_node);
            val_min=[];
            for i in range(len(neighbors_currentNodes)):
                data_neighBorNode=matrix[neighbors_currentNodes[i][0]][neighbors_currentNodes[i][1]];
                if(data_neighBorNode[0]==1):
                    if(len(val_min)==0):
                        val_min.append( (neighbors_currentNodes[i][0],neighbors_currentNodes[i][1],data_neighBorNode[1]+data_neighBorNode[2],data_neighBorNode[1]) );
                        continue;
                    if( val_min[0][2]>(data_neighBorNode[1]+data_neighBorNode[2]) or  (val_min[0][2]==(data_neighBorNode[1]+data_neighBorNode[2]) and val_min[0][3]>data_neighBorNode[1]  )  ):    
                        val_min.pop();
                        val_min.append( (neighbors_currentNodes[i][0],neighbors_currentNodes[i][1],data_neighBorNode[1]+data_neighBorNode[2],data_neighBorNode[1]) );
            

            curent_node=(val_min[0][0],val_min[0][1]);
            listNodes.append(curent_node);

        
        if(len(listNodes)==0):
            return None;
        return listNodes;








    
    
    def find_nextCurrentValueMin(self,matrix):
        min_val=[];  #(y,x,G,H)  y,x: position of node , total_value: G+H ,if (total_value==total_value) -> min(h)
        for i in range(self.row):
            for j in range(self.column):
                if( matrix[i][j][0]==0 ):
                    if(len(min_val)==0):
                        min_val.append( ( i, j, matrix[i][j][1], matrix[i][j][2] ) );
                        continue;
                    if( (min_val[0][2]+min_val[0][3]) > (matrix[i][j][1] + matrix[i][j][2]) ):
                        # for _ in range(len(min_val)):
                        #     min_val.pop();
                        min_val.pop();
                        min_val.append( ( i, j, matrix[i][j][1], matrix[i][j][2] ) );
                    elif( (min_val[0][2]+min_val[0][3]) == (matrix[i][j][1] + matrix[i][j][2])  and  (min_val[0][3]>matrix[i][j][2]) ):
                        min_val.pop();
                        min_val.append( ( i, j, matrix[i][j][1], matrix[i][j][2] ) );
        if(len(min_val)==0):
            return None;
        return min_val[0];
                        




            

    def h_cost(x_current,y_current,x_final,y_final): #Heuristic Cost
        x=x_current;
        y=y_current;
        val=0;
        incrementor=14;
        while ( not (x==x_final and y==y_final) ):
            if(x==x_final or y==y_final):
                if(x==x_final):
                    if(y>y_final):
                        y-=1;
                    else:
                        y+=1;
                elif(y==y_final):
                    if(x>x_final):
                        x-=1;
                    else:
                        x+=1;
                val+=10;
                #continue;
            else:
                if(x>x_final and y>y_final):
                    x-=1;
                    y-=1;
                elif(x>x_final and y<y_final):
                    x-=1;
                    y+=1;
                elif(x<x_final and y>y_final):
                    x+=1;
                    y-=1;
                elif(x<x_final and y<y_final):
                    x+=1;
                    y+=1;
                val+=14;
        return val;




if(__name__=="__main__"):


    b=[ [0,0,0,0,0],
        [0,5,2,0,0],
        [0,5,5,5,0],
        [0,0,1,0,0],
        [0,0,0,0,0]
    ]



    #b1=A_Star_Algorithm(b , len(b) , len(b[0]) , (3,2) , (1,2) );
    #b1.Algorithm()




    c=[ [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,5,2,0,0,0,0,0,0],
        [0,0,0,5,5,5,5,5,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0]
        ];

    d=[ [0,0,0,5,5,5,0,0,0,0,0],
        [0,0,0,0,2,5,0,0,0,0,0],
        [0,0,0,5,5,5,5,5,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0]
        ];

    e=[ [0,0,0,5,5,5,0,0,0,0,0],
        [0,0,0,0,2,5,0,0,0,0,0],
        [0,0,0,5,5,5,5,5,0,0,0],
        [0,0,0,0,0,0,5,0,0,0,0],
        [0,0,0,0,0,0,5,1,0,0,0],
        [0,0,0,0,0,0,5,0,0,0,0]
        ];

    c1=A_Star_Algorithm(d,len(d),len(d[0]),(4,7),(1,4))
    if(c1.find_ShortPath()==None):
        print("No path");
    else:
        print(c1.find_ShortPath())
    #print(c1.Algorithm())
    #c1.find_ShortPath()

    #a1=A_Star_Algorithm(a,len(a),len(a[0]),(2,2),(6,5) );
    #print( a1.find_neighbors( a1.start_point ) )
    #print( a1.find_neighbors( (1,0) ) )
                
                #if(x)
                #if( self.matrix[ self.start_point[0] ][ self.start_point[1] ]  ):
                    
