student_info = {                #Dictionary
    "name": "abhi",
    "age": "10",
    "class": "5"
}
print(student_info)
print(student_info["name"])

ec2_instance_info = [
    {
        "id": "instance=001",
        "type": "t2.micro"
    },
    {
        "id": "instance=002",
        "type": "t2.medium"
    },
    {
        "id": "instance=003",
        "type": "t2.xlarge"
    }
]

print(ec2_instance_info)
print(ec2_instance_info[1]["type"])