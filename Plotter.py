from PlotterClass import Plotter

# Plotter code
foldername = r"C:\Users\aimrl\Documents\GitHub\Python-Plotter\Sample Data"
# plotstyle = 'seaborn-talk'  # 'seaborn-talk' or 'science' or 'science-ieee'
plotstyle = 'science'
verbose = False
title = "Sample Plot"
xlabel = "X Label"
ylabel1 = "Y Label"
ylabel2 = "Y Label 2"
xlimits = [0, 1]
ylimits1 = False
ylimits2 = False
legend = True

# False = default sizes
figsize = (3.5, 2.625) # figsize for science style
# figsize = False # default figsize
title_fontsize = False
label_fontsize = False
tick_fontsize = False
legend_fontsize = False

# Create instance of class
PlotData = Plotter(foldername, plotstyle, verbose, title, xlabel, ylabel1, ylabel2, xlimits=xlimits, ylimits1=ylimits1, ylimits2=ylimits2, legend=legend, 
                   figsize=figsize, title_fontsize=title_fontsize, label_fontsize=label_fontsize, tick_fontsize=tick_fontsize, legend_fontsize=legend_fontsize)

# Run ONE of the following three lines
# PlotData.plot_pickle()        # run this if you want to plot from a pickle file
# PlotData.plot_twin_axes()     # run this line for twin y-axes
PlotData.plot_single_axis()     # run this line for single y-axis

