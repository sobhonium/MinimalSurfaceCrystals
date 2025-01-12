# MinimalSurfaceCrystals
A simple tool for fine-tuning and generating unit cells and crystals of of minimal surfaces. The focus is on their medial axis (skeletons).

```python
import numpy as np


from minimal_surface_skeletons import Gyroid
from utils import plotter                                  
from crystal import Crystal

g3 = Gyroid(edge_param=np.array([1, 1, 1, 1, 1, 1]), 
                angle_param=np.array([2*np.pi/3, 2*np.pi/3, 2*np.pi/3, 2*np.pi/3, 2*np.pi/3]), 
                classic_cubic=False)
                  

crystal2 = Crystal(unit_cell=g3.skelton_chalnnel2, g1_dim=1, g2_dim=1, g3_dim=1)    
crystal3 = Crystal(unit_cell=g3.skelton_chalnnel1, g1_dim=1, g2_dim=1, g3_dim=1)
crystals = [crystal2, crystal3]
plotter(crystals=crystals)
    
```
![image](images/result_gyroid.png)


```python
import numpy as np


from minimal_surface_skeletons import Primitive
from utils import plotter                                  
from crystal import Crystal

g1 = Primitive(classic_cubic=True)

crystal1 = Crystal(unit_cell=g1.skelton_chalnnel1, g1_dim=3, g2_dim=3, g3_dim=2)
crystals = [crystal1]
plotter(crystals=crystals)    
```
![image](images/result_primitive.png)

By running ```main.py```, you will get
![image](images/result1.png)
