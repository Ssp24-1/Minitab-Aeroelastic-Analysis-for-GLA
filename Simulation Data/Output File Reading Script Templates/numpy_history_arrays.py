import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from pymatreader import read_mat

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

data = read_mat('history_0.0_350_342.00000s.mat')
my_df = pd.DataFrame(data['SPC_LOAD'][:])
df1 = my_df.to_numpy()

my_df2 = pd.DataFrame(data['Z'][:])
df2 = my_df2.to_numpy()

# Extract every 6th row from df1, starting from index 1
extracted_rows = df1[:, 3]

# Extract every 6th row from df1, starting from index 1
extracted_rows2 = df2[262, :]

# Extract every 6th row from df1, starting from index 1
extracted_rows3 = df1[:, 4]

# =============================================================================
# # Display the extracted rows
# print('Extracted rows:')
# print(extracted_rows)
# print(extracted_rows2)
# print(extracted_rows3)
# =============================================================================

# Export df1 as a .npy file
np.save('Root_BM.npy', extracted_rows)

# Alternatively, export df1 as a CSV file
np.savetxt('Root_BM_CSV.csv', extracted_rows, delimiter=',')


# Export df1 as a .npy file
np.save('Twist_Angle.npy', extracted_rows2)

# Alternatively, export df1 as a CSV file
np.savetxt('Twist_Angle_CSV.csv', extracted_rows2, delimiter=',')


# Export df1 as a .npy file
np.save('Root_TM.npy', extracted_rows3)

# Alternatively, export df1 as a CSV file
np.savetxt('Root_TM_CSV.csv', extracted_rows3, delimiter=',')



# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Get a list of all .mat files in the same directory as the script
mat_files = glob.glob(os.path.join(script_directory, '*.mat'))

# List to store the NumPy arrays
numpy_arrays = []

# Iterate over each .mat file
for mat_file in mat_files:
    # Read the .mat file
    data = read_mat(mat_file)
    
    # Convert the data to a DataFrame
    my_df = pd.DataFrame(data['PAX'][:])
    
    # Convert the DataFrame to a NumPy array
    df_array = my_df.to_numpy()
    
    # Append the NumPy array to the list
    numpy_arrays.append(df_array)

# Save the NumPy arrays to a .npz file
np.savez('numpy_arrays.npz', *numpy_arrays)

# Now numpy_arrays contains the NumPy arrays for all .mat files