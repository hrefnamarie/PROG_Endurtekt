dog_age = int(input("Input dog's age: "))
human_age = 0

while True:
    if dog_age <= 0:
        print ("Invalid age")
        break
    
    if dog_age > 16:
        print ("Invalid age")
        break

    if dog_age == 1:
        human_age = 15
        print ("Human age:",human_age)
        break
    
    elif dog_age == 2:
        human_age = 24
        print ("Human age:",human_age)
        break

    else :
        human_age = (dog_age+1)*6
        print("Human age:",human_age)
        break