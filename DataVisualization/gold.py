import pandas as pd
import matplotlib.pyplot as plt
gold_df = pd.read_csv("FileExcel/gold_monthly_csv.csv")
print("10 dong dau")
print(gold_df.head(10))
print("10 dong cuoi")
print(gold_df.tail(10))

#Filter data of 1 year
gold_stat_1996 = gold_df.loc[gold_df['Date'].str.startswith('1996')]
print("Du lieu nam 96")
print(gold_stat_1996)

plt.plot(gold_stat_1996['Date'], gold_stat_1996['Price'], marker="o")
plt.title("1996 Price Gold")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(alpha=0.4)

#Save the plot to disk (must be done be4 the show() function)
plt.savefig(r"C:\Study\Y4S1\DataScience\FileExcel\cjd.png")
plt.show()
