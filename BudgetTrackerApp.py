import matplotlib.pyplot as plt
import datetime

name = []
amount = []
count = int(input("Enter the number of items to be tracked: "))

for i in range(count):
    name.append(input("Enter the name of the item to be tracked: "))
    amount.append(int(input("Enter the amount spent: ")))

# Pie chart
plt.pie(amount, labels=name, autopct="%1.1f%%")
plt.title("Budget Tracker Chart")
#plt.show()#Lesson learned, when show is called, the program will not continue hence save as an image
plt.savefig("BudgetTrackerChart.png")
plt.close()

# Write to file
with open("Me.txt", "w") as file:
    file.write("The time is now "+ str(datetime.datetime.now())+'\n')
    file.write("-"*50+'\n')
    for i in range(count):
        file.write(f"{i+1}. {name[i]:<15} R{amount[i]:>2}\n")
    file.write("-"*50+'\n')
    file.write(f"Total: R{sum(amount)}\n")

