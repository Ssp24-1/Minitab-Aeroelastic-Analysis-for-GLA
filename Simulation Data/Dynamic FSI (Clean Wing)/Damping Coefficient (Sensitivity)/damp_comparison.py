import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files
data1 = pd.read_csv('flow_time_lift_coeff_0.csv')
data2 = pd.read_csv('flow_time_lift_coeff_2.csv')
data3 = pd.read_csv('flow_time_lift_coeff_5.csv')
data4 = pd.read_csv('flow_time_lift_coeff_10.csv')



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

# with open('Output_FSI_dyn.out', 'r') as file:
#     lines = file.readlines()

# # Initialize a dictionary to store the last tip displacement value for each timestep
# tip_displacements = {}
# total_lift = {}
# flow_time = {}
# current_timestep = None
# current_error = None

# # Function to check if a string can be converted to a float
# def is_float(value):
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False

# # Iterate through each line in the file
# for line in lines:
#     # Check if the line contains "Time step: "
#     if "Time step: " in line:
#         # Extract the timestep
#         current_timestep = line.split("Time step: ")[1].split(" ")[0]
    
#     # Check if the line contains "Tip displacement: " and the error is less than 1e-3
#     if "Tip displacement: " in line:
#         # Extract the value after "Tip displacement: "
#         value = line.split("Tip displacement: ")[1].split(" ")[0].strip()
#         # Update the dictionary with the latest value for the timestep
#         tip_displacements[current_timestep] = value

# # Extract the values from the dictionary and print them
# last_tip_displacements = list(tip_displacements.values())
# # print(last_tip_displacements)

# # Iterate through each line in the file
# for line in lines:
#     # Check if the line contains "Time step: "
#     if "Time step: " in line:
#         # Extract the timestep
#         current_timestep = line.split("Time step: ")[1].split(" ")[0]
    
#     # Check if the line contains "Tip displacement: " and the error is less than 1e-3
#     if "Total lift: " in line:
#         # Extract the value after "Tip displacement: "
#         value = line.split("Total lift: ")[1].split(" ")[0].strip()
#         # Update the dictionary with the latest value for the timestep
#         total_lift[current_timestep] = value

# # Iterate through each line in the file
# for line in lines:
#     # Check if the line contains "Time step: "
#     if "Time step: " in line:
#         # Extract the timestep
#         current_timestep = line.split("Time step: ")[1].split(" ")[0]
    
#     # Check if the line contains "Tip displacement: " and the error is less than 1e-3
#     if "Flow time = " in line:
#         # Extract the value after "Tip displacement: "
#         value = line.split("Flow time = ")[1].split(" ")[0].strip()
#         # Update the dictionary with the latest value for the timestep
#         flow_time[current_timestep] = value

# # Extract the values from the dictionaries
# last_tip_displacements = list(tip_displacements.values())
# last_flow_time = list(flow_time.values())
# last_total_lift = list(total_lift.values())

# # Convert the flow times and tip displacements to floats
# last_flow_time = list(range(len(last_flow_time)))
# # last_flow_time = [value * 0.005 for value in last_flow_time]
# last_tip_displacements = [float(displacement) for displacement in last_tip_displacements]
# last_total_lift = [float(lift) for lift in last_total_lift]

# dyn_press = 2128598.72082399
# lift_coeff = [value / dyn_press for value in last_total_lift]


# # print(last_flow_time)
# # print(last_tip_displacements)
# # print(last_total_lift)
# # print(lift_coeff)

# # ========================================================================================================
# # Find the lowest value in the lift coefficient list
# lowest_value_lift = float('inf')
# lowest_index_lift = -1

# # Iterate through the list to find the minimum value not equal to 0
# for index, value in enumerate(lift_coeff):
#     if value != 0 and value < lowest_value_lift:
#         lowest_value_lift = value
#         lowest_index_lift = index

# # print("Lowest value not equal to 0:", lowest_value_lift, "at index:", lowest_index_lift)

# ========================================================================================================  
peak_cl_time = 115
peak_disp_time = 138


plt.figure(1)
plt.plot(flow_time1[:231], tip_displacement1[:231], color = 'black')
plt.plot(flow_time2, tip_displacement2, color='blue')
plt.plot(flow_time3, tip_displacement3, color='red')
plt.plot(flow_time4, tip_displacement4, color='green')
# plt.plot(flow_time2, tip_displacement2, color='red')

plt.axvline(x=peak_cl_time, color='orange', linestyle='--', linewidth=1)  # Peak Cl

plt.axvline(x=peak_disp_time, color='green', linestyle='--', linewidth=1)  # Peak Tip Disp

tip_disp_0K = tip_displacement1[138]
tip_disp_2K = tip_displacement2[138]
tip_disp_5K = tip_displacement3[138]
tip_disp_10K = tip_displacement4[138]


print(f"0% K: {tip_disp_0K}\n2% K: {tip_disp_2K}\n5% K: {tip_disp_5K}\n10% K: {tip_disp_10K}")

# Calculate the difference
difference = abs(tip_disp_2K - tip_disp_0K)
percent_diff = (difference / tip_disp_0K) * 100

# Format the difference into the string
result_string = f'Difference = {difference:.2f}mm ; Percent Diff = {percent_diff:.2f}%'

plt.text(138 + 2, 1900, result_string, color='magenta', va='center', ha='left')



# plt.axvline(x=lowest_index_disp, color='red', linestyle='-', linewidth=1)  # Time of Lowest Tip Displacement
# plt.text(lowest_index_disp + 2, lowest_value_disp-400, f't = {lowest_index_disp*0.01:.4f}', color='red', va='center', ha='left', rotation = 'vertical')

# plt.axhline(y=lowest_value_disp, color='green', linestyle='--', linewidth=1)  # Lowest Tip Displacement
# plt.text(100, lowest_value_disp-50, f'Lowest Disp. = {lowest_value_disp:.4f}mm', color='green', va='center', ha='left')

# plt.axhline(y=1681.5, color='blue', linestyle='--', linewidth=1)  # Median Tip Displacement
# plt.text(100, 1600, f'Median Disp = 1681.5mm', color='blue', va='center', ha='left')

plt.legend(['0% K ', '2% K ','5% K ','10% K ', 'Peak Cl', 'Peak Disp'])
plt.xlabel('Flow Time (0.01s)')
plt.ylabel('Tip Displacement')
plt.title('Tip Displacement Vs Time (Damping Coeff Variation %K)')
plt.grid(True)

# plt.xlim(0, len(last_flow_time) + 1)
# plt.ylim(0, 2500)

# xticks = range(0, len(last_flow_time) + 1, 25)
# plt.xticks(xticks)


# ========================================================================================================


plt.figure(2)
plt.plot(flow_time1[:231], lift_coeff1[:231], color = 'black')
plt.plot(flow_time2, lift_coeff2, color='blue')
plt.plot(flow_time3, lift_coeff3, color='red')
plt.plot(flow_time4, lift_coeff4, color='green')
# plt.plot(flow_time2, lift_coeff2, color='red')

plt.axvline(x=peak_cl_time, color='orange', linestyle='--', linewidth=1)  # Peak Cl

plt.axvline(x=peak_disp_time, color='green', linestyle='--', linewidth=1)  # Peak Tip Disp

lift_coeff_0K = lift_coeff1[115]
lift_coeff_2K = lift_coeff2[115]
lift_coeff_5K = lift_coeff3[115]
lift_coeff_10K = lift_coeff4[115]

print(f"0% K: {lift_coeff_0K}\n2% K: {lift_coeff_2K}\n5% K: {lift_coeff_5K}\n10% K: {lift_coeff_10K}")

# Calculate the difference
difference = abs(lift_coeff_10K - lift_coeff_0K)
percent_diff = (difference / lift_coeff_0K) * 100

# Format the difference into the string
result_string = f'Difference = {difference:.3f} ; Percent Diff = {percent_diff:.3f}%'

plt.text(115 + 2, 0.55, result_string, color='magenta', va='center', ha='left')

# plt.legend()

# plt.axvline(x=lowest_index_lift, color='red', linestyle='-', linewidth=1)  # Time of Lowest Lift Coefficient
# plt.text(lowest_index_lift + 2, 0.4, f't = {lowest_index_lift*0.01:.4f}', color='red', va='center', ha='left', rotation = 'vertical')

# plt.axhline(y=lowest_value_lift, color='green', linestyle='--', linewidth=1)  # Lowest Lift Coefficient
# plt.text(100, lowest_value_lift-0.003, f'Lowest Cl = {lowest_value_lift:.4f}', color='green', va='center', ha='left')

# plt.axhline(y=0.3832, color='blue', linestyle='--', linewidth=1)  # Median Tip Displacement
# plt.text(100, 0.378, f'Median Cl = 0.383', color='blue', va='center', ha='left')

plt.legend(['0% K ', '2% K ','5% K ','10% K ', 'Peak Cl', 'Peak Disp'])
plt.xlabel('Flow Time (0.01s)')
plt.ylabel('Lift Coeff.')
plt.title('Lift Coeff. Vs Time (Damping Coeff Variation %K)')
plt.grid()

# plt.xlim(0, len(last_flow_time) + 1)
plt.ylim(0.3, 0.6)

# xticks = range(0, len(last_flow_time) + 1, 25)
# plt.xticks(xticks)

plt.show()