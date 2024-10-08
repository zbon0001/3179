import pandas as pd

# Original data (replace this with the path to your file or modify as needed)
data = {
    'DonorType': ['Regular donor', 'Lapsed donor', 'New donor'],
    'Malaysia': [61.2, 18, 20.8],
    'Selangor': [56.9, 22.3, 20.7],
    'Melaka': [64.1, 16.8, 19.1],
    'Pulau Pinang': [65.2, 16.9, 17.9],
    'Pahang': [62.4, 14, 23.6],
    'Terengganu': [57.5, 14.6, 27.9],
    'Perak': [65, 15.4, 19.6],
    'Sarawak': [73.8, 11.4, 14.8],
    'Sabah': [61.5, 16.3, 22.3],
    'Johor': [59.2, 18.8, 22],
    'Kelantan': [56.3, 16, 27.7],
    'Negeri Sembilan': [59.4, 18.6, 22],
    'Kedah': [57.6, 19.1, 23.3]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to transform it into the desired long format
df_melted = df.melt(id_vars='DonorType', var_name='State', value_name='Percentage')

# Save the transformed DataFrame to a CSV file
df_melted.to_csv('donor_regularities.csv', index=False)

print("Transformed data saved as 'donor_regularities.csv'")
