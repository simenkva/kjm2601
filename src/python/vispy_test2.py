import sys
import numpy as np
from vispy import app, scene
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QSlider, QLabel, QWidget
from PyQt5.QtCore import Qt

# Initial parameters
N = 2000  # Number of points
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

# PyQt5 window with sliders
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main widget
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # Layout for the sliders
        layout = QVBoxLayout(self.main_widget)

        # Lambda slider (scaled to integer for slider control)
        self.lamb_slider = QSlider(Qt.Horizontal)
        self.lamb_slider.setMinimum(100)  # Scaling factor: 10
        self.lamb_slider.setMaximum(3000)  # Scaling factor: 10
        self.lamb_slider.setValue(int(lamb_init * 10))
        self.lamb_slider.setTickInterval(100)
        self.lamb_slider.setTickPosition(QSlider.TicksBelow)
        self.lamb_slider.valueChanged.connect(self.update_lambda)
        layout.addWidget(QLabel(r'$\lambda$'))
        layout.addWidget(self.lamb_slider)

        # T slider (scaled to integer for slider control)
        self.T_slider = QSlider(Qt.Horizontal)
        self.T_slider.setMinimum(1000)  # Scaling factor: 10
        self.T_slider.setMaximum(30000)  # Scaling factor: 10
        self.T_slider.setValue(int(T_init * 10))
        self.T_slider.setTickInterval(1000)
        self.T_slider.setTickPosition(QSlider.TicksBelow)
        self.T_slider.valueChanged.connect(self.update_T)
        layout.addWidget(QLabel('T'))
        layout.addWidget(self.T_slider)

    def update_lambda(self, value):
        global current_lambda
        current_lambda = value / 10.0  # Scaling back to float

    def update_T(self, value):
        global current_T
        current_T = value / 10.0  # Scaling back to float

# Create a PyQt5 application
if __name__ == '__main__':
    app_qt = app.use_app('pyqt5')
    win = MainWindow()
    win.setWindowTitle("Wave Function Animation with Sliders")
    win.show()
    app.run()
    