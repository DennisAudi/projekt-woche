from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
temperatures = [10, 22.455, 23.941, 23.987, 22.19, 23.806, 23.173, 23.308, 23.435, 23.924, 23.004, 22.784, 23.76, 22.877, 23.922, 23.368, 23.303, 22.318, 22.027, 23.373, 22.652, 22.372, 23.968, 23.295, 23.514, 23.743, 23.716, 22.608, 23.356, 22.307, 22.09, 23.286, 22.091, 23.545, 23.551, 23.874, 23.517, 23.842, 22.858, 23.248, 23.918, 22.879, 23.141, 22.493, 23.173, 22.411, 23.895, 23.204, 23.549, 22.561, 22.965, 23.614, 22.941, 23.785, 22.542, 22.549, 23.366, 22.78, 22.104, 23.912, 22.596, 23.197, 23.057, 23.22, 23.623, 23.834, 23.046, 23.125, 23.619, 23.108, 23.936, 23.864, 23.75, 22.969, 23.666, 22.581, 23.189, 22.101, 23.536, 23.055, 22.148, 22.181, 23.468, 22.173, 22.79, 22.817, 22.566, 23.637, 23.931, 23.81, 23.686, 23.556, 23.047, 22.173, 22.485, 23.78, 22.43, 23.4, 22.619, 23.381, 22.988, 23.719, 22.509, 22.036, 23.333, 23.46, 22.054, 22.63, 22.239, 22.005, 23.984, 23.328, 22.162, 23.33, 22.604, 22.835, 22.772, 23.107, 22.116, 23.329, 22.74, 23.545, 22.842, 22.081, 23.356, 22.783, 23.355, 23.355, 23.506, 23.532, 23.623, 22.007, 22.394, 22.054, 22.884, 23.598, 22.799, 22.72, 23.506, 23.843, 23.98, 23.925, 22.453, 22.499, 23.476, 22.625, 22.18, 23.168, 22.906, 22.66, 23.891, 23.388, 23.565, 22.889, 22.165, 23.776, 23.546, 23.511, 23.607, 22.417, 23.074, 22.315, 22.407, 22.627, 23.392, 23.186, 22.484, 23.012, 22.87, 23.91, 22.923, 22.618, 22.562, 22.03, 23.431, 23.56, 22.844, 23.582, 22.853, 22.666, 23.3, 23.324, 22.457, 22.183, 23.484, 23.97, 22.002, 22.953, 22.369, 23.873, 23.639, 23.27, 22.002, 22.953, 22.369, 23.873, 23.639, 23.27, 22.455, 23.941, 23.987, 22.19, 23.806, 23.173, 23.308, 23.435, 23.924, 23.004, 22.784, 23.76, 22.877, 23.922, 23.368, 23.303, 22.318, 22.027, 23.373, 22.652, 22.372, 23.968, 23.295, 23.514, 23.743, 23.716, 22.608, 23.356, 22.307, 22.09, 23.286, 22.091, 23.545, 23.551, 23.874, 23.517, 23.842, 22.858, 23.248, 23.918, 22.879, 23.141, 22.493, 23.173, 22.411, 23.895, 23.204, 23.549, 22.561, 22.965, 23.614, 22.941, 23.785, 22.542, 22.549, 23.366, 22.78, 22.104, 23.912, 22.596, 23.197, 23.057, 23.22, 23.623, 23.834, 23.046, 23.125, 23.619, 23.108, 23.936, 23.864, 23.75, 22.969, 23.666, 22.581, 23.189, 22.101, 23.536, 23.055, 22.148, 22.181, 23.468, 22.173, 22.79, 22.817, 22.566, 23.637, 23.931, 23.81, 23.686, 23.556, 23.047, 22.173, 22.485, 23.78, 22.43, 23.4, 22.619, 23.381, 22.988, 23.719, 22.509, 22.036, 23.333, 23.46, 22.054, 22.63, 22.239, 22.005, 23.984, 23.328, 22.162, 23.33, 22.604, 22.835, 22.772, 23.107, 22.116, 23.329, 22.74, 23.545, 22.842, 22.081, 23.356, 22.783, 23.355, 23.355, 23.506, 23.532, 23.623, 22.007, 22.394, 22.054, 22.884, 23.598, 22.799, 22.72, 23.506, 23.843, 23.98, 23.925, 22.453, 22.499, 23.476, 22.625, 22.18, 23.168, 22.906, 22.66, 23.891, 23.388, 23.565, 22.889, 22.165, 23.776, 23.546, 23.511, 23.607, 22.417, 23.074, 22.315, 22.407, 22.627, 23.392, 23.186, 22.484, 23.012, 22.87, 23.91, 22.923, 22.618, 22.562, 22.03, 23.431, 23.56, 22.844, 23.582, 22.853, 22.666, 23.3, 23.324, 22.457, 22.183, 23.484, 23.97, 22.002, 22.953, 22.369, 23.873, 23.639, 30]
# plot function is created for
# plotting the graph in
# tkinter window
def plot():
    # the figure that will contain the plot
    fig = Figure(figsize=(5, 5),
                 dpi=100)
    # list of squares
    y = [i for i in temperatures]
    # adding the subplot
    plot1 = fig.add_subplot(111)
    # plotting the graph
    plot1.plot(y)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=window)
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
# the main Tkinter window
window = Tk()
# setting the title
window.title('Plotting in Tkinter')
# dimensions of the main window
window.geometry("500x500")
# button that displays the plot
ttk.Button(text="Quit", command=window.destroy).pack()
# place the button
# in main window
ttk.Button(master=window, command=plot, text="Plot").pack()
# run the gui
window.mainloop()
