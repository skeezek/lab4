import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv('employees.csv')
except:
    print('Неможливо відкрити файл employees.csv')

gender_counts = df['Стать'].value_counts()

sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='cubehelix')

plt.title('Порівняння кількості чоловіків і жінок')
plt.xlabel('Кількість осіб')
plt.ylabel('Стать')
plt.show()

men_count = 0
women_count = 0

for index, row in df.iterrows():

    if row['Стать'].lower() == 'ч':
        men_count += 1
    elif row['Стать'].lower() == 'ж':
        women_count += 1

print(f"Кількість чоловіків: {men_count}")
print(f"Кількість жінок: {women_count}")

xlsx = pd.ExcelFile('employees_range.xlsx')
df1 = pd.read_excel(xlsx, 'younger_18')
num_18 = df1.shape[0]
print(f'Кількість людей молодше 18 років: {num_18}')

df2 = pd.read_excel(xlsx, '18-45')
num_45 = df2.shape[0]
print(f'Кількість людей у віковому діапазоні 18-45 років: {num_45}')

df3 = pd.read_excel(xlsx, '45-70')
num_70 = df3.shape[0]
print(f'Кількість людей у віковому діапазоні 45-70 років: {num_70}')

df4 = pd.read_excel(xlsx, 'Older_70')
num_older_70 = df4.shape[0]
print(f'Кількість людей старших за 70 років: {num_older_70}')

age_groups = ['<18', '18-45', '45-70', '>70']
num_people = [num_18, num_45, num_70, num_older_70]

plt.bar(age_groups, num_people, color=['blue', 'purple', 'darkblue', 'slateblue'])

plt.title('Кількість людей у кожній віковій групі')
plt.xlabel('Вікова група')
plt.ylabel('Кількість людей')

plt.show()

men_count_18 = sum([1 for gender in df1['Стать'] if gender.lower() == 'ч'])
women_count_18 = sum([1 for gender in df1['Стать'] if gender.lower() == 'ж'])

print(f"Кількість чоловіків молодше 18 років: {men_count_18}")
print(f"Кількість жінок молодше 18 років: {women_count_18}")

men_count_45 = sum([1 for gender in df2['Стать'] if gender.lower() == 'ч'])
women_count_45 = sum([1 for gender in df2['Стать'] if gender.lower() == 'ж'])

print(f"Кількість чоловіків 18-45 років: {men_count_45}")
print(f"Кількість жінок 18-45 років: {women_count_45}")

men_count_70 = sum([1 for gender in df3['Стать'] if gender.lower() == 'ч'])
women_count_70 = sum([1 for gender in df3['Стать'] if gender.lower() == 'ж'])

print(f"Кількість чоловіків 45-70 років: {men_count_70}")
print(f"Кількість жінок 45-70 років: {women_count_70}")

men_count_older_70 = sum([1 for gender in df4['Стать'] if gender.lower() == 'ч'])
women_count_older_70 = sum([1 for gender in df4['Стать'] if gender.lower() == 'ж'])

print(f"Кількість чоловіків старших за 70 років: {men_count_older_70}")
print(f"Кількість жінок старших за 70 років: {women_count_older_70}")

men_counts = [men_count_18, men_count_45, men_count_70, men_count_older_70]
women_counts = [women_count_18, women_count_45, women_count_70, women_count_older_70]

age_groups = ['<18', '18-45', '45-70', '>70']

bar_width = 0.35
index = np.arange(len(age_groups))

fig, ax = plt.subplots()

bar1 = ax.bar(index, men_counts, bar_width, label='Чоловіки', color='blue')
bar2 = ax.bar(index + bar_width, women_counts, bar_width, label='Жінки', color='purple')

# Додавання міток, заголовку та легенди
ax.set_xlabel('Вікова група')
ax.set_ylabel('Кількість людей')
ax.set_title('Порівняння чоловіків і жінок у різних вікових групах')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(age_groups)
ax.legend()

plt.tight_layout()
plt.show()