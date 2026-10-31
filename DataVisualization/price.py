import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gold_df = pd.read_csv(r'C:\Users\ACER\PycharmProjects\KHDL\DataVisualizationWithMatplotlib\gold_monthly_csv.csv')
print(gold_df.head())
print(gold_df.tail())

# Filter data of one year: 2020
gold_df_2020 = gold_df[gold_df['Date'].str.startswith('2020')]

print("\nDữ liệu năm 2020:")
print(gold_df_2020)

plt.plot(gold_df_2020['Date'], gold_df_2020['Price'], marker="o")
plt.title("2020 Price Gold")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(alpha=0.4)
# plt.savefig(r'C:\Users\ACER\Downloads\2020Sales.pdf')
plt.show()

# Draw a function graph: y = x**2 + 5
x = np.arange(-10,10,0.01)
y = x ** 2 + 5
sin_x = 10 * np.sin(x)
plt.plot(x, y, color='red', linewidth=2)
plt.plot(x, sin_x)
plt.title("Basic line plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(alpha=0.4)
plt.show()