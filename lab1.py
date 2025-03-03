import pandas as pd
from scipy.stats import pointbiserialr
from scipy.stats import ttest_ind, sem
import matplotlib.pyplot as plt
import seaborn as sns

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


# Create a scatter plot with regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='Training Hours (0-10)', y='Phishing Confidence (1-5)', data=df)
plt.title(f"Scatter Plot of Training Hours vs Phishing Confidence with Regression Line\nCorrelation Coefficient: {correlation:.2f}")
plt.xlabel('Training Hours (0-10)')
plt.ylabel('Phishing Confidence (1-5)')
plt.grid(True)
plt.show()



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

# Create a violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Clicked Suspicious Link (Yes/No)', y='Training Hours (0-10)', data=df)
plt.title('Violin Plot of Training Hours by Clicked Suspicious Link')
plt.xlabel('Clicked Suspicious Link (0 = No, 1 = Yes)')
plt.ylabel('Training Hours (0-10)')
plt.grid(True)
plt.show()


print("\n")
# Calculate means for each group
mean_yes = df[df['Clicked Suspicious Link (Yes/No)'] == 1]['Training Hours (0-10)'].mean()
mean_no = df[df['Clicked Suspicious Link (Yes/No)'] == 0]['Training Hours (0-10)'].mean()


# Print the means
print("Mean Training Hours for each group: ")
print(f"    Mean Training Hours for group of people choose 'Yes': {mean_yes}")
print(f"    Mean Training Hours for gourp of people choose'No': {mean_no}")

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=['Yes', 'No'], y=[mean_yes, mean_no])
plt.title('Mean Training Hours by Clicked Suspicious Link')
plt.xlabel('Clicked Suspicious Link (Yes/No)')
plt.ylabel('Mean Training Hours (0-10)')
plt.grid(True)
plt.show()



print("\n")
# Perform t-test on the two groups on 'Training Hours'
yes_group = df[df['Clicked Suspicious Link (Yes/No)'] == 1]['Training Hours (0-10)']
no_group = df[df['Clicked Suspicious Link (Yes/No)'] == 0]['Training Hours (0-10)']

# Calculate means and standard errors
mean_yes = yes_group.mean()
mean_no = no_group.mean()
sem_yes = sem(yes_group)
sem_no = sem(no_group)

t_stat, p_value = ttest_ind(yes_group, no_group)
# Print the t-statistic and p-value
print("T-test results between yes_group and no_group: ")
print(f"t-statistic: {t_stat}")
print(f"p-value: {p_value}")

print("Results: The analysis shows that there is a statistically significant and substantial difference in training hours between Yes and No group.")
print("\n")

# Create a t-test bar plot with error bars
plt.figure(figsize=(10, 6))
plt.bar(['Yes', 'No'], [mean_yes, mean_no], yerr=[sem_yes, sem_no], capsize=5)
plt.title(f'Mean Training Hours by Clicked Suspicious Link\nT-test p-value: {p_value:.4f}')
plt.xlabel('Clicked Suspicious Link (Yes/No)')
plt.ylabel('Mean Training Hours (0-10)')
plt.grid(True)
plt.show()