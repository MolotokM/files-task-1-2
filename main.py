#TASK 1 WITH FILES
def replace_string():
    with open("/Users/mariiasyrykh/Desktop/test.txt", "r") as my_file:
        oldtext = my_file.read()
        print('MY OLD VALUES IN THE TXT FILE: ', oldtext)
    replacetext = oldtext.replace('Hello', 'Bye')
    with open("/Users/mariiasyrykh/Desktop/test.txt", "w") as my_file2:
        my_file2.write(replacetext)
        print('MY NEW VALUES IN THE TXT FILE: ', replacetext)
replace_string()
def del_by_index():
    with open("/Users/mariiasyrykh/Desktop/test.txt") as my_file3:
        lines = my_file3.readlines()
        del lines[1]
        my_file4 = open("/Users/mariiasyrykh/Desktop/test.txt", "w+")
        for line in lines:
            my_file4.write(line)
        print("DELETE BY INDEX 1: ", lines)
del_by_index()

#TASK 2 WITH FILES
with open("/Users/mariiasyrykh/Desktop/test.txt") as text_file:
    lines = text_file.readlines()
    print(lines)
    for line in reversed(lines):
        print (line)