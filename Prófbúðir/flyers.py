'''
Skrifið Python forrit sem les upplýsingar úr skránni flights.txt og gerir eftirfarandi:

- Prentar út nöfn allra ferðalanganna í stafrófsröð.
- Fyrir hvern ferðalang prentar út þau lönd sem hann hefur ferðast til í stafrófsröð.
- Prentar út nafn þess ferðalangs sem hefur ferðast til flestra landa og hversu margra landa viðkomandi hefur komið til.

ATH: Ef að margir ferðalangar hafa farið til jafnmargra landa skal prenta út þann fyrsta af þeim.

Hvern ferðalang skal prenta út með eftirfarandi sniði:
Nafn ferðalangsins og tvípunkt.
Sérhvert land í sér línu með tab ("\t") táknið á undan hverju landi. 

'''

def open_file(filename):
    '''Opens the given file, returning its file object if found, otherwise None'''
    try:
        file_object = open(filename, 'r')
        return file_object
    except FileNotFoundError:
        return None


def flyer_dict(file_object):
    ''' Creates a dictionary from the given file stream.
        The name is the key, the set of countries is the value '''
    flyers = {}                         #empty dict
    for line in file_object:            #for each line in text file
        name, country = line.split()    #split line to name and country
        if name not in flyers:          #if the name is not in text file
            flyers[name] = {country}    #then dict only says "country"
        else:
            flyers[name].add(country)   #else add country 
    return flyers
    

def print_dict(flyers):
    ''' Prints info from flyers ordered by key.
        The values is also printed ordered '''
    for name in sorted(flyers.keys()): #fyrir hvert nafn í flyers(keys)
        print("{}:".format(name))      #prenta nafnið
        for country in sorted (flyers[name]): #fyrir hvert land í flyers
            print("\t{}".format(country))  #\t = tab 

def visited_most_countries(flyers):
    countries_count = 0    #create counter
    max_flyer = ' '        #create name var 
    for name, countries in flyers.items(): #fyrir hvert nafn og hvert land
        if len(countries) > countries_count:
            countries_count = len(countries)   #telja löndin 
            max_flyer = name                   #setja nafnið 
    return max_flyer, countries_count      #return hvert nafn og löndum sem hann/hún hefur komið til

 
def print_most_visited(name,count):
    print ()    #prenta auða línu
    print ("{} has been to {} countries".format(name,count))


def main():
    filename = "flights.txt"     
    file_object = open_file(filename)
    flyers = flyer_dict(file_object)
    print_dict(flyers)
    name,count = visited_most_countries(flyers)
    print_most_visited(name,count)

main()