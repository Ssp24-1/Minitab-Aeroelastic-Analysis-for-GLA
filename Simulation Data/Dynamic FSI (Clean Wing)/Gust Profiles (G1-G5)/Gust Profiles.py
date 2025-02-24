import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files
data1 = pd.read_csv('G1_Clean.csv')
data2 = pd.read_csv('G2_Clean.csv')
data3 = pd.read_csv('G3_Clean.csv')
data4 = pd.read_csv('G4_Clean.csv')



# Extract relevant data
flow_time1 = data1['Flow Time']
tip_displacement1 = data1['Tip Displacement']
lift_coeff1 = data1['Lift Coeff']

flow_time2 = data2['Flow Time']
tip_displacement2 = data2['Tip Displacement']
lift_coeff2 = data2['Lift Coeff']

flow_time3 = data3['Flow Time']
tip_displacement3 = data3['Tip Displacement']
lift_coeff3 = data3['Lift Coeff']

flow_time4 = data4['Flow Time']
tip_displacement4 = data4['Tip Displacement']
lift_coeff4 = data4['Lift Coeff']

# ========================================================================================================

peak_cl_time = 134
peak_disp_time = 138


# Assuming lift_coeff2, lift_coeff3, and lift_coeff4 are defined earlier in the code
# Example arrays (replace these with actual data)
lift_coeff1 = np.array(lift_coeff1)
lift_coeff2 = np.array(lift_coeff2)
lift_coeff3 = np.array(lift_coeff3)
lift_coeff4 = np.array(lift_coeff4)

# Slice arrays to exclude the first 70 values
lift_coeff1_sliced = lift_coeff1[70:]
lift_coeff2_sliced = lift_coeff2[70:]
lift_coeff3_sliced = lift_coeff3[70:]
lift_coeff4_sliced = lift_coeff4[70:]


# Find the index of the maximum value in each sliced array
index_peak_lift_coeff1 = np.argmax(lift_coeff1_sliced) + 70
index_peak_lift_coeff2 = np.argmax(lift_coeff2_sliced) + 70
index_peak_lift_coeff3 = np.argmax(lift_coeff3_sliced) + 70
index_peak_lift_coeff4 = np.argmax(lift_coeff4_sliced) + 70

# Find the peak values
peak_lift_coeff1 = lift_coeff1[index_peak_lift_coeff1]
peak_lift_coeff2 = lift_coeff2[index_peak_lift_coeff2]
peak_lift_coeff3 = lift_coeff3[index_peak_lift_coeff3]
peak_lift_coeff4 = lift_coeff4[index_peak_lift_coeff4]

# Print all the peak values 
print(f'Peak Lift Coeff 1: {peak_lift_coeff1} at index {index_peak_lift_coeff1}')
print(f'Peak Lift Coeff 2: {peak_lift_coeff2} at index {index_peak_lift_coeff2}')
print(f'Peak Lift Coeff 3: {peak_lift_coeff3} at index {index_peak_lift_coeff3}')
print(f'Peak Lift Coeff 4: {peak_lift_coeff4} at index {index_peak_lift_coeff4}')

# Find the maximum and minimum values among the peaks
max_peak_value = max(peak_lift_coeff1, peak_lift_coeff2, peak_lift_coeff3, peak_lift_coeff4)
min_peak_value = min(peak_lift_coeff1, peak_lift_coeff2, peak_lift_coeff3, peak_lift_coeff4)

# Calculate the maximum difference
max_difference = max_peak_value - min_peak_value
percentage_difference = (max_difference / min_peak_value) * 100

# ========================================================================================================

# Define the onset indices
onset_g1 = 130
onset_g2 = 129
onset_g3 = 128
onset_g4 = 124

# Shift the flow_time values so that they all start from X = 0
shift_value1 = flow_time1[onset_g1]
shift_value2 = flow_time2[onset_g2]
shift_value3 = flow_time3[onset_g3]
shift_value4 = flow_time4[onset_g4]

adjusted_flow_time1 = [time - shift_value1 for time in flow_time1]
adjusted_flow_time2 = [time - shift_value2 for time in flow_time2]
adjusted_flow_time3 = [time - shift_value3 for time in flow_time3]
adjusted_flow_time4 = [time - shift_value4 for time in flow_time4]

# Divide the adjusted flow time values by 100
adjusted_flow_time1 = [time / 100 for time in adjusted_flow_time1]
adjusted_flow_time2 = [time / 100 for time in adjusted_flow_time2]
adjusted_flow_time3 = [time / 100 for time in adjusted_flow_time3]
adjusted_flow_time4 = [time / 100 for time in adjusted_flow_time4]



plt.figure(1)
plt.plot(adjusted_flow_time1, tip_displacement1, color='black')
# plt.plot(adjusted_flow_time2, tip_displacement2, color='blue')
# plt.plot(adjusted_flow_time3, tip_displacement3, color='red')
# plt.plot(adjusted_flow_time4, tip_displacement4, color='green')

# Add a prominent vertical line at X=0
plt.axvline(x=0, color='black', linewidth=2, linestyle='--')

# plt.plot(flow_time2, tip_displacement2, color='red')
# plt.axvline(x=peak_cl_time, color='orange', linestyle='--', linewidth=1)  # Peak Cl

# Change the font size of the axis numbers
plt.tick_params(axis='both', which='major', labelsize=18)

plt.legend(['Gust G1', 'Gust G2', 'Gust G3', 'Gust G4'], fontsize = 16)
plt.xlabel('Time (s)', fontsize = 18)
plt.ylabel('Tip Displacement', fontsize = 18)
# plt.title('Tip Displacement Vs Time (Gust Profiles)')
plt.grid(True)

plt.xlim(-0.19, 1.00)
plt.ylim(1500, 1800)

# xticks = range(0, len(last_flow_time) + 1, 25)
# plt.xticks(xticks)


# ========================================================================================================

plt.figure(2)
plt.plot(adjusted_flow_time1, lift_coeff1, color='red')
# plt.plot(adjusted_flow_time2, lift_coeff2, color='blue')
# plt.plot(adjusted_flow_time3, lift_coeff3, color='red')
# plt.plot(adjusted_flow_time4, lift_coeff4, color='green')

# Add a prominent vertical line at X=0
# plt.axvline(x=0, color='black', linewidth=2, linestyle='--')

# Change the font size of the axis numbers
plt.tick_params(axis='both', which='major', labelsize=18)

# plt.legend(['Gust G1', 'Gust G2', 'Gust G3', 'Gust G4'], fontsize = 16)
# plt.xlabel('Time (s)', fontsize = 18)
# plt.ylabel('Lift Coeff.', fontsize = 18)
# plt.title('Lift Coeff. Vs Time (Gust Profiles)')
# plt.grid()

plt.xlim(-0.19, 0.4)
plt.ylim(0.3, 0.55)

plt.show()


# # Calculate the target value
# target_value = 0.383 * 1.005

# # Function to find the index where the value first exceeds the target value, skipping the first 70 values
# def find_index_exceeding_target(lift_coeff, target_value):
#     for index in range(70, len(lift_coeff)):
#         if lift_coeff[index] > target_value:
#             return index
#     return None

# # Find indices for each plot
# index1 = find_index_exceeding_target(lift_coeff1, target_value)
# index2 = find_index_exceeding_target(lift_coeff2, target_value)
# index3 = find_index_exceeding_target(lift_coeff3, target_value)
# index4 = find_index_exceeding_target(lift_coeff4, target_value)

# # Print the indices
# print(f'Index for lift_coeff1: {index1}')
# print(f'Index for lift_coeff2: {index2}')
# print(f'Index for lift_coeff3: {index3}')
# print(f'Index for lift_coeff4: {index4}')

plt.show()
