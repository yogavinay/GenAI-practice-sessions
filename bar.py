sns.barplot(
    data=df,
    x="division",         
    y="sales",errorbar="sd")
plt.show()