# import pandas as pd

# # Load the CSV file into a DataFrame
# df = pd.read_csv('categorizedstate_blood_donations_vs_year.csv')  # Replace with your CSV file path

# # Filter for rows where blood_type is 'all'
# all_blood_type_df = df[df['blood_type'] == 'all']

# # Group by 'year' and 'state', then sum the donations
# yearly_state_donations = all_blood_type_df.groupby(['year', 'state'])['donations'].sum().reset_index()

# # Find the top 5 states by donations for each year
# top_5_states_per_year = yearly_state_donations.sort_values(['year', 'donations'], ascending=[True, False]).groupby('year').head(5)

# # Export the results to a CSV file
# top_5_states_per_year.to_csv('top5_states_each_year.csv', index=False)  # Replace with desired output path

# # Display the results
# print(top_5_states_per_year)

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('categorizedstate_blood_donations_vs_year.csv')  # Replace with your CSV file path

# Filter for rows where blood_type is A, AB, B, or O
filtered_df = df[df['blood_type'].isin(['a', 'ab', 'b', 'o'])]

# Group by 'year', 'state', and 'blood_type', then sum the donations
state_donations = filtered_df.groupby(['year', 'state', 'blood_type'])['donations'].sum().reset_index()

# Calculate the total for each blood type across all states for each year (for "Malaysia")
malaysia_donations = state_donations.groupby(['year', 'blood_type'])['donations'].sum().reset_index()
malaysia_donations['state'] = 'Malaysia'

# Combine the state-level data with the "Malaysia" totals
combined_df = pd.concat([state_donations, malaysia_donations], ignore_index=True)

# Export the results to a CSV file
combined_df.to_csv('stacked_bar_blood groups.csv', index=False)  # Replace with desired output path

# Display the results
print(combined_df)

