import numpy as np


from minimal_surface_skeletons import Primitive, Gyroid, Diamond
from utils import plotter                                  
from crystal import Crystal                                 
                                      
def main():

    # some sample skeletons of minimal surfaces with parameters changed.
    g1 = Primitive(classic_cubic=True) # standard Primitive (without parmater change on standard cartesian cubic).
    g2 = Diamond(edge_param=np.array([1.5, 1, 1, 1]),  
                 angle_param=np.array([209.5267460*np.pi/180, 109.5267460*np.pi/180]),
                 classic_cubic=False)   
                  
    g3 = Gyroid(edge_param=np.array([1, 2, 1,1,1,1]), 
                angle_param=np.array([2*np.pi/3, 2*np.pi/3, 2*np.pi/3, 2*np.pi/3, 2*np.pi/3]), 
                classic_cubic=False)
                  
    # 4 crystal to show              
    crystal1 = Crystal(unit_cell=g1.skelton_chalnnel1, g1_dim=3, g2_dim=3, g3_dim=2)
    crystal2 = Crystal(unit_cell=g2.skelton_chalnnel2, g1_dim=2, g2_dim=2, g3_dim=2)    
    crystal3 = Crystal(unit_cell=g2.skelton_chalnnel1, g1_dim=2, g2_dim=2, g3_dim=2)
    crystal4 = Crystal(unit_cell=g3.skelton_chalnnel2, g1_dim=3, g2_dim=5, g3_dim=2)
    
    crystals = [crystal1, crystal2, crystal3, crystal4]
    plotter(crystals=crystals)
    
    
 
if __name__ == "__main__":
    main()
