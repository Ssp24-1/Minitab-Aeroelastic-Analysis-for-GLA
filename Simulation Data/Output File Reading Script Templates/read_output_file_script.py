import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import make_interp_spline

# from pymatreader import read_mat
dyn_press = 2128598.72082399
# Initialize lists to collect x, y, z coordinates
x_coords = []
y_coords = []
z_coords = []
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Load the NumPy arrays from the .npz file
data = np.load('numpy_arrays.npz')

# Access the arrays
numpy_arrays = [data[key] for key in data]

# # Print the number of arrays
# # print(f"Number of arrays: {len(numpy_arrays)}")


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')


# # Iterate over every 5th NumPy array
# for i in range(0, 70):  # Step by 5
#     array = numpy_arrays[i]
    
#     # Ignore the 1st column
#     array = array[:, 1:]
    
#     # Select multiples of the 6th value starting from the 2nd value
#     selected_values = array[2::6, :]
    
#     # Remove the first x value
#     selected_values = selected_values[1:, :]
    
#     # Create x and y coordinates
#     x = np.arange(selected_values.shape[0])
#     y = np.full_like(x, i + 70)  # Use the index of the array as the y-coordinate, starting from 70
    
#     # Fit a high-order polynomial (e.g., 5th order) to the data
#     for j in range(selected_values.shape[1]):
#         ax.plot(x, y, selected_values[:, j], label=f'Array {i + 70}, Column {j}')
    
#     # Print the sum of all the values in the selected array
#     array_sum = np.sum(selected_values)
#     print(f'Sum of all values in array {i + 70}: {array_sum}')
#     print(f'Sum of all values in array {i + 70} multiplied by dyn_press: {array_sum / dyn_press}')

# ax.view_init(elev=30, azim=60)  # Adjust the elevation and azimuthal angles as needed

# ax.set_title('3D Plot of Multiples of 6th Value Starting from 2nd Value')
# ax.set_xlabel('Index')
# ax.set_ylabel('Array Index')
# ax.set_zlabel('Value')
# plt.show()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# fig, ax = plt.subplots()

# # Iterate over every 5th NumPy array
# for i in range(0, 37, 18):  # Step by 18
#     array = numpy_arrays[i]
    
#     # Ignore the 1st column
#     array = array[:, 1:]
    
#     # Select multiples of the 6th value starting from the 2nd value
#     selected_values = array[2::6, :]
    
#     # Remove the first x value
#     selected_values = selected_values[0:, :]
    
#     # Create x coordinates
#     x = np.arange(selected_values.shape[0])
    
#     # Plot each column of the selected values
#     for j in range(selected_values.shape[1]):
#         ax.plot(x/44, selected_values[:, j])
    
#     # Print the sum of all the values in the selected array
#     array_sum = np.sum(selected_values)
#     print(f'Sum of all values in array {i + 70}: {array_sum}')
#     print(f'Sum of all values in array {i + 70} multiplied by dyn_press: {array_sum / dyn_press}')

# ax.set_title('Spanwise Loads during Minitab Deploy + Stow (Gust G1)')
# ax.set_xlabel('Spanwise Position (y/b)')
# ax.set_ylabel('Force (N)')
# ax.legend(['Clean Wing', 'Minitab Peak Minima', 'Steady State after Deployment'])
# ax.grid(True)
# plt.show()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
fig, ax = plt.subplots()

# Define the labels for the plots
# labels = ["Steady State before Deployment", "Peak Load Reduction", "Steady State after Deployment"]
idx_0 = []
idx_5 = []
idx_10 = []
idx_15 = []
idx_20 = []
idx_25 = []
idx_30 = []
idx_35 = []
idx_40 = []

# Iterate over the specified NumPy arrays
for i in range(0, 150):  # Indices of the arrays
    array = numpy_arrays[i]
    
    # Ignore the 1st column
    array = array[:, 1:]
    
    # Select multiples of the 6th value starting from the 2nd value
    selected_values0 = array[0::6, :]       # X force
    selected_values1 = array[1::6, :]       # Y force
    selected_values2 = array[2::6, :]       # Z force
    
    selected_values = np.sqrt(selected_values0**2 + selected_values1**2 + selected_values2**2)
    
    # Remove the first 4 x values
    selected_values = selected_values[0:, :]
    
    # Create x and y coordinates
    x = np.arange(selected_values.shape[0]) + 0
    x_normalized = x * 100 / x.max()

    y = np.full_like(x, i + 119)  # Use the index of the array as the y-coordinate, starting from 70
    
    # Plot the selected values in 2D
    for j in range(selected_values.shape[1]):
        idx_0.append(selected_values[0, j])
        idx_5.append(selected_values[5, j])
        idx_10.append(selected_values[10, j])
        idx_15.append(selected_values[15, j])
        idx_20.append(selected_values[20, j])
        idx_25.append(selected_values[25, j])
        idx_30.append(selected_values[30, j])
        idx_35.append(selected_values[35, j])
        idx_40.append(selected_values[40, j])

# Read the CSV files
idx_0 = pd.read_csv('idx_0.csv', header=None).values.flatten()
idx_5 = pd.read_csv('idx_5.csv', header=None).values.flatten()
idx_10 = pd.read_csv('idx_10.csv', header=None).values.flatten()
idx_15 = pd.read_csv('idx_15.csv', header=None).values.flatten()
idx_20 = pd.read_csv('idx_20.csv', header=None).values.flatten()
idx_25 = pd.read_csv('idx_25.csv', header=None).values.flatten()
idx_30 = pd.read_csv('idx_30.csv', header=None).values.flatten()
idx_35 = pd.read_csv('idx_35.csv', header=None).values.flatten()
idx_40 = pd.read_csv('idx_40.csv', header=None).values.flatten()

# Plot the data from the CSV files
fig, ax = plt.subplots()
x = np.arange(len(idx_10)) + 20

ax.plot(x/100, idx_10, label='25% Span')
ax.plot(x/100, idx_20, label='47% Span')
ax.plot(x/100, idx_25, label='59% Span')
ax.plot(x/100, idx_30, label='70% Span')
ax.plot(x/100, idx_35, label='82% Span')
ax.plot(x/100, idx_40, label='93% Span')

# Increase the size of the legend, axis labels, and numbers
ax.legend(loc='upper right', fontsize=12)
ax.set_xlabel('Time (s)', fontsize=16)
ax.set_ylabel('Sectional Lift Force (N)', fontsize=18)
ax.tick_params(axis='both', which='major', labelsize=18)

# Draw a vertical orange line at X = 0.2
ax.axvline(x=0.2, color='black', linestyle='--', linewidth=1)
plt.text(0.15, 15000, f'Minitab Deployment', color='red', va='center', ha='left', rotation='vertical', fontsize=14)

# Add grid
ax.grid(True)

plt.show()

# # ========================================================================================================
# fig, ax = plt.subplots()

# # Define the labels for the plots
# # labels = ["Steady State before Deployment", "Peak Load Reduction", "Steady State after Deployment"]
# idx_0 = []
# idx_5 = []
# idx_10 = []
# idx_15 = []
# idx_20 = []
# idx_25 = []
# idx_30 = []
# idx_35 = []
# idx_40 = []

# # Iterate over the specified NumPy arrays
# for i in range(0, 150):  # Indices of the arrays
#     array = numpy_arrays[i]
    
#     # Ignore the 1st column
#     array = array[:, 1:]
    
#     # Select multiples of the 6th value starting from the 2nd value
#     selected_values0 = array[0::6, :]       # X force
#     selected_values1 = array[1::6, :]       # Y force
#     selected_values2 = array[2::6, :]       # Z force
    
#     selected_values = np.sqrt(selected_values0**2 + selected_values1**2 + selected_values2**2)
    
#     # Remove the first 4 x values
#     selected_values = selected_values[0:, :]
    
#     # Create x and y coordinates
#     x = np.arange(selected_values.shape[0]) + 0
#     x_normalized = x * 100 / x.max()

#     y = np.full_like(x, i + 119)  # Use the index of the array as the y-coordinate, starting from 70
    
#     # Plot the selected values in 2D
#     for j in range(selected_values.shape[1]):
#         idx_0.append(selected_values[0, j])
#         idx_5.append(selected_values[5, j])
#         idx_10.append(selected_values[10, j])
#         idx_15.append(selected_values[15, j])
#         idx_20.append(selected_values[20, j])
#         idx_25.append(selected_values[25, j])
#         idx_30.append(selected_values[30, j])
#         idx_35.append(selected_values[35, j])
#         idx_40.append(selected_values[40, j])

# # Function to smooth the data using spline interpolation
# def smooth_data(x, y):
#     x_new = np.linspace(np.min(x), np.max(x), 300)
#     spl = make_interp_spline(x, y, k=3)  # k=3 for cubic spline
#     y_smooth = spl(x_new)
#     return x_new, y_smooth

# # Plot idx_30 with smoothing
# fig, ax = plt.subplots()
# x = np.arange(len(idx_10))
# x_smooth, idx_10_smooth = smooth_data(x, idx_10)
# x_smooth, idx_20_smooth = smooth_data(x, idx_20)
# x_smooth, idx_25_smooth = smooth_data(x, idx_25)
# x_smooth, idx_30_smooth = smooth_data(x, idx_30)
# x_smooth, idx_35_smooth = smooth_data(x, idx_35)
# x_smooth, idx_40_smooth = smooth_data(x, idx_40)

# ax.plot(x_smooth, idx_10_smooth)
# ax.plot(x_smooth, idx_20_smooth)
# ax.plot(x_smooth, idx_25_smooth)
# ax.plot(x_smooth, idx_30_smooth)
# ax.plot(x_smooth, idx_35_smooth)
# ax.plot(x_smooth, idx_40_smooth)

# # Increase the size of the legend, axis labels, and numbers
# ax.legend(['25% Span', '47% Span', '59% Span', '70% Span', '82% Span', '93% Span'], loc='upper right', fontsize=12)
# # ax.set_title('Spanwise Load Distribution after Minitab Deployment', fontsize=16)
# ax.set_xlabel('Time (s)', fontsize=16)
# ax.set_ylabel('Sectional Lift Force (N)', fontsize=18)
# ax.tick_params(axis='both', which='major', labelsize=18)

# # Set x-axis limits
# ax.set_xlim([70, 150])

# plt.show()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

with open('Output_FSI_dyn.out', 'r') as file:
    lines = file.readlines()

# Initialize a dictionary to store the last tip displacement value for each timestep
tip_displacements = {}
total_lift = {}
flow_time = {}
current_timestep = None
current_error = None

# Function to check if a string can be converted to a float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Iterate through each line in the file
for line in lines:
    # Check if the line contains "Time step: "
    if "Time step: " in line:
        # Extract the timestep
        current_timestep = line.split("Time step: ")[1].split(" ")[0]
    
    # Check if the line contains "Tip displacement: " and the error is less than 1e-3
    if "Tip displacement: " in line:
        # Extract the value after "Tip displacement: "
        value = line.split("Tip displacement: ")[1].split(" ")[0].strip()
        # Update the dictionary with the latest value for the timestep
        tip_displacements[current_timestep] = value

# Extract the values from the dictionary and print them
last_tip_displacements = list(tip_displacements.values())
# print(last_tip_displacements)

# Iterate through each line in the file
for line in lines:
    # Check if the line contains "Time step: "
    if "Time step: " in line:
        # Extract the timestep
        current_timestep = line.split("Time step: ")[1].split(" ")[0]
    
    # Check if the line contains "Tip displacement: " and the error is less than 1e-3
    if "Total lift: " in line:
        # Extract the value after "Tip displacement: "
        value = line.split("Total lift: ")[1].split(" ")[0].strip()
        # Update the dictionary with the latest value for the timestep
        total_lift[current_timestep] = value

# Iterate through each line in the file
for line in lines:
    # Check if the line contains "Time step: "
    if "Time step: " in line:
        # Extract the timestep
        current_timestep = line.split("Time step: ")[1].split(" ")[0]
    
    # Check if the line contains "Tip displacement: " and the error is less than 1e-3
    if "Flow time = " in line:
        # Extract the value after "Tip displacement: "
        value = line.split("Flow time = ")[1].split(" ")[0].strip()
        # Update the dictionary with the latest value for the timestep
        flow_time[current_timestep] = value

# Extract the values from the dictionaries
last_tip_displacements = list(tip_displacements.values())
last_flow_time = list(flow_time.values())
last_total_lift = list(total_lift.values())

# Convert the flow times and tip displacements to floats
last_flow_time = list(range(len(last_flow_time)))
# last_flow_time = [value * 0.005 for value in last_flow_time]
last_tip_displacements = [float(displacement) for displacement in last_tip_displacements]
last_total_lift = [float(lift) for lift in last_total_lift]

lift_coeff = [value / dyn_press for value in last_total_lift]


# print(last_flow_time)
# print(last_tip_displacements)
# print(last_total_lift)
# print(lift_coeff[90:100])

# ========================================================================================================
# Find the lowest value in the lift coefficient list
lowest_value_lift = float('inf')
lowest_index_lift = -1

# Iterate through the list to find the minimum value not equal to 0
for index, value in enumerate(lift_coeff):
    if value != 0 and value < lowest_value_lift:
        lowest_value_lift = value
        lowest_index_lift = index

# print("Lowest value not equal to 0:", lowest_value_lift, "at index:", lowest_index_lift)
# ========================================================================================================
# Lowest Tip Displacement not equal to 0 after the first 60 values
sliced_displacements = last_tip_displacements[60:]

# Initialize variables to store the minimum value and its index
lowest_value_disp = float('inf')
lowest_index_disp = -1

# Iterate through the sliced list to find the minimum value not equal to 0
for index, value in enumerate(sliced_displacements):
    if value != 0 and value < lowest_value_disp:
        lowest_value_disp = value
        lowest_index_disp = index + 60  # Adjust index to match the original list

# print(f"The lowest value not equal to 0 after the first 60 values is {lowest_value_disp} at index {lowest_index_disp}")

# ========================================================================================================

plt.figure(1)
plt.plot([x / 100 - 0.75 for x in last_flow_time[:335]], last_tip_displacements[:335], color='black', label='_nolegend_')
# plt.axvline(x=0.2, color='orange', linestyle='-', linewidth=1)  # Deployment Time
# # plt.text(0.2 + 0.02, 1350, f'Deployment at t = {20*0.01:.4f}', color='orange', va='center', ha='left', rotation='vertical')

# plt.axvline(x=0, color='black', linestyle='--', linewidth=2)

# plt.axvline(x=0.85, color='red', linestyle='-', linewidth=1)  # Time of Lowest Tip Displacement
# plt.text(0.85 + 0.02, 1172 + 350, f'Lowest at t = {85*0.01:.4f}', color='red', va='center', ha='left', rotation='vertical', fontsize=14)

# plt.axhline(y=lowest_value_disp, color='green', linestyle='--', linewidth=1)  # Lowest Tip Displacement
# plt.text(1.2, lowest_value_disp - 20, f'Lowest Disp. = {lowest_value_disp:.2f}mm', color='green', va='center', ha='left', fontsize=14)

# plt.axhline(y=1343.80, color='magenta', linestyle='--', linewidth=1)  # Steady Tip Displacement
# plt.text(2.1, 1343.80 - 20, f'Final Disp. = {1343.80:.2f}mm', color='magenta', va='center', ha='left', fontsize=14)

# plt.axhline(y=1681.5, color='blue', linestyle='--', linewidth=1)  # Median Tip Displacement
# plt.text(1.2, 1650, f'Clean Wing Disp. = 1681.5mm', color='blue', va='center', ha='left', fontsize=14)

# Change the font size of the axis numbers
# plt.tick_params(axis='both', which='major', labelsize=18)

# plt.xlabel('Time (s)', fontsize=18)
# plt.ylabel('Tip Displacement (mm)', fontsize=18)
# # plt.title('Tip Displacement vs Flow Time (Midflight Deployment (No Gust))')
# plt.legend(['Deployment of Minitab (T = 0.2s)'], fontsize=14)
# plt.grid(True)

plt.xlim(-0.2, 2.75)
plt.ylim(1000, 1900)

# xticks = range(0, len(last_flow_time) + 1, 25)
# plt.xticks(xticks)

# ========================================================================================================
# Load the plot_data.csv file
plot_data = pd.read_csv('plot_data.csv')

# Extract the time and lift coefficient data from the CSV file
time_csv = plot_data['Flow Time']
lift_coeff_csv = plot_data['Lift Coeff']

plt.figure(2)
plt.plot([x / 100 - 0.75 for x in last_flow_time[:335]], lift_coeff[:335], color='black', label='_nolegend_')
# plt.plot(time_csv[55:] / 100, lift_coeff_csv[55:], color='brown', linestyle='-')
# plt.axhline(y=0.349, color='brown', linestyle='--', linewidth=1, label='_nolegend_')  # Lowest Lift Coefficient
# plt.text(1.0, 0.351, f'Steady State Cl (Rigid) = 0.349', color='brown', va='center', ha='left', fontsize=14)

# plt.axvline(x=0.2, color='orange', linestyle='-', linewidth=1)  # Deployment Time
# # plt.text(0.2 + 0.02, 0.36, f'Deployment at t = {20*0.01:.4f}', color='orange', va='center', ha='left', rotation='vertical')

# plt.axvline(x=0, color='black', linestyle='--', linewidth=2, label='_nolegend_')

# plt.axvline(x=0.41, color='red', linestyle='-', linewidth=1, label='_nolegend_')  # Time of Lowest Lift Coefficient
# plt.text(0.41 + 0.02, 0.388, f'Lowest at t = {40*0.01:.4f}', color='red', va='center', ha='left', rotation='vertical', fontsize=14)

# plt.axhline(y=lowest_value_lift, color='green', linestyle='--', linewidth=1, label='_nolegend_')  # Lowest Lift Coefficient
# plt.text(1.0, lowest_value_lift - 0.001, f'Lowest Cl = {lowest_value_lift:.4f}', color='green', va='center', ha='left', fontsize=14)

# plt.axhline(y=0.3706, color='magenta', linestyle='--', linewidth=1, label='_nolegend_')  # Steady Lift Coefficient
# plt.text(1.65, 0.3706 - 0.001, f'Final Cl = {0.3706:.4f}', color='magenta', va='center', ha='left', fontsize=14)

# plt.axhline(y=0.3835, color='blue', linestyle='--', linewidth=1, label='_nolegend_')  # Median Cl
# plt.text(1.0, 0.382, f'Clean Wing Cl = 0.383', color='blue', va='center', ha='left', fontsize=14)

# # Change the font size of the axis numbers
# plt.tick_params(axis='both', which='major', labelsize=18)

# plt.xlabel('Time (s)', fontsize=18)
# plt.ylabel('Lift Coeff.', fontsize=18)
# # plt.title('Lift Coeff. vs Flow Time (Midflight Deployment (No Gust))')
# plt.legend(['Rigid Wing (Purely Aerodynamic)', 'Deployment of Minitab (T = 0.2s)'], fontsize=14)
# plt.grid()

plt.xlim(-0.2, 2.75)
plt.ylim(0.34, 0.4)

# xticks = range(0, len(last_flow_time) + 1, 25)
# plt.xticks(xticks)

# ========================================================================================================


# Load the Root_BM.npy file
root_bm = np.load('Root_BM.npy')

# # Load the Root_BM_Clean.npy file
# root_bm_clean = np.load('Root_BM_Clean.npy')


# Create the column index
column_index = np.arange(len(root_bm))

# Find the minimum value in the Root_BM array
min_root_bm = np.min(root_bm[75:342])
print(min_root_bm)
min_root_bm_index = np.argmin(root_bm)

# Find the maximum value in the Root_BM array
max_root_bm = np.max(root_bm[75:342])
max_root_bm_index = np.argmax(root_bm)


# Find percent difference between median and min
percent_diff = (-(min_root_bm/1000 - 1.26e7) / 1.26e7) * 100

# Plot Root_BM vs Column Index
# Create a figure and a set of subplots
fig, ax1 = plt.subplots()

# Plot Root_BM vs Column Index on the left y-axis
ax1.plot((column_index[:215] - 75) / 100, root_bm[:215] / 1000, '-', label='Root BM', color='red')
ax1.axvline(x=0, color='black', linestyle='--', linewidth=2, label='_nolegend_')

# Set labels and title for the left y-axis
ax1.set_xlabel('Time (s)', fontsize=18)
ax1.set_ylabel('Root Bending Moment (Nm) $e^{+7}$', color='red', fontsize=18)
# ax1.set_title('Root Bending Moment (Nm) and Tip Displacement vs Flow Time (s) (Minitab Deployment (No Gust))', fontsize=18)
ax1.tick_params(axis='y', labelcolor='red', labelsize=16)
ax1.tick_params(axis='x', labelsize=18)
ax1.set_xlim([-0.1, 1.5])
ax1.set_ylim([1e7, 1.5e7])

# Create a second y-axis for the tip displacement
ax2 = ax1.twinx()
ax2.plot([(x - 75) / 100 for x in last_flow_time[:215]], last_tip_displacements[:215], color='black', label='Tip Displacement')
ax2.set_ylabel('Tip Displacement (mm)', color='black', fontsize=18)
ax2.tick_params(axis='y', labelcolor='black', labelsize=18)
ax2.axvline(x=0.20, color='orange', linestyle='-', linewidth=1)  # Deployment Time

# Add legends
fig.legend(['Root Bending Moment', 'Tip Displacement', 'Deployment Time (T = 0.2s)'], loc='upper right', bbox_to_anchor=(0.88, 0.88), fontsize=12)
# Add grid
ax1.grid(True)


# ========================================================================================================

# Load the data
root_tm = np.load('Root_TM.npy')
tip_twist = np.load('Twist_Angle.npy')

# Create the column indices
column_index1 = np.arange(len(root_tm))
column_index2 = np.arange(len(tip_twist))

# Create a figure and a set of subplots
fig, ax1 = plt.subplots()

# Plot root_tm on the left y-axis
ax1.plot((column_index1[:215] - 75)/100, root_tm[:215]/1000, '-', label='Root TM', color='red')
ax1.axvline(x=0, color='black', linestyle='--', linewidth=2, label='_nolegend_')
# ax1.set_title('Root Torsion Moment (Nm) and Tip Twist Angle (Deg) vs Flow Time (s) (Minitab Deployment (No Gust))', fontsize=18)

ax1.set_xlabel('Time (s)', fontsize=18)
ax1.set_ylabel('Root Torsion Moment (Nm) $e^{+7}$', color='red', fontsize=16)
ax1.tick_params(axis='y', labelcolor='red', labelsize=16)
ax1.tick_params(axis='x', labelsize=18)
ax1.set_xlim([-0.10, 1.50])  # Set x-axis limits
ax1.set_ylim([-4e7, -1.5e7])


# Create a second y-axis for the tip twist
ax2 = ax1.twinx()
ax2.plot((column_index2[:215] - 75) / 100, tip_twist[:215] * 57.2958, '-', label='Tip Twist', color='black')
ax2.set_ylabel('Tip Twist (degrees)', color='black', fontsize=18)
ax2.tick_params(axis='y', labelcolor='black', labelsize=18)
ax2.axvline(x=0.20, color='orange', linestyle='-', linewidth=1)  # Deployment Time


# Add legends
fig.legend(['Root Torsion Moment', 'Tip Twist Angle', 'Deployment Time (T = 0.2s)'], loc='upper right', bbox_to_anchor=(0.88, 0.88), fontsize=12)

# Add grid
ax1.grid(True)


# Show the plot
plt.show()
