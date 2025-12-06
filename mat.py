import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 20, 22]
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9]
exam_scores = [50, 55, 60, 63, 68, 72, 78, 85, 90]
ages = [18, 22, 25, 30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55, 60, 62, 65, 70, 72]
load_times = [320, 340, 310, 330, 335, 345, 325, 355, 360, 340, 335, 345, 350, 355, 335, 950]
plt.figure(figsize=(5,4))
plt.plot(months,sales,marker="o")
plt.title("Monthly Sales")
plt.xlabel("months")
plt.ylabel("sales")
plt.grid(True)
plt.show()