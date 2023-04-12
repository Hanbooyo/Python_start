#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset("flights")

plt.figure(figsize=(12,3)) #행, 열 사이즈 설정

print(flights)

sns.barplot(data = flights, x='year', y='passengers')