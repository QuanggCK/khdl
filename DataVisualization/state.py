import matplotlib.pyplot as plt
# Check current ver
#print(f"Current version: {matplotlib.__version__}")

#Create data
months = ["January", "Febuary", "March", "April"]
sales=[123, 253, 533, 12]
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Units (k)")
plt.grid(alpha=0.3)

#Save the plot to disk (must be done be4 the show() function)
plt.savefig(r"C:\Study\Y4S1\DataScience\FileExcel\monthly_sales.png")
plt.show()

