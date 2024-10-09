import pandas as pd

# Replace with the path to your CSV file
input_file = 'stacked_bar_blood groups.csv'
output_file = 'filtered_stacked_bar_blood_groups.csv'

# Read the CSV file
df = pd.read_csv(input_file)

# Filter out rows where the state is 'Malaysia'
filtered_df = df[df['state'] != 'Malaysia']

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv(output_file, index=False)

print("Rows with 'Malaysia' as the state have been removed and saved to", output_file)
