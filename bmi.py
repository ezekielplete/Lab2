def calculate_bmi(height,weight) :
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = (weight/(height*height))

    if (bmi<18.5) :
        print("You are Underweight !")
    elif (bmi>=18.5 and bmi<=25.0) :
        print("You are normal !")
    elif (bmi > 25.0) :
        print("You are overweight !")

calculate_bmi(weight=100, height=1.4)