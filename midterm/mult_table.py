mult_number = int(input("Input number to multiply: "))
how_often = int(input("Input how often to multiply: "))

number = mult_number
times = how_often +1

for i in range (1,times):
    print(i*number)


