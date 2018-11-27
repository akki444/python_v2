
from data import dataset
from task1 import *

#   Написати рекурсивну функцію, що зберігає інформацію кількість вмінь, що отримав студент
#   Рекурсивно необхідно пройтись по користувачам та по компаніям, де вони працювали.



def recursionByCompany(dataset):
    dataset["company"][]



def recursionByStudents(dataset,sum=0):
    recursionByCompany(dataset[0])
    sum = sum + recursionByCompany(dataset[0])
    recursionByStudents(dataset[1:],sum)



print("Task 3")

result = recursionByStudents()
print(result)

print("\n\n")



