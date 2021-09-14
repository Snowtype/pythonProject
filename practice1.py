import pandas as pd

df1 = pd.read_excel('Data05.xlsx')

df1 = pd.read_excel('Data05.xlsx', skiprows=1) #제일 위에 행 삭제함

a = df1.shape
b = df1.columns

print(a)
print(b)
