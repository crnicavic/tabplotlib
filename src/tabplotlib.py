import matplotlib.pyplot as plt
import matplotlib.figure as fig

import tkinter
from tkinter import ttk

from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

class Tabplot:
    def __init__(self, window_name):
        # initialize the GUI
        self.root = tkinter.Tk()
        self.root.wm_title(window_name)

        # create the tabcontrol
        self.tabcontrol = tkinter.ttk.Notebook(self.root)
        # no idea what this does
        self.tabcontrol.pack(expand = 1, fill ="both")

        # freedom button
        button_quit = tkinter.Button(master=self.root, text="Quit", command=exit)
        button_quit.pack(side=tkinter.BOTTOM)

        self.tabs = []
        self.canvases = []

    def add_plot(self, plot_name, figure=None):
        new_tab = tkinter.Frame(self.tabcontrol)
        self.tabs.append(new_tab)
        self.tabcontrol.add(new_tab, text=plot_name)

        if figure is None:
            figure = plt.figure(plot_name)

        canvas = FigureCanvasTkAgg(figure, new_tab)
        toolbar = NavigationToolbar2Tk(canvas, self.root, pack_toolbar=False)
        toolbar.update()

        self.canvases.append(canvas)


    def show(self):
        for c in self.canvases:
            c.draw()
            c.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        tkinter.mainloop()

