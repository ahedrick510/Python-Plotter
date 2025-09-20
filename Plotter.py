from PlotterClass import Plotter

# Plotter code
foldername = r"C:\Users\aimrl\Documents\GitHub\Python-Plotter\Sample Data"
verbose = False
title = "Example Plot"
xlabel = "Time (s)"
ylabel1 = "Y Label 1"
ylabel2 = "Y Label 2"
xlimits = [0, 1]
ylimits1 = False
ylimits2 = False
legend = True

# False = default sizes
figsize = False
title_fontsize = False
label_fontsize = False
tick_fontsize = False
legend_fontsize = False

# Create instance of class
PlotData = Plotter(foldername, verbose, title, xlabel, ylabel1, ylabel2, xlimits=xlimits, ylimits1=ylimits1, ylimits2=ylimits2, legend=legend, 
                   figsize=figsize, title_fontsize=title_fontsize, label_fontsize=label_fontsize, tick_fontsize=tick_fontsize, legend_fontsize=legend_fontsize)

# Run this if you want to plot from a pickle file
PlotData.plot_pickle()

# # Run these lines if you want to select data and plot from scratch
# PlotData.select_data()
# PlotData.select_columns_twin_axes()
# PlotData.plot_data()

# # Run these lines if you want to select data and plot from scratch, single y-axis
# PlotData.select_data()
# PlotData.select_columns_single_axis()
# PlotData.plot_data()