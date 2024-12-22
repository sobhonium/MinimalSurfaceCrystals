import numpy as np

from unit_cell import UnitCell


        
        
        
class Crystal:
    def __init__(self, unit_cell, g1_dim=1, g2_dim=1, g3_dim=1):
        self.unit_cell = unit_cell
        self.g1_dim = g1_dim
        self.g2_dim = g2_dim
        self.g3_dim = g3_dim
        self.crystal_create_()
    # Function to generate crystal skeletal structure
    def crystal_create_(self,):
        
        
        v, e = self.unit_cell.vertices, self.unit_cell.edges
        g1, g2, g3 = self.unit_cell.g1, self.unit_cell.g2, self.unit_cell.g3
        
        self.vertices = []
        self.edges = []
        # Create the transformed vertices and edges
        for i in range(self.g1_dim):
            for j in range(self.g2_dim):
                for k in range(self.g3_dim):
                    for T in range(len(v)):
                        transformed_point = v[T] + (i - 1) * g1 + (j - 1) * g2 + (k - 1) * g3
                        self.vertices.append(transformed_point)

                    # Transform edges
                    for T in range(len(e)):
                        p1_idx, p2_idx = e[T]
                        p1_transformed = v[p1_idx] + (i - 1) * g1 + (j - 1) * g2 + (k - 1) * g3
                        p2_transformed = v[p2_idx] + (i - 1) * g1 + (j - 1) * g2 + (k - 1) * g3
                        self.edges.append([p1_transformed, p2_transformed])

        self.vertices = np.array(self.vertices)     
    

