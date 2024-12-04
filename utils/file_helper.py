
def read_file(filepath, handle_line):
    file = open(filepath)

    for line in file:
        handle_line(line)

    file.close()
