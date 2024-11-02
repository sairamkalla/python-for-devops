import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it will charge 2 dollars a day")
elif type == "t2.medium":
      print("it will charge 4 dollar a day")
elif type == "t2.xlarge":
      print("it will charge 8 dollar a day")
else:
    print("provide valid instance name")