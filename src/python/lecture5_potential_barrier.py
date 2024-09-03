import sys
import numpy as np
from vispy import app, scene
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QSlider, QLabel, QWidget
from PyQt5.QtCore import Qt

# Initial parameters
N = 2000  # Number of points
x_lim = [-10, 10]
y_lim = [-2., 2.]
x = np.linspace(x_lim[0], x_lim[1], N)

V0 = 10.0 # Potential barrier height
E = 2.0 # Energy of the particle
a = 5.0 # Barrier width

t = 0.0
V0_init = V0
E_init = E

def scattering_state(x, E, V0, a):
    k = np.sqrt(2 * E)
    A = 1.0
    if E > V0:
        psi = A * np.exp(1j * k * x)
        # k2 = np.sqrt(2 * (E - V0))
        # psi = np.piecewise(x, [x < 0.0, (x >= 0.0) & (x <= a), x > a],
        #                     [lambda x: A*np.exp(k1 * x) + A*np.exp(-k1 * x),
        #                         lambda x: A*np.exp(k1 * x) + A*np.exp(-k1 * x),
        #                         lambda x: A*np.exp(k2 * x)])
    else:
        kappa = np.sqrt(2 * (V0 - E))
        M = np.array([[-1, 1, 1, 0], 
                      [1j*k, kappa, -kappa, 0], 
                      [0, np.exp(kappa*a), np.exp(-kappa*a), -np.exp(1j*k*a)], 
                      [0, kappa*np.exp(kappa*a), -kappa*np.exp(-kappa*a), -1j*k*np.exp(1j*k*a)]])
                     
        v = np.array([A, 1j*k*A, 0, 0])
        sol = np.linalg.solve(M, v)
        B, C, D, F= sol


        psi = np.piecewise(x, [x < 0.0, (x >= 0.0) & (x <= a), x > a],
                            [lambda x: A*np.exp(1j * k * x) + B*np.exp(-1j * k * x),
                                lambda x: C*np.exp(kappa * x) + D*np.exp(-kappa * x),
                                lambda x: F*np.exp(1j*k * x)])
        
    return psi
    
# Vertex positions of data to draw
pos = np.zeros((N, 2), dtype=np.float32)
pos[:, 0] = x
pos[:, 1] = scattering_state(x, E, V0, a).real

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
current_E = E_init
current_V0 = V0_init

# Update function to animate the plot
def update(ev):
    global t, pos, current_E, current_V0, line
    t += 1.0
    pos[:, 1] = scattering_state(x, current_E, current_V0, a).real
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
        self.E_slider = QSlider(Qt.Horizontal)
        self.E_slider.setMinimum(100)  # Scaling factor: 10
        self.E_slider.setMaximum(3000)  # Scaling factor: 10
        self.E_slider.setValue(int(E_init * 100))
        self.E_slider.setTickInterval(100)
        self.E_slider.setTickPosition(QSlider.TicksBelow)
        self.E_slider.valueChanged.connect(self.update_E)
        layout.addWidget(QLabel(r'E'))
        layout.addWidget(self.E_slider)

        # T slider (scaled to integer for slider control)
        self.V0_slider = QSlider(Qt.Horizontal)
        self.V0_slider.setMinimum(1000)  # Scaling factor: 10
        self.V0_slider.setMaximum(30000)  # Scaling factor: 10
        self.V0_slider.setValue(int(V0_init * 10))
        self.V0_slider.setTickInterval(1000)
        self.V0_slider.setTickPosition(QSlider.TicksBelow)
        self.V0_slider.valueChanged.connect(self.update_V0)
        layout.addWidget(QLabel(r'V0'))
        layout.addWidget(self.V0_slider)

    def update_E(self, value):
        global current_E
        current_E = value / 10.0  # Scaling back to float

    def update_V0(self, value):
        global current_V0
        current_V0 = value / 10.0  # Scaling back to float

# Create a PyQt5 application
if __name__ == '__main__':
    app_qt = app.use_app('pyqt5')
    win = MainWindow()
    win.setWindowTitle("Wave Function Animation with Sliders")
    win.show()
    app.run()
    