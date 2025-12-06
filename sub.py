import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
fig, axes = plt.subplots(2, 3, figsize=(12, 10))

#line plot
axes[0,0].plot(df["SepalWidthCm"], marker='o', linestyle='-', color='pink')
axes[0,0].set_title("Sepal Width")
axes[0,0].set_xlabel("Index")
axes[0,0].set_ylabel("Sepal Width (cm)")
axes[0,0].grid(True)

#Bar plot
axes[0,1].bar(df["Id"], df["PetalLengthCm"], color='orange')
axes[0,1].set_title("Petal Length by ID")
axes[0,1].set_xlabel("ID")
axes[0,1].set_ylabel("Petal Length (cm)")
axes[0,1].grid(True)


#Histogram plot
axes[1,0].hist(df["SepalLengthCm"], bins=9,color='green', edgecolor='black', alpha=0.7)
axes[1,0].set_title("Sepal Length")
axes[1,0].set_xlabel("Sepal Length (cm)")
axes[1,0].set_ylabel("Frequency")
axes[1,0].grid(True)

#pie plot
Species_count = df["Species"].value_counts()
axes[0,2].pie(Species_count.values, labels=Species_count.index,autopct="%1.1f%%")
axes[0,2].set_title("data Species distribution")
plt.tight_layout()

#box plot
axes[1,1].boxplot(df["SepalLengthCm"], patch_artist=True, boxprops=dict(facecolor="lightblue",linewidth=2)) 
axes[1,1].set_title("sepal length")
axes[1,1].set_ylabel("sepal Length (cm)")
axes[1,1].grid(True)


#scatter plot
axes[1,2].scatter(df["SepalLengthCm"], df["SepalWidthCm"], color='purple')
axes[1,2].set_title("Sepal Length vs Width")
axes[1,2].set_xlabel("Sepal Length (cm)")
axes[1,2].set_ylabel("Sepal Width (cm)")
axes[1,2].grid(True)
plt.tight_layout()
plt.show()