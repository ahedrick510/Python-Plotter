# Python-Plotter
## Easily plot data from one experiment or multiple related experiments

### Top Level Explanation:
`PlotterClass.py` allows the user to compare data from multiple trials on one python plot. Every trial must be the same length of time. There are two types of plots: standard 2D plot and twin-axis 2D plot. The user is prompted to select which files they want to plot and which column(s) from each file. Before the plot is displayed, the user is asked whether they want to save the data as a pickle file for plotting again later (will plot same data with whatever settings are listed in `Plotter.py`) and if they want to save the plot as a png. Plots and Pickles are saved in corresponding folders in the specified path from `foldername`.

### Instructions:
0. Install packages: `numpy`, `pandas`, `matplotlib`, `os`, `scipy`, and `pickle`. `scienceplots` recommended but not required.
1. Open `Plotter.py`.
2. Make sure all data you want to plot is in one folder, copy that folder name into variable `foldername`.
3. Make any desired edits to the plot format variables. Uncomment ONE of the functions at the bottom of `Plotter.py`.
4. Run code, follow instructions.

### Functions:
- `plot_pickle()`: Plots from a pickle file. Cannot reselect data, but you can change plot parameters.
- `plot_single_axis()`: Plots all selected data on a single axis. Up to 10 different colors.
- `plot_twin_axes()`: Plots selected data on two different axes. User selects which axis for each array. 
- `plot_bode(start_freq, end_freq, sampling_rate)`: Creates Bode plots on the same axes for user-selected input and output signal(s). Assumes linear chirp input. Optional smoothing function in `PlotterClass.py`.

### Notes:
1. Data must be in .csv or .xlsx files (doesn't matter which). Column titles must be in first row.
2. This code assumes each trial takes place over the same amount of time. However, the data columns do NOT need to be the same length (useful if data is recorded at different rates, including for bode plots). This means if you try to plot trials that take DIFFERENT amounts of time, some of the data WILL be plotted INCORRECTLY.
3. Plots are created in the `plot_data` function in the class, easily modifiable if you need to make any changes (transparency, line types, colors, etc.).

### Example:
![alt text](https://github.com/ahedrick510/Python-Plotter/blob/main/Sample%20Data/Plots/all-data-plotted.png "science plot example")
