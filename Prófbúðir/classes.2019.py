class Distribution:
    def __init__(self, file_stream=None):
        # Can make instance of class without file strem
        # However if file  stream is sent in dist value will be processed data from file stream
        # If filestream is None set dist value as empty dict
        if file_stream:
            self.__distribution = self.__data_processing(file_stream)
        else:
            self.__distribution = {}

    def __data_processing(self, filestream):
        # make empty dict will be the self dist value
        dist_dict = {}
        # make list of lines from file stream
        # each value in list is str type
        lines_list = filestream.readlines()
        filestream.close()
        # iterate through lines in lines list
        for line in lines_list:
            # clean up line and turn into list
            line_list = line.strip().split()
            for number in line_list:
                # make sure thenumber is int for later calculations
                number = int(number)
                # if the number is not a key in the dict we add it with counter 1
                if number not in dist_dict:
                    dist_dict[number] = 1
                else:
                    # key is in dictionary raise counter by 1
                    dist_dict[number] += 1
        # sort dict by turning into list of tuples, sort it and turn back into dict
        dist = sorted(dist_dict.items())
        return dict(dist)

    def set_distribution(self, distribution):
        # get distribution and sets value
        self.__distribution = distribution

    def __str__(self):
        # get the print statemnet looking pretty
        ret_str = ""
        for key, value in self.__distribution.items():
            ret_str += "{}: {}\n".format(key, value)
        return ret_str

    def average(self):
        # make sum and count values for calc
        dist_sum = 0
        counter = 0
        # raise sum by the number multiplied by its count
        for key, value in self.__distribution.items():
            dist_sum += key * value
            counter += value

        # try to calc average, catch error in case self.__distribution is empty
        try:
            avg = dist_sum/counter
        except ZeroDivisionError:
            avg = 0
        return avg

    def __ge__(self, other):
        # returns True is self avg is bigger or eq to other avg
        # what a prettty one liner
        return self.average() >= other.average()

    def __add__(self, other):
        # take self dist and other dist and merge and create new instance of class
        # set dist and return instance
        new_dist_class = Distribution()
        # Copies the value of self dist into a new dictionary
        new_dist = self.__distribution
        # goes through the other dist and raises count of number if it exists 
        # otherwise it makes a new key, value pair
        for key, value in other.__distribution.items():
            if key not in new_dist:
                new_dist[key] = value
            else:
                new_dist[key] += value

        # set the new distibution to our new class instance and returns
        new_dist_class.set_distribution(new_dist)

        return new_dist_class


def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None

dist1 = Distribution()
dist1.set_distribution({1:5, 2:3, 3:7, 4:4, 5:6, 6:4}) # 1 appears 5 times, 2 appears 3 times, etc.
print("Dist1: ")
print(dist1)
print(dist1.average())

filename = input("Enter filename: ")
file_stream = open_file(filename)

dist2 = Distribution(file_stream)
print("\nDist2: ")
print(dist2)
print(dist2.average())

if dist1 >= dist2:
    print("Dist1 >= Dist2")
else:
    print("Dist2 > Dist1")

dist3 = dist1 + dist2
print("\nDist3: ")
print(dist3)
print(dist3.average())