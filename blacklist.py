def initialize(blacklist):
    file_object = open("PATH_TO_FILE"+blacklist, "r")
    input_file = file_object.read()
    input_file = input_file.split('\n')
    input_file = input_file[1:len(input_file)-2]
    input_file = list(map(str, input_file))
    return input_file

def check_blacklist(name, phone_number):
    string_check = name+" "+str(phone_number)
    if(string_check) in blacklist_file:
        return True
    else:
        return False

blacklist_file = initialize("blacklist_file.txt")
check_blacklist("Andi",1341441)
