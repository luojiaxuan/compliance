import pandas as pd
from scipy.stats import pointbiserialr
from scipy.stats import ttest_ind

# Replace 'your_file.xlsx' with the path to your actual file
df = pd.read_excel('Employee_Survey_Results.xlsx', engine='openpyxl')


# Summary statistics for numerical columns
Descriptive_Stats = df.describe()
print("Descriptive Statistics for Numerical Columns: ")
print(Descriptive_Stats)
print("\n\n")


# Calculate the percentage of Yes and No
# Calculate the count of 'Yes' and 'No' values
yes_no_counts = df['Clicked Suspicious Link (Yes/No)'].value_counts()

# Calculate the total number of rows
total_counts = len(df)

# Calculate percentages
yes_percentage = (yes_no_counts['Yes'] / total_counts) * 100
no_percentage = (yes_no_counts['No'] / total_counts) * 100

# Print the percentages
print("Percentage of 'Yes' and 'No' values: ")
print(f"    Percentage of 'Yes': {yes_percentage:.2f}%")
print(f"    Percentage of 'No': {no_percentage:.2f}%")


print("\n")
# Calculate the correlation coefficient between 'Training Hours' and 'Phishing Confidence'
correlation = df['Training Hours (0-10)'].corr(df['Phishing Confidence (1-5)'])
# Print the correlation coefficient
print(f"Correlation coefficient between 'Training Hours' and 'Phishing Confidence': {correlation}")
print("Results: Training Hours and Phishing Confidence are positive correlated.")


print("\n")
# Calculate point-biserial correlation between 'Clicked Suspicious Link' and 'Training Hours'
# Convert 'Clicked Suspicious Link' to binary (1 for Yes, 0 for No)
df['Clicked Suspicious Link (Yes/No)'] = df['Clicked Suspicious Link (Yes/No)'].apply(lambda x: 1 if x == 'Yes' else 0)

# Calculate point-biserial correlation
correlation, p_value = pointbiserialr(df['Clicked Suspicious Link (Yes/No)'], df['Training Hours (0-10)'])

# Print the correlation and p-value
print("Point-biserial correlation between 'Clicked Suspicious Link' and 'Training Hours': ")
print(f"Point-biserial correlation: {correlation}")
print(f"P-value: {p_value}")

print("Results: Indicates a strong negative relationship between 'Clicked Suspicious Link' on yes and more 'Training Hours'.")


print("\n")
# Calculate means for each group
mean_yes = df[df['Clicked Suspicious Link (Yes/No)'] == 1]['Training Hours (0-10)'].mean()
mean_no = df[df['Clicked Suspicious Link (Yes/No)'] == 0]['Training Hours (0-10)'].mean()


# Print the means
print("Mean Training Hours for each group: ")
print(f"    Mean Training Hours for group of people choose 'Yes': {mean_yes}")
print(f"    Mean Training Hours for gourp of people choose'No': {mean_no}")


print("\n")
# Perform t-test on the two groups on 'Training Hours'
yes_group = df[df['Clicked Suspicious Link (Yes/No)'] == 1]['Training Hours (0-10)']
no_group = df[df['Clicked Suspicious Link (Yes/No)'] == 0]['Training Hours (0-10)']

t_stat, p_value = ttest_ind(yes_group, no_group)
# Print the t-statistic and p-value
print("T-test results between yes_group and no_group: ")
print(f"t-statistic: {t_stat}")
print(f"p-value: {p_value}")

print("Results: The analysis shows that there is a statistically significant and substantial difference in training hours between Yes and No group.")
print("\n")