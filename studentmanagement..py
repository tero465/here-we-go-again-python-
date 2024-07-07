# making a student management system\ 
import time


def delay(n):
  time.sleep(n)


studentMangement = {}


def addStudent(name, marks):
  studentMangement[name] = marks
  print(f'Added name {name}with marks{marks}')


#update the student
def update(name, marks):
  if name in studentMangement:
    studentMangement[name] = marks
    print(f'updated the marks of {name} to {marks}')

  else:
    print(f"{name} is not found")


def delet(name):
  if name in studentMangement:
    del studentMangement[name]
    print(f'Deleted {name}')
  else:
    print(f'{name} is not found')


#display
def display():
  if studentMangement:
    for name, marks in studentMangement.items():
      print(f'{name}:{marks}')
      delay(4)
    else:
      print("no student found")


def main():
  while True:
    print("Student management system")
    delay(2)
    print("1.Add student")
    print("2.Update Student")
    print("3.Delet Student")
    print("4.View  student")
    print("5.Exit from the program")
    delay(4)
    choice = int(input("\nenter a choice"))
    if choice == 1:
      name = input("\nenter a name")
      marks = int(input("\nenter a marks"))
      addStudent(name, marks)
      delay(1)

    elif choice == 2:
      name = input("\nenter a name")
      marks = int(input("\nenter a marks"))
      delay(1)
      update(name, marks)
      delay(1)

    elif choice == 3:
      name = input("\nenter a name")
      delet(name)
      delay(1)

    elif choice == 4:
      display()
      delay(1)

    elif choice == 5:
      print(" \nthank you for using this program")
      break

    else:
      print("\nplease select a valid choice ")


if __name__ == "__main__":
  main()
