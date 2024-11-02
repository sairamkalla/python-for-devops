import sys

type = sys.argv[1]

if type == "t2.micro":
    print("ok, we will the instance for you")
else:
    print("your input is not t2.micro, we cannot create")