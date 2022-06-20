#Christian Lara
#000983220
#7/15/2021
#7/14/2021
#This program is made to keep track and calculete the
# average rainfall ina given amount of years. The program uses while
#lopps to validate the user input

#declare the variables
NUMBER_OF_MONTHS = 12
monthCounter = 0
totalInchesOfRainfall = 0.0
averageRainfall = 0.0
yearCount = 1
validYear = False
validRainfallAmount = False

#ask for fist user input
numberOfYears = int(input('Enter number of years: '))
#validates the year to be grather than zero
while not validYear:
    if numberOfYears > 0:
        validYear = True
    else:
        print('Invalid entry. Number of years must be greater than zero.')
        numberOfYears = int(input('Reenter number of years: '))
        validYear = False

#this loop will loop until the total number of years have been iterated
while yearCount <= numberOfYears:
    print('Enter monthly rainfall amount for year ' + str(yearCount))
    monthNum = 1
    #this loops asks the user for inpout of each month of the year
    while monthNum <= NUMBER_OF_MONTHS:
        inchesOfRainInput = float(input('Enter rainfall for month ' + str(monthNum) + ':'))

        #this loop validates the rainfall amount ionput
        while not validRainfallAmount:
            if inchesOfRainInput >= 0:
                validRainfallAmount = True
            else:
                print('Invalid entry. Monthly rainfall must be greater than or equal to zero.')
                inchesOfRainInput = float(input('Reenter rainfall for month ' + str(monthNum) + ':'))
                validRainfallAmount = False

        #this are the accomulators keeping the total of each data
        totalInchesOfRainfall = totalInchesOfRainfall + inchesOfRainInput
        monthCounter = monthCounter + 1
        monthNum = monthNum + 1
        validRainfallAmount = False

    #add one to year count to increace the year
    yearCount = yearCount + 1

#calculate the average rain fall
averageRainfall = totalInchesOfRainfall / monthCounter

#display the results of the accomulators and the formulas
print('Number of months: ' + str(monthCounter))
print('Total inches of rainfall: ' + str(format(totalInchesOfRainfall, '.2f')))
print('Average rainfall: ' + str(format(averageRainfall, '.2f')))
