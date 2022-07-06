#MathQuiz.py
#ICS201-03 Dip Tandel
#January 10th, 2020


import random
import turtle
t = turtle.Turtle() 
import time


#Introduction
print ("Hello fellow mathematician!") #Program will display "Hello fellow mathematician!"
time.sleep(1)  #This means that the code will not move on until a second is over
name = str(input("What is your name?: "))   #Asking for user input, in this case, for the user's name
print ("This quiz consists of 15 multiple choice questions, you will find out your score in the end of the quiz, you can't take your answer back")
time.sleep(6)
print ("don’t worry you can take your time")
time.sleep(2)
print ("The use of Google or other electronic sources is prohibited, you can use a sheet of paper to work on, as well as a calculator")
time.sleep(5)

t.screen.bgcolor("black") #Setting the background color to black
t.penup()   #Lifting up the pen, hence, not writing
t.pencolor("white") #The pen ink is now white
t.setposition(-300,200) #Moving the turtle/pen to (x,y) position
t.pendown()    #Putting the pen back down, hence, writing
t.fillcolor("red")   #From point a(begin) to point b(end), the colour will be filled with fillcolor(red)
t.begin_fill()       #From point a(begin) to point b(end), the colour will be filled with fillcolor(red)
for i in range(2):  #Code repeats x(2) amount of times
    t.forward(600)
    t.right(90)
    t.forward(400) #turtle/pen moves forward x(400) amount of pixels
    t.right(90)   #Right turn (90 degrees) 
t.end_fill()         #From point a(begin) to point b(end), the colour will be filled with fillcolor(red)

t.pencolor("white")
t.penup()
t.right(90)
t.forward(200)
t.left(90)
t.forward(10)
t.write("   Math", font=("Old English Text MT", 120, "normal")) #This prints in text form, whatever i desire(in this case "Math", and also in a certain font and size

t.backward(10) #Simply moves turtle/pen backwards by 10 pixels
t.right(90)
t.forward(200)
t.left(90)
t.forward(10)
t.write(" E-Quiz", font=("Old English Text MT", 120, "normal"))

t.backward(10)
t.right(90)
t.forward(110)
t.left(90)
t.backward(300)
t.pencolor("cyan")
t.write("Press ""Enter"" to Begin", font=("Terminal", 60, "normal"))

r = str(input("input any key or press enter to begin: "))
print ("Good Luck!")    #Regardless of what the user input's, it will always move on and say "Good Luck!"

#Set the value of 'w' to zero, and when a question is answered correctly, it is changed to 1 (this is for future calculations)    
w1 = 0
w2 = 0
w3 = 0
w4 = 0
w5 = 0
w6 = 0
w7 = 0
w8 = 0
w9 = 0
w10 = 0
w11 = 0
w12 = 0
w13 = 0
w14 = 0
w15 = 0

#QUESTION 1
number1 = random.randint(1,3)
#This will choose a number from 1 to 3 and provide the correlating question

if number1 == 1: #if number one is selected out of random, then....
    print ("Q1")
    time.sleep(1)
    print ("      21 - 4x = 9")
    time.sleep(1)
    print ("A: 3")
    print ("B: -3")
    print ("C: 9")
    print ("D: -9")
    ans1 = str(input("What is the value of x? "))  #Asks the user for the answer and if "a"(lowercase and capitalized) is the user's answer, a variable will change to 1, which determines that it is correct and will be used for future calculations 
    if ans1 == "a" or ans1 == "A":
        w1 = w1 + 1
if number1 == 2: #if number two is selected out of random, then....
    print ("Q1")
    time.sleep(1)
    print ("      11 + (-3x) = (-7)")
    time.sleep(1)
    print ("A: -6")
    print ("B: 6")
    print ("C: 2")
    print ("D: -2") 
    ans1 = str(input("What is the value of x? "))
    if ans1 == "b" or ans1 == "B":
        w1 = w1 + 1
if number1 == 3: #if number three is selected out of random, then....
    print ("Q1")
    time.sleep(1)
    print ("      9 * 3x = (-108)")
    time.sleep(1)
    print ("A: -3")
    print ("B: -6")
    print ("C: 4")
    print ("D: -4")
    ans1 = str(input("What is the value of x? "))
    if ans1 == "d" or ans1 == "D":
        w1 = w1 + 1

#QUESTION2
number2 = random.randint(1,3)

if number2 == 1:
    print ("Q2")
    time.sleep(1)
    print("   x^8(x^6)   ")     # "^" means superscript
    print("  ----------  ")
    print("     x^4      ")
    time.sleep(1)
    print ("A: x^18")
    print ("B: x^8")    
    print ("C: x^10")
    print ("D: x^12") 
    ans2 = str(input("What is the simplified form of this expression? "))
    if ans2 == "c" or ans2 == "C":
        w2 = w2 + 1        
if number2 == 2:
    print ("Q2")
    time.sleep(1)
    print("    x^12(x^37)    ")
    print("    ---------     ")
    print("       y^7        ")
    time.sleep(1)
    print ("A: x^49/y^7")
    print ("B: x^49y^7")    
    print ("C: xy^7")
    print ("D: xy^42") 
    ans2 = str(input("What is the simplified form of this expression? "))
    if ans2 == "a" or ans2 == "A":
        w2 = w2 + 1   
if number2 == 3:
    print ("Q2")
    time.sleep(1)
    print("    x^4(y^7) ")
    print("   --------- ")
    print("      x^2    ")
    time.sleep(1)
    print ("A: x^8y^7")
    print ("B: xy^14")    
    print ("C: x^6y^7")
    print ("D: x^2y^7") 
    ans2 = str(input("What is the simplified form of this expression? "))
    if ans2 == "d" or ans2 == "D":
        w2 = w2 + 1

#QUESTION3
number3 = random.randint(1,3)

if number3 == 1:
    print ("Q3")
    time.sleep(1)
    print ("      (-2m + 3) - (5m - 6)")
    time.sleep(1)
    print ("A: 3m - 3")
    print ("B: 3m + 9")    
    print ("C: -7m + 9")
    print ("D: -7m - 3") 
    ans3 = str(input("What is the simplified form of this expression? "))
    if ans3 == "c" or ans3 == "C":
        w3 = w3 + 1      
if number3 == 2:
    print ("Q3")
    time.sleep(1)
    print ("      (14x + 7) + (43m - 6)")
    time.sleep(1)
    print ("A: 14x + 43m + 1")
    print ("B: 21x + 37m")    
    print ("C: 57mx + 1")
    print ("D: 14x + 7 + 43m -6") 
    ans3 = str(input("What is the simplified form of this expression? "))
    if ans3 == "a" or ans3 == "A":
        w3 = w3 + 1
if number3 == 3:
    print ("Q3")
    time.sleep(1)
    print ("      4(-3y + 33) - (8y - 48)")
    time.sleep(1)
    print ("A: -4y + 84")
    print ("B: -20y + 84")    
    print ("C: -4y - 180")
    print ("D: -20y + 180") 
    ans3 = str(input("What is the simplified form of this expression? "))
    if ans3 == "d" or ans3 == "D":
        w3 = w3 + 1

#QUESTION4
number4 = random.randint(1,3)

if number4 == 1:
    print ("Q4")
    time.sleep(1)
    print ("The Equation below can be used to convert between temperatures in degrees Celsius, C, and temperatures in degrees Fahrenheit, F")
    print("      C        F - 32   ")
    print("     ---  =   -------   ")
    print("      5          9      ")
    time.sleep(3)
    print ("A: between 41 and 60 (inclusive)")
    print ("B: less than zero")    
    print ("C: greater than 60")
    print ("D: between 20 and 40 (inclusive)")
    ans4 = str(input("If the temperature in degrees Celcius is 15, the temperature in degrees Fahrenheit is… "))
    if ans4 == "a" or ans4 == "A":
        w4 = w4 + 1
if number4 == 2:
    print ("Q4")
    time.sleep(1)
    print ("The Equation below can be used to convert between temperatures in degrees Celsius, C, and temperatures in degrees Fahrenheit, F")
    print("      C        F - 32   ")
    print("     ---  =   -------   ")
    print("      5          9      ")
    time.sleep(3)
    print ("A: between 60 and 70 (inclusive)")
    print ("B: greater than 80")
    print ("C: less than 60")
    print ("D: between 71 and 80 (inclusive)")
    ans4 = str(input("If the temperature in degrees Celcius is 24, the temperature in degrees Fahrenheit is… "))
    if ans4 == "d" or ans4 == "D":
        w4 = w4 + 1
if number4 == 3:
    print ("Q4")
    time.sleep(1)
    print ("The Equation below can be used to convert between temperatures in degrees Celsius, C, and temperatures in degrees Fahrenheit, F")
    print("      C        F - 32   ")
    print("     ---  =   -------   ")
    print("      5          9      ")
    time.sleep(3)
    print ("A: less than -10")
    print ("B: more than 25")
    print ("C: between 6 and 25 (inclusive)")
    print ("D: between -10 and 5 (inclusive)")
    ans4 = str(input("If the temperature in degrees Celcius is -2, the temperature in degrees Fahrenheit is… "))
    if ans4 == "b" or ans4 == "B":
        w4 = w4 + 1

#QUESTION5
print ("Q5")
time.sleep(1)

t.reset()  #erases all pen drawings and starts from the beginning 
t.pencolor("blue")
t.forward(100)
t.left(115)
t.forward(120)
t.left(130)
t.forward(120)
t.left(120)


t.pencolor("green")
t.penup()
t.setposition(80,1)
t.write("x", font=("Arial", 16, "normal")) 


t.setposition(45,75)
t.write("38", font=("Arial", 10, "normal"))

time.sleep(1)
print ("A: 38 degrees")
print ("B: 71 degrees")
print ("C: 104 degrees")
print ("D: 161 degrees")
ans5 = str(input("What is the value of x? "))
if ans5 == "b" or ans5 == "B":
    w5 = w5 + 1    

#QUESTION6
number6 = random.randint(1,3)

if number6 == 1:
    print ("Q6")
    time.sleep(1)
    print ("A plane flies 2880km in 180 minutes")
    time.sleep(1)
    print ("A: 16km/h")
    print ("B: 720km/h")
    print ("C: 960km/h")
    print ("D: 840 km/h")
    ans6 = str(input("What is its average speed in km/h? "))
    if ans6 == "c" or ans6 == "C":
        w6 = w6 + 1
if number6 == 2:
    print ("Q6")
    time.sleep(1)
    print ("Tom can ride his horse for 28km in 3 and a half hours")
    time.sleep(1)
    print ("A: 9km/h")
    print ("B: 10km/h")
    print ("C: 7km/h")
    print ("D: 8 km/h")
    ans6 = str(input("What is its average speed in km/h? "))
    if ans6 == "d" or ans6 == "D":
        w6 = w6 + 1
if number6 == 3:
    print ("Q6")
    time.sleep(1)
    print ("Julian walks at a speed of 5km/h and it takes him 15 minutes to get to his gym")
    time.sleep(1)
    print ("A: 2.5 km")
    print ("B: 1250 m")
    print ("C: 1.5 km")
    print ("D: 2000 m")
    ans6 = str(input("How far is the gym? "))
    if ans6 == "b" or ans6 == "B":
        w6 = w6 + 1

#QUESTION7
number7 = random.randint(1,3)

if number7 == 1:
    print ("Q7")
    time.sleep(1)
    print ("There are 600 kids in a school, the ratio of boys to girls is 3:5")
    time.sleep(1)
    print ("A: 225 boys and 375 girls")
    print ("B: 375 boys and 225 girls")
    print ("C: 200 boys and 400 girls")
    print ("D: 400 boys and 200 girls")
    ans7 = str(input("How many boys and girls are in this school? "))
    if ans7 == "a" or ans7 == "A":
        w7 = w7 + 1
if number7 == 2:
    print ("Q7")
    time.sleep(1)
    print ("The perimeter of a rectangle is 280cm, the ratio of its length to width is 5:2")
    time.sleep(1)
    print ("A: 4000cm^2")
    print ("B: 16,000cm^2")
    print ("C: 7840cm^2")
    print ("D: 560cm^2")
    ans7 = str(input("Find the area of the rectangle "))
    if ans7 == "a" or ans7 == "A":
        w7 = w7 + 1
if number7 == 3:
    print ("Q7")
    time.sleep(1)
    print ("A jar is filled with pennies and nickels in the ratio of 5:3, there are 30 nickles in the jar")
    time.sleep(1)
    print ("A: 160 coins")
    print ("B: 30 coins")
    print ("C: 80 coins")
    print ("D: 50 coins") 
    ans7 = str(input("How many coins are in the jar? "))
    if ans7 == "c" or ans7 == "C":
        w7 = w7 + 1

#QUESTION8
number8 = random.randint(1,3)

if number8 == 1:
    print ("Q8")
    time.sleep(1)
    print ("        x + y - 4 = 0")
    time.sleep(1)
    print ("A: y = x - 4")
    print ("B: y = -x + 4")
    print ("C: y = 4x + 0")
    print ("D: y = -4x + 0")
    ans8 = str(input("Express the equation in the form y = mx + b "))
    if ans8 == "b" or ans8 == "B":
        w8 = w8 + 1
if number8 == 2:
    print ("Q8")
    time.sleep(1)
    print ("      x - y + 2 = 0")
    time.sleep(1)
    print ("A: y = 2x + 0")
    print ("B: y = -2x + 0")
    print ("C: y = x + 2")
    print ("D: y = -x - 2")
    ans8 = str(input("Express the equation in the form y = mx + b "))
    if ans8 == "c" or ans8 == "C":
        w8 = w8 + 1
if number8 == 3:
    print ("Q8")
    time.sleep(1)
    print ("      x + 4y + 3 = 0")
    time.sleep(1)
    print ("A: y = -x/4 - 3/4")
    print ("B: y = x + 3")
    print ("C: y = -x + 3")
    print ("D: y = x/4 + 3/4")
    ans8 = str(input("Express the equation in the form y = mx + b "))
    if ans8 == "a" or ans8 == "A":
        w8 = w8 + 1

#QUESTION9
print ("Q9")
time.sleep(1)

t.reset()
t.pencolor("white")
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(180)

count = 30
for i in range (9):
    t.setposition(count,0)
    t.pendown()
    t.forward(300)
    t.penup()
    count = count + 30
    if count == 150:
        t.pencolor("blue")
    else:
        t.pencolor("white")
    
t.right(90)
count = 30
for i in range (9):
    t.setposition(0,count)
    t.pendown()
    t.forward(300)
    t.penup()
    count = count + 30
    if count == 150:
        t.pencolor("blue")
    else:
        t.pencolor("white")


count = 30
for i in range (5):
    t.penup()
    t.setposition(150,count)
    t.pencolor("red")
    t.pendown()
    t.backward(10)
    count = count + 60
    
t.left(90)

count = 30
for i in range (5):
    t.penup()
    t.setposition(count,150)
    t.pencolor("red")
    t.pendown()
    t.backward(10)
    count = count + 60

t.penup()
t.setposition(140,135)
t.write("0", font=("Arial", 10, "normal"))

t.penup()
t.setposition(80,135)
t.write("-2", font=("Arial", 10, "normal"))

t.penup()
t.setposition(20,135)
t.write("-4", font=("Arial", 10, "normal"))



t.penup()
t.setposition(200,135)
t.write("2", font=("Arial", 10, "normal"))

t.penup()
t.setposition(260,135)
t.write("4", font=("Arial", 10, "normal"))



t.penup()
t.setposition(135,200)
t.write("2", font=("Arial", 10, "normal"))

t.penup()
t.setposition(135,260)
t.write("4", font=("Arial", 10, "normal"))



t.penup()
t.setposition(135,80)
t.write("2", font=("Arial", 10, "normal"))

t.penup()
t.setposition(135,20)
t.write("4", font=("Arial", 10, "normal"))



t.penup()
t.setposition(210,300)
t.pencolor("yellow")
t.pendown()
t.left(180)
t.right(26.8)
t.forward(330)

time.sleep(1)
print ("A: b = 1 & m = 2")
print ("B: b = 1 & m = -2")
print ("C: b = -1 & m = 2")
print ("D: b = -1 & m = -2")
ans9 = str(input("What is the y-intercept and slope of this line? "))
if ans9 == "a" or ans9 == "A":
    w9 = w9 + 1

#QUESTION10
print ("Q10")
time.sleep(1)

t.reset()
t.pencolor("magenta")
t.forward(200)
t.pencolor("blue")
t.write("C: 2x", font=("Arial", 12, "normal"))
t.pencolor("magenta")
t.forward(50)
t.left(100)
t.forward(170)
t.left(80)
t.forward(120)
t.left(59)
t.forward(197)
t.pencolor("blue")
t.write("     B: x", font=("Arial", 12, "normal"))

t.penup()
t.setposition(100,150)
t.write("A: 4x", font=("Arial", 12, "normal"))

t.penup()
t.setposition(180,150)
t.write("D: 3x", font=("Arial", 12, "normal"))
time.sleep(1)
print ("A: 110")
print ("B: 134")
print ("C: 120")
print ("D: 144")
ans10 = str(input("What is the measure of angle BAD? "))
if ans10 == "d" or ans10 == "D":
    w10 = w10 + 1

#QUESTION11
print ("Q11")
time.sleep(1)

t.reset()
t.pencolor("white")
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(300)
t.left(139.2)
t.forward(266.5)

t.pencolor("orange")
t.penup()
t.setposition(20,1)
t.write("B", font=("Arial", 12, "normal"))
t.setposition(200,1)
t.write("C", font=("Arial", 12, "normal"))
t.setposition(125,130)
t.write("A", font=("Arial", 12, "normal"))
t.setposition(134,110)
t.write("25", font=("Arial", 12, "normal"))
t.setposition(270,1)
t.write("D", font=("Arial", 12, "normal"))

time.sleep(1)
print ("A: 25 degrees")
print ("B: 35 degrees")
print ("C: 45 degrees")
print ("D: 55 degrees")                                                                                            
ans11 = str(input("What is the measure of angle ADC? "))
if ans11 == "b" or ans11 == "B":
    w11 = w11 + 1

#QUESTION12
number12 = random.randint(1,3)

if number12 == 1:
    print ("Q12")
    time.sleep(1)
    print ("The radius of a circle is 8cm")
    time.sleep(1)
    print ("A: 201 cm")
    print ("B: 181 cm")
    print ("C: 221 cm")
    print ("D: 161 cm")
    ans12 = str(input("What is the area of this circle? "))
    if ans12 == "a" or ans12 == "A":
        w12 = w12 + 1
if number12 == 2:
    print ("Q12")
    time.sleep(1)
    print ("The diameter of a circle is 6m")
    time.sleep(1)
    print ("A: 19m")
    print ("B: 9m")
    print ("C: 48m")
    print ("D: 28m")
    ans12 = str(input("What is the area of this circle? "))
    if ans12 == "d" or ans12 == "D":
        w12 = w12 + 1
if number12 == 3:
    print ("Q12")
    time.sleep(1)
    print ("The area of a circle is 254cm")
    time.sleep(1)
    print ("A: 7 cm")
    print ("B: 8 cm")
    print ("C: 9 cm")
    print ("D: 10 cm")
    ans12 = str(input("What is the radius of this circle? "))
    if ans12 == "c" or ans12 == "C":
        w12 = w12 + 1

#QUESTION13
number13 = random.randint(1,3)

if number13 == 1:
    print ("Q13")
    time.sleep(1)
    print ("The diameter of a circle is 14")
    time.sleep(1)
    print ("A: 22")
    print ("B: 44")
    print ("C: 66")
    print ("D: 55")
    ans13 = str(input("What is the circumference of this circle? "))
    if ans13 == "b" or ans13 == "B":
        w13 = w13 + 1

if number13 == 2:
    print ("Q13")
    time.sleep(1)
    print ("The radius of a circle is 10")
    time.sleep(1)
    print ("A: 23")
    print ("B: 43")
    print ("C: 53")
    print ("D: 63")
    ans13 = str(input("What is the circumference of this circle? "))
    if ans13 == "d" or ans13 == "D":
        w13 = w13 + 1

if number13 == 3:
    print ("Q13")
    time.sleep(1)
    print ("The circumference of a circle is 128")
    time.sleep(1)
    print ("A: 20")
    print ("B: 30")
    print ("C: 40")
    print ("D: 50")
    ans13 = str(input("What is the radius of this circle? "))
    if ans13 == "a" or ans13 == "A":
        w13 = w13 + 1

#QUESTION14
number14 = random.randint(1,2)

if number14 == 1:
    print ("Q14")
    time.sleep(1)

    t.reset()
    t.pencolor("white")
    for i in range (3):
        t.forward(150)
        t.left(120)

    t.penup()
    t.left(45)  
    t.forward(150)
    t.right(45)
    t.forward(120)
    t.left(120)
    t.pendown()
    t.forward(120)
    t.left(120)
    t.penup()
    t.forward(120)
    t.left(120)
    t.forward(120)
    t.right(126)
    t.pendown()
    t.forward(130)
    t.right(114)
    t.forward(150)
    t.right(79)
    t.forward(123)

    t.penup()
    t.setposition(75,130)
    t.right(135)
    t.pendown

    for i in range(7):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()


    t.penup()
    t.pencolor("lime")
    t.setposition(40,50)
    t.write("8cm", font=("Arial", 12,"normal"))

    t.setposition(20,-20)
    t.write("12cm", font=("Arial", 12,"normal"))

    t.setposition(190,30)
    t.write("20cm", font=("Arial", 12,"normal"))
    
    time.sleep(1)
    print ("A: 960cm^3")
    print ("B: 1920xcm^3")
    print ("C: 960cm^2")
    print ("D: 1920cm^2")
    ans14 = str(input("What is the volume of the object? "))
    if ans14 == "a" or ans14 == "A":
        w14 = w14 + 1
if number14 == 2:
    print ("Q14")
    time.sleep(1)

    t.reset()
    t.pencolor("white")
    for i in range (3):
        t.forward(150)
        t.left(120)

    t.penup()
    t.left(45)  
    t.forward(150)
    t.right(45)
    t.forward(120)
    t.left(120)
    t.pendown()
    t.forward(120)
    t.left(120)
    t.penup()
    t.forward(120)
    t.left(120)
    t.forward(120)
    t.right(126)
    t.pendown()
    t.forward(130)
    t.right(114)
    t.forward(150)
    t.right(79)
    t.forward(123)

    t.penup()
    t.setposition(75,130)
    t.right(135)
    t.pendown

    for i in range(7):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()


    t.penup()
    t.pencolor("lime")
    t.setposition(40,50)
    t.write("8cm", font=("Arial", 12,"normal"))

    t.setposition(20,-20)
    t.write("12cm", font=("Arial", 12,"normal"))

    t.setposition(190,30)
    t.write("20cm", font=("Arial", 12,"normal"))

    time.sleep(1)
    print ("A: 720cm^2")
    print ("B: 816cm^2")
    print ("C: 960cm^2")
    print ("D: 640cm^2")
    ans14 = str(input("What is the surface area of the object? "))
    if ans14 == "b" or ans14 == "B":
        w14 = w14 + 1

#QUESTION15
print ("Q15")
time.sleep(1)

t.reset()
t.pencolor("brown")
t.penup()
t.right(90)
t.forward(200)
t.pendown()


t.left(160)
t.forward(200)

t.backward(200)
t.right(160)
t.left(180)

t.left(20)
t.forward(200)

t.backward(200)
t.right(20)

for i in range(9):
    t.penup()
    t.forward(10)
    t.pendown()
    t.forward(10)

t.penup()
t.forward(24)
t.left(90)
t.pendown()
for i in range(24):
    t.forward(3)
    t.left(1)
t.left(138)
for i in range(24):
    t.forward(3)
    t.left(1)
t.penup()
t.setposition(0,0)
t.forward(65)
t.right(90)
t.forward(18)
t.right(180)
t.left(60)
t.pendown()
for i in range(24):
    t.forward(3)
    t.left(1)

t.penup()
t.setposition(0,0)
t.left(90)
t.forward(20)
t.left(90)

t.pendown()
for i in range(35):
    t.forward(2)
    t.left(0.4)

t.left(165)
t.penup()
t.forward(7)
for i in range(6):
    t.penup()
    t.forward(10)
    t.pendown()
    t.forward(10)

t.penup()
t.pencolor("gold")
t.setposition(-10,-10)
t.write("10cm", font=("Arial", 10, "normal"))

t.setposition(0,-50)
t.write("12cm", font=("Arial", 10, "normal"))

t.setposition(-70,-240)
t.pendown()
t.left(180)

t.fillcolor("skyblue")
t.begin_fill()
for i in range(2):
    t.forward(140)
    t.right(90)
    t.forward(50)
    t.right(90)
t.end_fill()

t.penup()
t.right(90)
t.forward(41)
t.left(90)
t.forward(6)
t.pencolor("purple")
t.write(" Hint: 𝜋rs + 𝜋r^2", font=("Arial", 14, "normal"))

time.sleep(1)
print ("Hint, 𝜋rs + 𝜋r^2")
time.sleep(1)
print ("A: 267 cm^2") 
print ("B: 283 cm^2")
print ("C: 691 cm^2")
print ("D: 723 cm^2")
ans15 = str(input("Which is the closest to the surface area of the cone? "))
if ans15 == "b" or ans15 == "B":
    w15 = w15 + 1
#I asked the name of the user earlier and this is where it is being used
print ("Congratulations", name,", you are done the quiz")

t.reset()
t.penup()
t.pencolor("white")
t.setposition(-400, 100)
t.pendown()
t.fillcolor("red")
t.begin_fill()
for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

t.pencolor("white")
t.penup()
t.right(90)
t.forward(175)
t.left(90)
t.forward(25)
t.write("Congratulations", font=("Terminal", 120, "normal"))

t.backward(25)
t.right(90)
t.forward(25)

t.forward(110)
t.left(90)
t.forward(85)
t.pencolor("cyan")
t.write("You Completed", font=("Terminal", 48, "normal"))

t.right(90)
t.forward(90)
t.write("  The Quiz", font=("Terminal", 48, "normal"))

time.sleep(3)
totalsum = w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8 + w9 + w10 + w11 + w12 + w13 + w14 + w15  #Calculations to see marks
print ("Here come the results!")
time.sleep(3)
print ("You got...")
time.sleep(5)
print ("Drumroll...")
time.sleep(7)
print ("You got", totalsum, "out of 15 correct")

time.sleep(2)

if w1 == 0:
    print ("Q1 is incorrect")  #Checks if the user got the questions wrong and if so, it tells the user which ones were wrong
    time.sleep(1)
if w2 == 0:
    print ("Q2 is incorrect")
    time.sleep(1)
if w3 == 0:
    print ("Q3 is incorrect")
    time.sleep(1)
if w4 == 0:
    print ("Q4 is incorrect")
    time.sleep(1)
if w5 == 0:
    print ("Q5 is incorrect")
    time.sleep(1)
if w6 == 0:
    print ("Q6 is incorrect")
    time.sleep(1)
if w7 == 0:
    print ("Q7 is incorrect")
    time.sleep(1)
if w8 == 0:
    print ("Q8 is incorrect")
    time.sleep(1)
if w9 == 0:
    print ("Q9 is incorrect")
    time.sleep(1)
if w10 == 0:
    print ("Q10 is incorrect")
    time.sleep(1)
if w11 == 0:
    print ("Q11 is incorrect")
    time.sleep(1)
if w12 == 0:
    print ("Q12 is incorrect")
    time.sleep(1)
if w13 == 0:
    print ("Q13 is incorrect")
    time.sleep(1)
if w14 == 0:
    print ("Q14 is incorrect")
    time.sleep(1)
if w15 == 0:
    print ("Q15 is incorrect") 

print("                                       ")
print("                                       ") 
print("                                       ") 
print("                                       ") 
print("                                       ") 
print("                                       ") 

time.sleep(2)

if totalsum == 15:                                    #Feedback is given depending on how well the user did on the test
    print ("You got a perfect mark, well done!!!")
    print ("You should try again and see if you get a perfect mark again, there should be different questions this time")
if totalsum == 14:
    print ("Amazing! you should try again for a perfect mark, you were so close")
if totalsum == 13:
    print ("You did well, may the pi be with you")
    print ("I suggest you try again for even better of a mark, there will be different questions")
if totalsum == 12:
    print ("Not bad, try again for a better score?")
if totalsum == 11:
    print ("try again?")
if totalsum > 8:
    print ("You can do better, practice and try harder another time, there will be different questions if you do it again")
if totalsum == 8:
    print ("That's way too close to a 50, practice and try harder another time, there will be different questions if you do it again")
if totalsum < 8:
    print ("Better luck next time")
    print ("I suggest you practice a good amount")
    print ("after that, come back and try again for a better score")
    print ("most of the questions should be different each time")


