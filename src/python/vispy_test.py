import sys
import numpy as np
from vispy import app, scene
from ipywidgets import interact, FloatSlider
from IPython.display import display

# Initial parameters
N = 200  # Number of points
x_lim = [50., 750.]
y_lim = [-2., 2.]
x = np.linspace(x_lim[0], x_lim[1], N)

lamb_init = 100.0  # Initial wavelength
T_init = 1000.0  # Initial period
t = 0.0  # Initial time

# Vertex positions of data to draw
pos = np.zeros((N, 2), dtype=np.float32)
pos[:, 0] = x
pos[:, 1] = np.sin(2 * np.pi * (x / lamb_init))

# Color array
color = np.ones((N, 4), dtype=np.float32)
color[:, 0] = np.linspace(0, 1, N)
color[:, 1] = color[::-1, 0]

# Create the VisPy canvas
canvas = scene.SceneCanvas(keys='interactive', show=True)
grid = canvas.central_widget.add_grid(spacing=0)

viewbox = grid.add_view(row=0, col=1, camera='panzoom')

# Add some axes
x_axis = scene.AxisWidget(orientation='bottom')
x_axis.stretch = (1, 0.1)
grid.add_widget(x_axis, row=1, col=1)
x_axis.link_view(viewbox)
y_axis = scene.AxisWidget(orientation='left')
y_axis.stretch = (0.1, 1)
grid.add_widget(y_axis, row=0, col=0)
y_axis.link_view(viewbox)

# Add a line plot inside the viewbox
line = scene.Line(pos, color, parent=viewbox.scene)

# Auto-scale to see the whole line
viewbox.camera.set_range()

# Global variables to store current lambda and T values
current_lambda = lamb_init
current_T = T_init

# Update function to animate the plot
def update(ev):
    global t, pos, current_lambda, current_T, line
    t += 1.0
    pos[:, 1] = np.sin(2 * np.pi * (x / current_lambda - t / current_T))
    line.set_data(pos=pos, color=color)

# Timer to continuously update the plot
timer = app.Timer()
timer.connect(update)
timer.start(0)

# Interactivity with sliders
def update_params(lamb, T):
    global current_lambda, current_T
    current_lambda = lamb
    current_T = T

# Interactive sliders for lambda and T
lamb_slider = FloatSlider(min=10.0, max=300.0, step=1.0, value=lamb_init, description=r'$\lambda$')
T_slider = FloatSlider(min=100.0, max=3000.0, step=10.0, value=T_init, description='T')

# Set up the interactive sliders
interact(update_params, lamb=lamb_slider, T=T_slider)

# Show the canvas
if __name__ == '__main__' and sys.flags.interactive == 0:
    app.run()
    