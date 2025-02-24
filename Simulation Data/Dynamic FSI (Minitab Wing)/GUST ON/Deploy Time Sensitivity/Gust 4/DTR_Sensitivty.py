import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


# Read the CSV files
data1 = pd.read_csv('0852_G4.csv')
data2 = pd.read_csv('0926_G4.csv')
data3 = pd.read_csv('1000_G4.csv')
data4 = pd.read_csv('1074_G4.csv')
data5 = pd.read_csv('G4_Clean.csv')


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

flow_time5 = data5['Flow Time']
tip_displacement5 = data5['Tip Displacement']
lift_coeff5 = data5['Lift Coeff']

peak_cl_time = 15
peak_disp_time = 138


# Assuming lift_coeff2, lift_coeff3, and lift_coeff4 are defined earlier in the code
# Example arrays (replace these with actual data)
lift_coeff1 = np.array(lift_coeff1)
lift_coeff2 = np.array(lift_coeff2)
lift_coeff3 = np.array(lift_coeff3)
lift_coeff4 = np.array(lift_coeff4)
lift_coeff5 = np.array(lift_coeff5)

# Slice arrays to exclude the first 70 values
lift_coeff1_sliced = lift_coeff1[70:]
lift_coeff2_sliced = lift_coeff2[70:]
lift_coeff3_sliced = lift_coeff3[70:]
lift_coeff4_sliced = lift_coeff4[70:]
lift_coeff5_sliced = lift_coeff5[70:]


# Find the index of the maximum value in each sliced array
index_peak_lift_coeff1 = np.argmax(lift_coeff1_sliced) + 70
index_peak_lift_coeff2 = np.argmax(lift_coeff2_sliced) + 70
index_peak_lift_coeff3 = np.argmax(lift_coeff3_sliced) + 70
index_peak_lift_coeff4 = np.argmax(lift_coeff4_sliced) + 70
index_peak_lift_coeff5 = np.argmax(lift_coeff5_sliced) + 70

# Find the peak values
peak_lift_coeff1 = lift_coeff1[index_peak_lift_coeff1]
peak_lift_coeff2 = lift_coeff2[index_peak_lift_coeff2]
peak_lift_coeff3 = lift_coeff3[index_peak_lift_coeff3]
peak_lift_coeff4 = lift_coeff4[index_peak_lift_coeff4]
peak_lift_coeff5 = lift_coeff5[index_peak_lift_coeff5]

# Find the maximum and minimum values among the peaks
max_peak_value = max(peak_lift_coeff1, peak_lift_coeff2, peak_lift_coeff3, peak_lift_coeff4, peak_lift_coeff5)
min_peak_value = min(peak_lift_coeff1, peak_lift_coeff2, peak_lift_coeff3, peak_lift_coeff4, peak_lift_coeff5)

# Calculate the maximum difference
max_difference = max_peak_value - min_peak_value
percentage_difference = (max_difference / min_peak_value) * 100


plt.figure(1)
plt.plot([x/100 - 1.24 for x in flow_time5], tip_displacement5, color='magenta')
plt.plot([x/100 - 1.24 for x in flow_time1], tip_displacement1, color='black')
plt.plot([x/100 - 1.24 for x in flow_time2], tip_displacement2, color='blue')
plt.plot([x/100 - 1.24 for x in flow_time3], tip_displacement3, color='red')
plt.plot([x/100 - 1.24 for x in flow_time4], tip_displacement4, color='green')

# plt.plot(flow_time2, tip_displacement2, color='red')

plt.axvline(x=0, color='black', linestyle='--', linewidth=1)  # Peak Cl

# Change the font size of the axis numbers
plt.tick_params(axis='both', which='major', labelsize=18)

plt.legend(['Clean Wing ', 'DTR = -0.12 ', 'DTR = 0.44 ', 'DTR = 1.00 ','DTR = 1.56 '], fontsize = 16)
plt.xlabel('Time (s)', fontsize = 18)
plt.ylabel('Tip Displacement', fontsize = 18)
# plt.title('Tip Displacement Vs Time (Deployment Time Variation (s)) Gust G4')
plt.grid(True)

plt.xlim(-0.40, 1.20)
plt.ylim(1000, 1900)

# xticks = range(0, len(last_flow_time) + 1, 25)
# plt.xticks(xticks)


# ========================================================================================================


plt.figure(2)
plt.plot([x/100 - 1.24 for x in flow_time5], lift_coeff5, color='magenta')
plt.plot([x/100 - 1.24 for x in flow_time1], lift_coeff1, color='black')
plt.plot([x/100 - 1.24 for x in flow_time2], lift_coeff2, color='blue')
plt.plot([x/100 - 1.24 for x in flow_time3], lift_coeff3, color='red')
plt.plot([x/100 - 1.24 for x in flow_time4], lift_coeff4, color='green')


plt.axvline(x=0, color='black', linestyle='--', linewidth=1)  # Peak Cl
plt.text((20 + 4)/100, 0.555, f'Max Diff: {percentage_difference:.3f}%', color='black', fontsize = 14)

# Change the font size of the axis numbers
plt.tick_params(axis='both', which='major', labelsize=18)

plt.legend(['Clean Wing ', 'DTR = -0.12 ', 'DTR = 0.44 ', 'DTR = 1.00 ','DTR = 1.56 '], fontsize = 16)
plt.xlabel('Time (s)', fontsize = 18)
plt.ylabel('Lift Coeff.', fontsize = 18)
# plt.title('Lift Coeff. Vs Time (Deployment Time Variation (s)) Gust G4')
plt.grid()

plt.xlim(-0.40, 1.20)
plt.ylim(0.3, 0.6)

# xticks = range(0, len(last_flow_time) + 1, 25)
# plt.xticks(xticks)

plt.show()

# Sample data
configurations = [1, 2, 3, 4]
lift_coeff_at_4 = [lift_coeff1[144], lift_coeff2[144], lift_coeff3[144], lift_coeff4[144]]

# Create a spline of the data
x_new = np.linspace(min(configurations), max(configurations), 300)
spl = make_interp_spline(configurations, lift_coeff_at_4, k=3)  # k=3 for cubic spline
lift_coeff_smooth = spl(x_new)

# Plot the smooth curve
plt.figure()
plt.plot(configurations, lift_coeff_at_4, linestyle='-', color='black', marker='o', markerfacecolor='red')

# Change the font size of the axis numbers
plt.tick_params(axis='both', which='major', labelsize=18)

plt.xticks(configurations, ['-0.12', '0.44', '1.00', '1.56'])
plt.xlabel('DTR', fontsize = 18)
plt.ylabel('Lift Coeff.', fontsize = 18)
# plt.title('Lift Coeff. at Gust(G2) Peak vs DTR Configurations')
plt.grid()
plt.show()