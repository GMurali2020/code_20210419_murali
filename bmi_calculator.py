import pandas as pd
import numpy as np

d=pd.read_json('health_risk.txt')

df=pd.DataFrame(d)
#df
m=df['HeightCm']/100
df1=df['WeightKg']/m
df['Bmi']=df1
#df

def health_risk(weights):
    if 18.4>=24.9:
         return "Malnutrition risk"
    elif 25 >= 29.9:
           return "Low risk"
    elif 30>=34.9:
         return "Enhanced risk"
    elif 35 >=39.9:
           return "Medium risk"
    elif 40 >=39.9:
        return "High risk"

l=[]
for weights in df['Bmi']:
       l.append(health_risk(weights))
df['Risk_Factor']=l
print(df)