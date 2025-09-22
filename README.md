# Python-Plotter
## Make plotting data from multiple related experiments on the same plot as painless as possible

### Top Level Explanation:
`PlotterClass.py` allows the user to compare data from multiple trials on one python plot. Every trial must be the same length of time. There are two types of plots: standard 2D plot and twin-axis 2D plot. The user is prompted to select which files they want to plot and which column(s) from each file. Before the plot is displayed, the user is asked whether they want to save the data as a pickle file for plotting again later (will plot same data with whatever settings are listed in `Plotter.py`) and if they want to save the plot. Plots and Pickles are saved corresponding folders in the specified path from `foldername`.

### Instructions:
0. Install required packages using `pip`: `numpy`, `pandas`, `matplotlib`, `os`, `pickle`, and `scienceplots`
1. Open `Plotter.py`
2. Make sure all data you want to plot is in one folder, copy that folder name into variable `foldername`
3. Make any desired edits to the plot format variables
4. Run code, follow instructions

### Notes:
1. Data must be in .csv or .xlsx files (doesn't matter which). Column titles should be in first row.
2. This code assumes each trial takes place over the same amount of time. However, the data columns do NOT need to be the same length (useful if data is recorded at different rates). This means if you try to plot trials that last different amounts of time, some of the data will be plotted incorrectly.
3. Plots are created in the `plot_data` function in the class, easily modifiable if you need to make any changes (transparency, line types, colors, etc.)
