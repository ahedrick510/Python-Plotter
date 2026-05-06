# Python-Plotter
## Easily plot data from one experiment or multiple related experiments

### Top Level Explanation:
`PlotterClass.py` allows the user to compare data from multiple trials on one python plot. Every trial must be the same length of time. There are three types of plots: standard 2D plot, twin-axis 2D plot, and bode plot. The user is prompted to select which files they want to plot and which column(s) from each file. The user is also asked whether they want to save the data as a pickle file for plotting again later (will plot same data with new plot settings) and if they want to save the plot as a png. Plots and Pickles are saved in corresponding folders in the specified path from `foldername`.

### New Instructions:
0. Install packages: `numpy`, `pandas`, `matplotlib`, `os`, `scipy`, `pickle`, and `tkinter`. `scienceplots` recommended but not required.
1. Navigate to the folder which contains both `PlotterClass.py` and `PlotterGUI.py`. Run `PlotterGUI.py` in the terminal and follow the prompts. See Functions below for list of possible graphs you can create.

### Functions:
- `plot_pickle()`: Plots from a pickle file. Cannot reselect data, but you can change plot visualization parameters.
- `plot_single_axis()`: Plots all selected data on a single axis. Up to 10 different colors.
- `plot_twin_axes()`: Plots all selected data on two different axes. User selects which axis for each array. 
- `plot_bode(start_freq, end_freq, sampling_rate)`: Creates Bode plots on the same axes for user-selected input and output signal(s). Smoothing function in `PlotterClass.py` can be commented out.

### Notes:
1. Data must be in .csv or .xlsx or .mat files (doesn't matter which). Column titles must be in first row for .csv and .xlsx. Struct with 1xn or nx1 doubles for .mat files.
2. This code assumes each trial takes place over the same amount of time. However, the data columns do NOT need to be the same length (useful if data is recorded at different rates, including for bode plots). This means if you try to plot trials that take DIFFERENT amounts of time, some of the data WILL be plotted INCORRECTLY.
3. Plots are created in the `plot_data` function in the class, easily modifiable if you need to make any changes (transparency, line types, colors, etc.).

### GUI + Sample Plot:

<p align="center">
  <img src="https://github.com/ahedrick510/Python-Plotter/blob/main/Sample%20Data/Plots/pyplotter.png" width="45%" />
  <img src="https://github.com/ahedrick510/Python-Plotter/blob/main/Sample%20Data/Plots/all-data-plotted.png" width="45%" />
</p>
