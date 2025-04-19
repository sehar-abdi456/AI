import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Creating a DataFrame and calculating Tax and Net Salary
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Salary': [50000, 60000, 45000, 80000]
}
df1 = pd.DataFrame(data1)
df1['Tax'] = df1['Salary'] * 0.10
df1['Net Salary'] = df1['Salary'] - df1['Tax']
print("1. Updated DataFrame with Tax and Net Salary:")
print(df1)

# 2. Mean ticket fare price for each combination of Sex and Class
data2 = {
    'Sex': ['male', 'female', 'female', 'male', 'female'],
    'Class': ['First', 'Second', 'Third', 'First', 'Second'],
    'Fare': [100, 50, 20, 120, 60]
}
df2 = pd.DataFrame(data2)
mean_fare = df2.groupby(['Sex', 'Class'])['Fare'].mean()
print("\n2. Mean ticket fare price for each combination of Sex and Class:")
print(mean_fare)

# 3. Counting passengers in each Class
passenger_count = df2['Class'].value_counts()
print("\n3. Number of passengers in each Class:")
print(passenger_count)

# 4. Reshaping DataFrame from wide to long format
data4 = {
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 90, 95],
    'Science': [88, 92, 96]
}
df4 = pd.DataFrame(data4)
long_format = pd.melt(df4, id_vars=['Student'], var_name='Subject', value_name='Score')
print("\n4. Reshaped DataFrame in long format:")
print(long_format)

# 5. Converting long format DataFrame back to wide format
data5 = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science'],
    'Score': [85, 90, 95, 88, 92, 96]
}
long_format_df = pd.DataFrame(data5)
wide_format = long_format_df.pivot(index='Student', columns='Subject', values='Score').reset_index()
print("\n5. Converted back to wide format:")
print(wide_format)

# 6. Performing Inner and Left Join
data6_1 = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']}
data6_2 = {'ID': [2, 3, 4], 'Score': [85, 90, 95]}
df6_1 = pd.DataFrame(data6_1)
df6_2 = pd.DataFrame(data6_2)
inner_join = pd.merge(df6_1, df6_2, on='ID', how='inner')
left_join = pd.merge(df6_1, df6_2, on='ID', how='left')
print("\n6. Inner Join:")
print(inner_join)
print("\n6. Left Join:")
print(left_join)

# 8. Total and average salary for each department
data8 = {
    'Department': ['HR', 'IT', 'Finance', 'HR', 'Finance', 'IT'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Salary': [50000, 60000, 55000, 52000, 59000, 61000]
}
df8 = pd.DataFrame(data8)
total_salary = df8.groupby('Department')['Salary'].sum()
average_salary = df8.groupby('Department')['Salary'].mean()
print("\n8. Total Salary for each Department:")
print(total_salary)
print("\n8. Average Salary for each Department:")
print(average_salary)

# 9. Handling missing values
data9 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, np.nan, 22, 32],
    'Salary': [50000, 60000, np.nan, 80000]
}
df9 = pd.DataFrame(data9)
mean_age = df9['Age'].mean()
df9['Age'].fillna(mean_age, inplace=True)
df9_cleaned = df9.dropna(subset=['Salary'])
print("\n9. DataFrame after replacing missing values in the Age column:")
print(df9)
print("\n9. DataFrame after dropping rows with missing Salary:")
print(df9_cleaned)

# 10. Line and Bar plot for Month vs. Sales
data10 = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [300, 400, 500, 600, 700]
}
df10 = pd.DataFrame(data10)
plt.figure(figsize=(8, 5))
plt.plot(df10['Month'], df10['Sales'], marker='o', linestyle='-', color='blue', label='Sales')
plt.title('Line Plot for Month vs. Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(df10['Month'], df10['Sales'], color='green', label='Sales')
plt.title('Bar Plot for Month vs. Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(axis='y')
plt.legend()
plt.show()

# 11. Convert date to datetime and filter Sales > 300
data11 = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Sales': np.random.randint(100, 500, size=5)
}
df11 = pd.DataFrame(data11)
df11['Date'] = pd.to_datetime(df11['Date'])
filtered_df11 = df11[df11['Sales'] > 300]
print("\n11. Original DataFrame:")
print(df11)
print("\n11. Filtered DataFrame (Sales > 300):")
print(filtered_df11)

# 12. Create Series of capital cities
data12 = {
    'USA': 'Washington, D.C.',
    'India': 'New Delhi',
    'Japan': 'Tokyo',
    'France': 'Paris'
}
capital_cities = pd.Series(data12)
print("\n12. Capital Cities Series:")
print(capital_cities)

# 13. Create DataFrame with population and capital
data13 = {
    'Population': [331002651, 1380004385, 126476461, 67081000],
    'Capital': ['Washington, D.C.', 'New Delhi', 'Tokyo', 'Paris']
}
countries_df = pd.DataFrame(data13, index=['USA', 'India', 'Japan', 'France'])
print("\n13. Countries DataFrame:")
print(countries_df)

# 14. Analyzing Titanic Dataset (Assume titanic.csv is present)
# Uncomment the below lines if you have the titanic.csv file
# df14 = pd.read_csv('titanic.csv')
# num_columns = len(df14.columns)
# print(f"\n14. Number of columns in the Titanic dataset: {num_columns}")
# print("Column names:", df14.columns.tolist())
# print("\nFirst few rows:")
# print(df14.head())

# 15. Create a DataFrame for 3 cities
matrix15 = {
    'Population (millions)': [8.4, 3.8, 5.0],
    'Size (km2)': [789, 605, 1214],
    'Population Density (people per km2)': [10600, 6298, 4127]
}
cities15 = ['New York', 'Paris', 'Tokyo']
df15 = pd.DataFrame(matrix15, index=cities15)
print("\n15. Cities DataFrame:")
print(df15)

# 16. Extracting data from city DataFrame
data16 = {
    'Population (millions)': [10.4, 5.8, 7.2, 3.6],
    'Size (km2)': [1200, 900, 850, 600],
    'Population Density (people per km2)': [8670, 6444, 8470, 6000]
}
cities16 = ['CityA', 'CityB', 'CityC', 'CityD']
df16 = pd.DataFrame(data16, index=cities16)
pop_density_all = df16['Population Density (people per km2)']
data_cityC_index = df16.loc['CityC']
data_cityC_row = df16.iloc[2]
print("\n16. Population Density for All Cities:")
print(pop_density_all)
print("\n16. Data for the third city (using index - CityC):")
print(data_cityC_index)
print("\n16. Data for the third city (using row number - 2):")
print(data_cityC_row)
