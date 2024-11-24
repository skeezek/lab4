from faker import Faker
import pandas as pd
from datetime import date
import random

fake = Faker(locale='uk_UA') 


num_empl = 2000
employee_list = []

for _ in range(num_empl):
    employee = {}
    gender = 'Ч' if random.random() > 0.4 else 'Ж' 
    
    employee["Ім'я"] = fake.first_name_male() if gender == 'Ч' else fake.first_name_female()
    employee['Прізвище'] = fake.last_name_male()  if gender == 'Ч' else fake.last_name_female()
    employee["По-батькові"] = fake.middle_name_male() if gender == 'Ч' else fake.middle_name_female()
    employee['Стать'] = gender
    employee['Дата народження'] = fake.date_between_dates(date_start=date(1938, 1, 1), date_end=date(2008, 12, 31))  
    employee['Посада'] = fake.random_element(elements=('Manager', 'Developer', 'Analyst', 'HR')) 
    employee['Місто'] = fake.city() 
    employee['Телефон'] = fake.phone_number() 
    employee['Email'] = fake.email() 
    employee_list.append(employee)


random.shuffle(employee_list)

df = pd.DataFrame(employee_list)
print(df)

df.to_csv(r'/Users/skeezek/PycharmProjects/lab4/employees.csv', index=False, encoding='utf-8-sig')
