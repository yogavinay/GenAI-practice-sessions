import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 20, 22]
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9]
exam_scores = [50, 55, 60, 63, 68, 72, 78, 85, 90]
ages = [18, 22, 25, 30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55, 60, 62, 65, 70, 72]
load_times = [320, 340, 310, 330, 335, 345, 325, 355, 360, 340, 335, 345, 350, 355, 335, 950]

# Create pie chart with various parameters
plt.figure(figsize=(10, 8))

plt.pie(
    sales,                          # values for slices
    explode=[0, 0, 0, 0, 0.1, 0],  # explode May slice slightly
    labels=months,                  # month labels
    colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F'],  # custom colors
    autopct='%.1f%%',              # show percentages with 1 decimal
    pctdistance=0.85,               # distance of % labels from center
    shadow=True,                    # add shadow
    labeldistance=1.05,             # distance of labels from pie
    startangle=90,                  # start at 90 degrees (top)
    radius=1.0,                     # size of pie
    counterclock=True,              # counterclockwise
    wedgeprops={'linewidth': 2, 'edgecolor': 'white'},  # white edges between slices
    textprops={'fontsize': 11, 'fontweight': 'bold'},  # text styling
    center=(0, 0),                  # center position
    frame=False,                    # no frame
    rotatelabels=False,             # don't rotate labels
)

plt.title("Monthly Sales Distribution", fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

