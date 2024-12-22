import numpy as np
import pyvista as pv
from matplotlib import cm
                                  
def plotter(crystals) :
   
    plotter = pv.Plotter()
    
    
    
    
    num_crystals = len(crystals)
    
    colormap = cm.get_cmap("Accent")  # Or any other categorical colormap
 

    # Loop through each crystal
    for i, crystal in enumerate(crystals):
        
        points_channel = pv.PolyData(crystal.vertices)

        
        color = colormap(i / num_crystals)  # Normalize index for colormap
        color_rgb = color[:3]  # Extract RGB 

        color_rgb = np.array(color_rgb)

        # Create an array where each vertex gets the same RGB color
        colors_channel = np.tile(color_rgb, (crystal.vertices.shape[0], 1))  

        # Assign the color array to the points as scalars (PyVista needs 3D color vectors for RGB)
        points_channel.point_data["colors"] = colors_channel

        # Add the points to the plotter,
        plotter.add_points(
            points_channel,
            scalars="colors",  # Use the 'colors' scalar field for coloring
            render_points_as_spheres=True,
            point_size=10,
            show_scalar_bar=False
        )

        
        for line in crystal.edges:
            line_pts = np.array(line)  # on Edge coordinates not indices
            line_poly = pv.PolyData(line_pts)
            line_poly.lines = np.array([[2, 0, 1]])  # Defines a line between points 0 and 1
            plotter.add_mesh(line_poly, color=color_rgb, line_width=3)  # Use the same color for edges
      
    # Set legend 
    legend_offset_y = 200  
    for i in range(num_crystals):
        label_position = (0, legend_offset_y - i * 20)  # Adjusting Y more significantly to prevent overlap
        color = colormap(i / num_crystals)[:3]  # Get the RGB color for the skeleton
        plotter.add_text(f"  Crystal {i + 1}", position=label_position, color=color, font_size=12)



    




    # Add axes to the plotter
    plotter.add_axes()

    # Set the view and display
    plotter.view_xy()
    plotter.show()    

