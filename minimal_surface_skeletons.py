import numpy as np

from unit_cell import UnitCell


        
        
        
class Primitive:
    def __init__(self, edge_param=np.array([1, 1, 1]), 
                 angle_param=np.array([np.pi/2, np.pi/2]), classic_cubic=True):

        if classic_cubic==True:
            self.build_cube_graphs_() # to be implemented
        else:
            self.angle_param = angle_param
            self.edge_param = edge_param
            self.build_graphs_()
    def build_cube_graphs_(self, ):
        vertices_channlel1 = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
        
        vertices_channlel2 =  np.array([[1/2, 1/2, 1/2], [1/2, 1/2, 3/2], [1/2, 1/2, -1/2],
                                 [1/2, 3/2, 1/2], [1/2, -1/2, 1/2], [-1/2, 1/2, 1/2],
                                 [3/2, 1/2, 1/2]])
        
        edges_channel1 = [[0, 1], [0, 2], [0, 3]]
        edges_channel2 = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6]]
        
        # Generators vectors
        g1=np.array([1, 0, 0]) 
        g2=np.array([0, 1, 0])
        g3=np.array([0, 0, 1])
        
        self.skelton_chalnnel1 = UnitCell(vertices=vertices_channlel1, 
                                          edges=edges_channel1, 
                                          g1=g1, g2=g2, g3=g3)
        self.skelton_chalnnel2 = UnitCell(vertices=vertices_channlel2, 
                                  edges=edges_channel2, 
                                  g1=g1, g2=g2, g3=g3)
    def build_graphs_(self,):
        v = np.empty((4,3))
        v[0] = np.array([0,0,0])
        v[1] = v[0] + np.array([1,0,0])*self.edge_param[0]
        v[2] = v[0] + np.array([np.cos(self.angle_param[0]),np.sin(self.angle_param[0]),0])*self.edge_param[1]
        v[3] = v[0] + np.array([np.cos(self.angle_param[1]), 0 , np.sin(self.angle_param[1])])*self.edge_param[2]
        
        vertices_channlel1 = v
    
        vertices_channlel2 =  1/2 - v
    
        edges_channel1 = [[0, 1], [0, 2], [0, 3]]
        edges_channel2 = [[0, 1], [0, 2], [0, 3]]
    
        # Generators vectors
        g1=v[1] 
        g2=v[2]
        g3=v[3]
        self.skelton_chalnnel1 = UnitCell(vertices=vertices_channlel1, 
                                          edges=edges_channel1, 
                                          g1=g1, g2=g2, g3=g3)
        self.skelton_chalnnel2 = UnitCell(vertices=vertices_channlel2, 
                                  edges=edges_channel2, 
                                  g1=g1, g2=g2, g3=g3)       




class Diamond:
    def __init__(self, edge_param=np.array([1, 1, 1, 1]), 
                 angle_param=np.array([109.5267460*np.pi/180, 109.5267460*np.pi/180]), classic_cubic=True):

        if classic_cubic==True:
            self.build_cube_graphs_() # to be implemented
        else:
            self.angle_param = angle_param
            self.edge_param = edge_param
            self.build_graphs_()
    def build_cube_graphs_(self, ):
                
        vertices_channlel1 = np.array([[7/8, 7/8, 3/8], [9/8, 9/8, 1/8], [5/8, 5/8, 1/8], [9/8, 5/8, 5/8], 
                                     [5/8, 9/8, 5/8], [3/8, 7/8, 7/8], [1/8, 5/8, 5/8], [5/8, 5/8, 9/8], 
                                     [7/8, 3/8, 7/8], [1/8, 9/8, 9/8], [5/8, 1/8, 5/8], [9/8, 1/8, 9/8], 
                                     [3/8, 3/8, 3/8], [1/8, 1/8, 1/8]])
    
        vertices_channlel2 =  np.array([[9/8, 9/8, 5/8], [7/8, 7/8, 7/8], [5/8, 9/8, 9/8], [5/8, 9/8, 1/8], 
                                     [3/8, 7/8, 3/8], [9/8, 5/8, 9/8], [1/8, 9/8, 5/8], [9/8, 5/8, 1/8], 
                                     [7/8, 3/8, 3/8], [5/8, 5/8, 5/8], [3/8, 3/8, 7/8], [1/8, 5/8, 9/8], 
                                     [9/8, 1/8, 5/8], [5/8, 1/8, 9/8], [1/8, 5/8, 1/8], [5/8, 1/8, 1/8], 
                                     [1/8, 1/8, 5/8]])
    
        edges_channel1 = [[0, 1], [0, 2], [0, 3], [0, 4], [4, 5], [5, 6], [5, 7], [5, 9], 
                                [3, 8], [7, 8], [8, 10], [8, 11], [2, 12], [12, 13], [10, 12], [6, 12]]
        edges_channel2 = [[0, 1], [1, 2], [1, 5], [3, 4], [4, 6], [7, 8], [9, 10], [1, 9],
                                [4, 9], [9, 8], [11, 10], [8, 12], [10, 13], [4, 14], [8, 15], [16, 10]]
        
        # Generators vectors
        g1=np.array([1, 0, 0]) 
        g2=np.array([0, 1, 0])
        g3=np.array([0, 0, 1])
        
        self.skelton_chalnnel1 = UnitCell(vertices=vertices_channlel1, 
                                          edges=edges_channel1, 
                                          g1=g1, g2=g2, g3=g3)
        self.skelton_chalnnel2 = UnitCell(vertices=vertices_channlel2, 
                                  edges=edges_channel2, 
                                  g1=g1, g2=g2, g3=g3)
    def build_graphs_(self,):
        v = np.empty((5,3))
        v[0] = np.array([3/8,3/8,3/8])
        v[1] = v[0] + np.array([1/4,1/4,-1/4])*self.edge_param[0]
        v[2] = v[0] + np.array([np.cos(self.angle_param[0])-np.sqrt(2)/2*np.sin(self.angle_param[0]),
                                np.cos(self.angle_param[0])-np.sqrt(2)/2*np.sin(self.angle_param[0]),
                                -np.cos(self.angle_param[0])-np.sqrt(2)*np.sin(self.angle_param[0])
                               ])*self.edge_param[1]/4
        v[3] = v[0] + np.array([1/4,-1/4,1/4])*self.edge_param[2]
        
        v[4] = v[0] + np.array([np.cos(self.angle_param[1])-np.sqrt(2)/2*np.sin(self.angle_param[1]),
                                -np.cos(self.angle_param[1])+np.sqrt(2)/2*np.sin(self.angle_param[1]),
                                np.cos(self.angle_param[1])+np.sqrt(2)*np.sin(self.angle_param[1])
                               ])*self.edge_param[3]/4        
        vertices_channlel1 = v
    
        vertices_channlel2 =  1 - v
    
        edges_channel1 = [[0, 1], [0, 2], [0, 3], [0,4]]
        edges_channel2 = [[0, 1], [0, 2], [0, 3], [0,4]]
    
        # Generators vectors
        g1=v[2] - v[1] 
        g2=v[3] - v[1]
        g3=v[4] - v[1]
        self.skelton_chalnnel1 = UnitCell(vertices=vertices_channlel1, 
                                          edges=edges_channel1, 
                                          g1=g1, g2=g2, g3=g3)
        self.skelton_chalnnel2 = UnitCell(vertices=vertices_channlel2, 
                                  edges=edges_channel2, 
                                  g1=g1, g2=g2, g3=g3)
                                  
                                  
class Gyroid:
    def __init__(self, edge_param=np.array([1,1,1, 1,1,1]), 
                 angle_param=np.array([2*np.pi/3, 2*np.pi/3, 2*np.pi/3, 2*np.pi/3, 2*np.pi/3]), classic_cubic=True):

        if classic_cubic==True:
            self.build_cube_graphs_() # to be implemented
        else:
            self.angle_param = angle_param
            self.edge_param = edge_param
            self.build_graphs_()
    def build_cube_graphs_(self, ):
        vertices_channlel1 = np.array([[0.625, 0.625, 0.625],
                                       [0.375, 0.875, 0.625],
                                       [0.375, 0.125, 0.875],
                                       [0.625, 0.375, 0.875],
                                       [0.875, 0.625, 0.375],
                                       [0.125, 0.875, 0.375],
                                       [0.125, 0.125, 0.125],
                                       [0.875, 0.375, 0.125],

                                        [1.125, 0.875, 0.375], #8
                                        [1.125, 0.125, 0.125], #9
                                        [0.375, 1.125, 0.875], #10
                                        [0.125, 1.125, 0.125], #11
                                        [0.125, 0.125, 1.125], #12 
                                        [0.875, 0.375, 1.125] #13
        ])


        vertices_channlel2 =  np.array([[0.375, 0.375, 0.375],
                                        [0.625, 0.125, 0.375],
                                        [0.625, 0.875, 0.125],
                                        [0.375, 0.625, 0.125],
                                        [0.125, 0.375, 0.625],
                                        [0.875, 0.125, 0.625],
                                        [0.875, 0.875, 0.875],
                                        [0.125, 0.625, 0.875],
                                        
                                        [-0.125,  0.125,  0.625],#8
                                        [-0.125,  0.875,  0.875],#9    
                                        [ 0.625, -0.125,  0.125],#10
                                        [ 0.875, -0.125,  0.875], # 11
                                        [ 0.875,  0.875, -0.125],#12
                                        [ 0.125,  0.625, -0.125]
        ])


        edges_channel1 = [[0,4], [0,1], [0,3], [3,2], [1,5], [4,7], [4,8], 
                           [7,9], [1,10], [5,11], [2,12], [3,13]]
        edges_channel2 =  [[0,4], [0,1], [0,3],[3,2], [1,5], [4,7], [4,8], 
                           [7,9], [1,10], [5,11], [2,12], [3,13]]

        # Generator vectors
        g1=np.array([1, 0, 0]) 
        g2=np.array([0, 1, 0])
        g3=np.array([0, 0, 1])
        
        self.skelton_chalnnel1 = UnitCell(vertices=vertices_channlel1, 
                                          edges=edges_channel1, 
                                          g1=g1, g2=g2, g3=g3)
        self.skelton_chalnnel2 = UnitCell(vertices=vertices_channlel2, 
                                  edges=edges_channel2, 
                                  g1=g1, g2=g2, g3=g3)
    def build_graphs_(self,):
        v = np.empty((7,3))
        
        v[0] = np.array([5/8,5/8,5/8])
        
        v[1] = v[0] + np.array([1,0,-1])*self.edge_param[0]/4
        
        v[2] = v[0] + np.array([np.cos(self.angle_param[0])/4-np.sqrt(3)/12*np.sin(self.angle_param[0]),
                                np.sqrt(3)/6*np.sin(self.angle_param[0]),
                                -np.cos(self.angle_param[0])/4-np.sqrt(3)/12*np.sin(self.angle_param[0])
                               ])*self.edge_param[1]
        
        v[3] = v[0] + np.array([np.cos(self.angle_param[1])/4+np.sqrt(3)/12*np.sin(self.angle_param[1]),
                                -np.sqrt(3)/6*np.sin(self.angle_param[1]),
                                -np.cos(self.angle_param[1])/4+np.sqrt(3)/12*np.sin(self.angle_param[1])
                               ])*self.edge_param[2]
        
        v[4] = v[1] + np.array([-np.cos(self.angle_param[2])/4-np.sqrt(3)/12*np.sin(self.angle_param[2]),
                                -np.sqrt(3)/6*np.sin(self.angle_param[2]),
                                np.cos(self.angle_param[2])/4-np.sqrt(3)/12*np.sin(self.angle_param[2])
                               ])*self.edge_param[3]

        v[5] = v[2] + np.array([np.cos(self.angle_param[3])/4-np.sqrt(3)/12*np.sin(self.angle_param[3]),
                                -1/4*np.cos(self.angle_param[3])-np.sqrt(3)/12*np.sin(self.angle_param[3]),
                                -np.sqrt(3)/12*np.sin(self.angle_param[3])
                               ])*self.edge_param[4]

        v[6] = v[3] + np.array([-np.sqrt(3)/6*np.sin(self.angle_param[4]),
                                1/4*np.cos(self.angle_param[4])-np.sqrt(3)/12*np.sin(self.angle_param[4]),
                                -1/4*np.cos(self.angle_param[4])-np.sqrt(3)/12*np.sin(self.angle_param[4])
                               ])*self.edge_param[5]
        
        vertices_channlel1 = v
    
        vertices_channlel2 =  1 - v
    
        edges_channel1 = [[0, 1], [0, 2], [0, 3], [1,4], [2,5], [3,6]]
        edges_channel2 = edges_channel1
    
        # Generators vectors
        g1=v[4] - v[2] 
        g2=v[5] - v[3]
        g3=v[6] - v[1]
        self.skelton_chalnnel1 = UnitCell(vertices=vertices_channlel1, 
                                          edges=edges_channel1, 
                                          g1=g1, g2=g2, g3=g3)
        self.skelton_chalnnel2 = UnitCell(vertices=vertices_channlel2, 
                                  edges=edges_channel2, 
                                  g1=g1, g2=g2, g3=g3)
                        
