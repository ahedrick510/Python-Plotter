###################################### 
# PLOTTER CLASS ######################
# BY: ALEXANDER HEDRICK ##############
# LAST UPDATED: 2025-09-19 ###########
######################################

# The goal of this class is to make plotting data as easy, quick, and customizable as possible,
# in particular for plotting recorded data vs data from video which might not match up in terms of length. 
# Because of this, there is a SINGLE x-axis for all data, so all data should be recorded over the same amount of time.
# The script will take care of any differences in length.

# The user points the class to a folder with data files (xlsx or csv) and then selects which files and columns to plot.
# The user can customize the plot with titles, axis labels, axis limits, and legend options

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import pickle

# Plotter class
class Plotter:
    def __init__(self, foldername, verbose, title, xlabel, ylabel1, ylabel2, xlimits, ylimits1, ylimits2, legend, figsize, title_fontsize, label_fontsize, tick_fontsize, legend_fontsize):
        self.foldername = foldername # folder name where the data is stored
        self.title = title # title of the plot
        self.xlabel = xlabel # x-axis label
        self.ylabel1 = ylabel1 # y-axis label
        self.ylabel2 = ylabel2 # y-axis label for second y-axis (if applicable)
        self.xlimits = xlimits # x-axis limits
        self.ylimits1 = ylimits1 # y-axis limits for first y-axis (if applicable)
        self.ylimits2 = ylimits2 # y-axis limits for second y-axis (if applicable)
        self.legend = legend # whether to show legend
        self.verbose = verbose # whether to print data information
        self.figsize = figsize # figure size
        self.title_fontsize = title_fontsize # title font size
        self.label_fontsize = label_fontsize # label font size
        self.tick_fontsize = tick_fontsize # tick font size
        self.legend_fontsize = legend_fontsize # legend font size

    def plot_pickle(self):
        # Load a previously saved pickle file containing a Plotter class instance
        # The folder in "foldername" should contain a "Pickles" subfolder with the pickle files.
        pickle_path = os.path.join(self.foldername, 'Pickles')
        pickles = [f for f in os.listdir(pickle_path) if f.endswith('.pkl')]

        for i, file in enumerate(pickles):
            print(f"Pickle {i}: {file}")
        pickle_idx = int(input("\nEnter index of pickle to load: "))
        with open(os.path.join(pickle_path, pickles[pickle_idx]), 'rb') as f:
            plotpickle = pickle.load(f)

        plotpickle.foldername = self.foldername # update foldername in case moved
        plotpickle.verbose = self.verbose # update verbose setting
        plotpickle.title = self.title # update title
        plotpickle.xlabel = self.xlabel # update xlabel
        plotpickle.ylabel1 = self.ylabel1 # update ylabel1
        plotpickle.ylabel2 = self.ylabel2 # update ylabel2
        plotpickle.xlimits = self.xlimits # update xlimits
        plotpickle.ylimits1 = self.ylimits1 # update ylimits1
        plotpickle.ylimits2 = self.ylimits2 # update ylimits2
        plotpickle.legend = self.legend # update legend setting
        plotpickle.figsize = self.figsize # update figsize
        plotpickle.title_fontsize = self.title_fontsize # update title fontsize
        plotpickle.label_fontsize = self.label_fontsize # update label fontsize
        plotpickle.tick_fontsize = self.tick_fontsize # update tick fontsize
        plotpickle.legend_fontsize = self.legend_fontsize # update legend fontsize


        plotpickle.plot_data()

    def select_data(self):
        # Creates a list of files in the given folder that are xlsx or csv files,
        # then prompts user to select which files to plot. Finally, the function
        # loads the selected files into pandas dataframes.

        # Make a list of data files
        path = self.foldername
        self.data_files = [f for f in os.listdir(path) if f.endswith('.xlsx') or f.endswith('.csv')]
        data_file_len = len(self.data_files)

        # Prompt user to select files
        print("Select files to plot (comma separated indices):")
        for i, file in enumerate(self.data_files):
            print(f"File {i}: {file}")

        temp_indices = input("\nEnter indices for data you want to plot, separated by commas: ")
        try:
            self.selected_indices = [int(x) for x in temp_indices.split(',')]
            if not all(0 <= idx < data_file_len for idx in self.selected_indices):
                print("Invalid indices. Please try again.")
        except ValueError:
            print("Invalid input. Please enter comma separated indices.")

        # Load the selected data files into dataframes
        self.selected_files = [self.data_files[i] for i in self.selected_indices]
        self.dataframes = {}
        for file in self.selected_files:
            name = file
            if file.endswith('.xlsx'):
                self.dataframes[name] = pd.read_excel(os.path.join(path, file))
            elif file.endswith('.csv'):
                self.dataframes[name] = pd.read_csv(os.path.join(path, file))

        self.selected_files = [self.data_files[i] for i in self.selected_indices]

        # If verbose, print head of each dataframe
        if self.verbose:
            for file, df in self.dataframes.items():
                print(f"\nData from {file}:")
                print(df.head())
            print("\n\n\n\n")

    def select_columns_single_axis(self):
        self.plot_type = 'single_axis'

        # Obtain x-axis (common to all plots)
        for i, key in enumerate(self.dataframes):
            print(f"Key {i}: {key}")
        self.frame_with_x = int(input("\nEnter key of dataframe to use for x-axis: "))
        x_key = list(self.dataframes.keys())[self.frame_with_x]

        # Prompt user to select x-axis from selected dataframe
        print(f"\nColumns in {x_key}:")
        for i, col in enumerate(self.dataframes[x_key].columns):
            print(f"Column {i}: {col}")
        self.x_idx = int(input("\nEnter index of column to plot on x-axis: "))
        self.x_data = self.dataframes[x_key].columns[self.x_idx]
        self.x_data_values = np.array(self.dataframes[x_key][self.x_data])

        # Prompt user to select y-axis from each dataframe
        self.columns = {}
        for file, df in self.dataframes.items():
            print(f"\nColumns in {file}:")
            for i, col in enumerate(df.columns):
                print(f"Column {i}: {col}")
            y_idx = int(input(f"\nEnter index of column to plot on y-axis for {file}: "))
            label = input(f"\nEnter label for {file} (or press Enter to use ylabel name): ")
            self.columns[file] = (df.columns[y_idx], label if label else self.ylabel1)

        if self.verbose:
            print("\nSelected columns for plotting:")
            for file, (y_col,lab) in self.columns.items():
                print(f"{file}: y -> {y_col}, label -> {lab}")
            print("\n\n\n\n")

    def select_columns_twin_axes(self):
        # Prompts user to select which columns to plot on x and y axes for twin axes
        self.plot_type = 'twin_axes'

        # Obtain x-axis (common to both plots)
        for i, key in enumerate(self.dataframes):
            print(f"Key {i}: {key}")
        self.frame_with_x = int(input("\nEnter key of dataframe to use for x-axis: "))
        x_key = list(self.dataframes.keys())[self.frame_with_x]

        # Prompt user to select x-axis from selected dataframe
        print(f"\nColumns in {x_key}:")
        for i, col in enumerate(self.dataframes[x_key].columns):
            print(f"Column {i}: {col}")
        self.x_idx = int(input("\nEnter index of column to plot on x-axis: "))
        self.x_data = self.dataframes[x_key].columns[self.x_idx]
        self.x_data_values = np.array(self.dataframes[x_key][self.x_data])

        # Prompt user to select y-axis from each dataframe
        self.columns = {}
        for file, df in self.dataframes.items():
            print(f"\nColumns in {file}:")
            for i, col in enumerate(df.columns):
                print(f"Column {i}: {col}")

            # x_idx = int(input(f"\nEnter index of column to plot on x-axis for {file}: "))
            y_idx = int(input(f"\nEnter index of column to plot on y-axis for {file}: "))
            y_axis = int(input(f"\nIs this y-axis for the first or second axis? (Enter 1 or 2): "))
            label = input(f"\nEnter label for {file} (or press Enter to use ylabel name): ")
            self.columns[file] = (df.columns[y_idx], y_axis, label if label else (self.ylabel1 if y_axis == 1 else self.ylabel2))

        if self.verbose:
            print("\nSelected columns for plotting:")
            for file, (y_col,y_ax,lab) in self.columns.items():
                print(f"{file}: y -> {y_col}, y-axis {y_ax}, label -> {lab}")
            print("\n\n\n\n")

    def plot_data(self):


        # Plots the selected data with given customizations.
        plt.style.use('seaborn-talk')
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']


        if self.plot_type == 'twin_axes':
            if not self.figsize:
                self.figsize = (10, 6)
            fig, ax1 = plt.subplots(figsize=self.figsize)
            ax2 = ax1.twinx()

            for i, (file, df) in enumerate(self.dataframes.items()):
                y_col = self.columns[file][0]
                y_axis = self.columns[file][1]
                label = self.columns[file][2]
                if y_axis == 1:
                    ax1.plot(np.linspace(self.x_data_values[0],self.x_data_values[-1],len(df[y_col])), df[y_col], label=label, color=f'C{i}', alpha=1)
                else:
                    ax2.plot(np.linspace(self.x_data_values[0],self.x_data_values[-1],len(df[y_col])), df[y_col], label=label, color=f'C{i+2}', alpha=0.7)

            if self.title:
                if self.title_fontsize is False:
                    ax1.set_title(self.title)
                else:
                    ax1.set_title(self.title, fontsize=self.title_fontsize)
            if self.label_fontsize is False:
                ax1.set_xlabel(self.xlabel)
                ax1.set_ylabel(self.ylabel1)
                ax2.set_ylabel(self.ylabel2)
            else:
                ax1.set_xlabel(self.xlabel, fontsize=self.label_fontsize)
                ax1.set_ylabel(self.ylabel1, fontsize=self.label_fontsize)
                ax2.set_ylabel(self.ylabel2, fontsize=self.label_fontsize)
            if self.tick_fontsize is False:
                ax1.tick_params(axis='x')  # Change x-axis tick label font size
                ax1.tick_params(axis='y')  # Change y-axis tick label font size
                ax2.tick_params(axis='y')  # Change y-axis tick label font size
            else:
                ax1.tick_params(axis='x', labelsize=self.tick_fontsize)  # Change x-axis tick label font size
                ax1.tick_params(axis='y', labelsize=self.tick_fontsize)  # Change y-axis tick label font size
                ax2.tick_params(axis='y', labelsize=self.tick_fontsize)  # Change y-axis tick label font size
            if self.xlimits:
                ax1.set_xlim(self.xlimits)
            if self.ylimits1:
                ax1.set_ylim(self.ylimits1)
            if self.ylimits2:
                ax2.set_ylim(self.ylimits2)
            if self.legend:
                if self.legend_fontsize is False:
                    ax1.legend(loc='upper left')
                    ax2.legend(loc='lower right')
                else:
                    ax1.legend(loc='upper left', fontsize=self.legend_fontsize)
                    ax2.legend(loc='lower right', fontsize=self.legend_fontsize)
            ax1.grid()

            self.save_data_plot()
            plt.show()


        else:
            if not self.figsize:
                self.figsize = (10, 6)
            plt.figure(figsize=self.figsize)
            for i, (file, df) in enumerate(self.dataframes.items()):
                y_col = self.columns[file][0]
                label = self.columns[file][1]
                plt.plot(np.linspace(self.x_data_values[0],self.x_data_values[-1],len(df[y_col])), df[y_col], color=colors[i], alpha=1, label=label)

            if self.title:
                if self.title_fontsize is False:
                    plt.title(self.title)
                else:
                    plt.title(self.title, fontsize=self.title_fontsize)
            if self.label_fontsize is False:
                plt.xlabel(self.xlabel)
                plt.ylabel(self.ylabel1)
            else:
                plt.xlabel(self.xlabel, fontsize=self.label_fontsize)
                plt.ylabel(self.ylabel1, fontsize=self.label_fontsize)
            if self.tick_fontsize is False:
                plt.tick_params(axis='x')  # Change x-axis tick label font size
                plt.tick_params(axis='y')  # Change y-axis tick label font size
            else:
                plt.tick_params(axis='x', labelsize=self.tick_fontsize)  # Change x-axis tick label font size
                plt.tick_params(axis='y', labelsize=self.tick_fontsize)  # Change y-axis tick label font size
            if self.xlimits:
                plt.xlim(self.xlimits)
            if self.ylimits1:
                plt.ylim(self.ylimits1)
            if self.legend:
                if self.legend_fontsize is False:
                    plt.legend()
                else:
                    plt.legend(fontsize=self.legend_fontsize)
            plt.grid()

            self.save_data_plot()
            plt.show()

    def save_data_plot(self):
        # Asks user if they want to save the data used for plotting to a pickle file AND/OR save the plot as an image file.
        save_data = input("Do you want to pickle the settings to easily plot later? (y/n): ")
        if save_data.lower() == 'y':
            # check if there is a folder called "Pickles" in the given folder, if not create it
            if not os.path.exists(self.foldername + '\\Pickles'):
                os.makedirs(self.foldername + '\\Pickles')

            pickle_name = input("Enter name for pickle file (without .pkl extension, NO SPACES): ")
            with open(self.foldername + '\\Pickles\\' + pickle_name + '.pkl', 'wb') as f:
                pickle.dump(self, f)
            print(f"Class pickled!")

        save_plot = input("Do you want to save the plot as an image file? (y/n): ")
        if save_plot.lower() == 'y':
            # check if there is a folder called "Plots" in the given folder, if not create it
            if not os.path.exists(self.foldername + '\\Plots'):
                os.makedirs(self.foldername + '\\Plots')
            plot_name = input("Enter name for figure (or hit enter to save as title of plot): ")
            if plot_name:
                plt.savefig(self.foldername + '\\Plots\\' + plot_name + '.png',bbox_inches='tight')
                print(f"Plot saved to {self.foldername} as {plot_name+ '.png'}")
            else:
                plt.savefig(self.foldername + '\\Plots\\' + self.title + '.png',bbox_inches='tight')
                print(f"Plot saved to {self.foldername} as {self.title + '.png'}")

