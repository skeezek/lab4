import pandas as pd
from datetime import datetime
try:
    df = pd.read_csv(r'/Users/skeezek/PycharmProjects/lab4/employees.csv')
except FileNotFoundError:
    print('Неможливо створити .xlsx файл')
    exit()

current_year = datetime.now().year
df['Вік'] = df['Дата народження'].apply(lambda x: current_year - int(x.split('-')[0]))

with pd.ExcelWriter(r'/Users/skeezek/PycharmProjects/lab4/employees_range.xlsx') as writer:
    df.to_excel(writer,sheet_name='All',index=False)
    df[df['Вік'] < 18].to_excel(writer, sheet_name='younger_18', index=False)
    df[(df['Вік'] >=18) & (df['Вік']  <= 45)].to_excel(writer,sheet_name ='18-45',index=False)
    df[(df['Вік'] >=45) & (df['Вік']  <= 70)].to_excel(writer,sheet_name ='45-70',index=False)
    df[df['Вік'] > 70].to_excel(writer,sheet_name ='Older_70',index=False)

print('Успішно завершено')