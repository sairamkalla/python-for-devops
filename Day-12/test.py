def update_server_config(file_path, key, value):

    with open(file_path, "r") as file:
        lines = file.readline()

    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "/n")
            else:
                file.write(line)

update_server_config("server.config", "MAX_CONNECTIONS", "1000")