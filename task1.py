from data import dataset

#   Написати функцію, що зберігає інформацію про улюблену страву користувача у певній країні
#   Викликати функцію


def addStudentSkill(student, company, skill,studpaper=""):
    if student in dataset:
        if company in dataset[student]["company"]:
            dataset[student]["company"][company].add(skill)
        else:
            dataset[student]["company"][company] = {skill}
    else:
        dataset[student]={"studpaper":studpaper,"company":{company:{skill}}}
    return dataset



print("Task 1")

#Додати нового студента та вміння у новій компанії
addStudentSkill("student2","microsoft","running","KM-212121")

#Додати існуючому студенту нове вміння у новій компанії
addStudentSkill("student1","ibm","math")

#Додати існуючому студенту нове вміння в існуючій компанії
addStudentSkill("student1","privat24","diving")

print(dataset)


print("\n\n")