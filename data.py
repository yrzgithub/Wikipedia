from os import system

# system("pip install pyperclip wikipedia")

for i in range(10):
    print()

from wikipedia import exceptions, summary
from pyperclip import copy

while True:
    try:
        data = summary(title=input("Enter the title:"), sentences=10)
        print("\n",data)
        copy(data)

    except exceptions.WikipediaException:
        print("Try with different name..")

    except:
        print("Fatal Error : Some thing went wrong...")
    
    finally:
        for i in range(3):
            print()
