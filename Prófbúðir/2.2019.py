# constant fyrir fjölda vinnings talna
NUM_OF_WINNING = 5
# const fyrir range
MIN_RANGE = 1
MAX_RANGE = 40

# fall sem opnar skráar streymi or skilar því 
# parameter væri nafn á skrá
def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None

# fall sem les frá skrá  DATA PROCESSING
def data_processing(file_stream):
    # make list of all lines from file stream
    # each value in list is str type
    ret_list = []
    # make empty list
    all_lines_list = file_stream.readlines()
    # iterate through lines in all_lines_list
    for line in all_lines_list:
        # clean up line and turn into list
        stripped_line = line.strip()
        # append cleaned line to return list
        line_list = stripped_line.split()  #split á str breytir automatíst í lista
        # append cleared line to return list 
        ret_list.append(line_list)
    # close stream    
    file_stream.close()    
    return ret_list

# fall sem villutjekkar user_input
def validation_check(user_input):
    # the row does not only contain int
    # the row does not contain exactly 5 int's
    # the row contains int's that are not in the range 1-40
    if len(user_input) is not NUM_OF_WINNING:
        return False
    for number in user_input:
        if number.isdigit() is False:
            return False
        if int(number) < MIN_RANGE or int(number) > MAX_RANGE:
            return False
    return True

# fall fyrir vinnings tölur
def mark_winning(file_list,user_list):
    # Loop through file_list and check if num in user_list
    for line in file_list:
        for i in range(len(line)):
            if line[i] in user_list:
                line[i] += "*"
    return file_list


def print_marked(file_list):
    
    for line in file_list:
        print_str = ""
        for numb in line:
            print_str += numb + " "
    print(print_str)   



def main():
    filename = input("Enter filename: ") 
    file_stream = open_file(filename)
    if not file_stream:
        print("file {} not found!".format(filename))
    else:
        file_list = data_processing(file_stream)
        user_input = input("Enter winning numbers: ")

        user_list = user_input.split(' ')
        valid = validation_check(user_list)
        if not valid:
            print("Winning numbers are invalid!")
        elif valid:
            marked_list = mark_winning(file_list,user_list)
            print_marked(marked_list)
           
# get filename
# send in filename
# handle if nona

main()

