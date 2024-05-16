import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from sklearn import svm
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import random #This is for testing ONLY.

# First is to obtain the data from the Comma Separate Values (.csv) file

maindata = pd.read_csv('C:/Users/beelink/Documents/VALLE/Brianne_Training_Data.csv', encoding='latin1')

# Use the data frame created to train the model using Support Vector Machine (SVM)
# Separate the contents of the dataframe into input and output variables.

x_data = maindata[['CIRCUIT1', 'CIRCUIT2', 'COMPAD1', 'COMPAD2', 'COMPARC', 'COMPLAW', 'COMPNET', 'COMPORG', 'DATACOM',
       'DATASTRUC', 'DESPRO1', 'DESPRO2', 'DIGIPRO', 'ELECTRO1', 'ELECTRO2', 'LCAST1', 'LCAST2', 'MICROPR', 'OPERSYS', 'PRACTICUM']]
y_data = maindata[['FIELD']]

# Convert the separated data frame into array as this is the accepted data structure of the SVM.

x_array = np.asarray(x_data)
y_array = np.asarray(y_data)

# Apply SVM

classifier = svm.SVC(kernel = 'linear')
classifier.fit(x_array, y_array)

# Generate an array of 20 random numbers from 80 to 100 for testing
random_grades = [[random.randint(80, 100) for _ in range(20)]]

# Test the classifier
field_predict = classifier.predict(random_grades)

## Build the User Interface

# Create main Tkinter window
root = tk.Tk()
root.title("Grade to Industry Recommender")
root.configure(bg = "lightgray")

# Define the funtion needed
def clickButton():
    grade01 = grade01_input.get()
    grade02 = grade02_input.get()
    grade03 = grade03_input.get()
    grade04 = grade04_input.get()
    grade05 = grade05_input.get()
    grade06 = grade06_input.get()
    grade07 = grade07_input.get()
    grade08 = grade08_input.get()
    grade09 = grade09_input.get()
    grade10 = grade10_input.get()
    grade11 = grade11_input.get()
    grade12 = grade12_input.get()
    grade13 = grade13_input.get()
    grade14 = grade14_input.get()
    grade15 = grade15_input.get()
    grade16 = grade16_input.get()
    grade17 = grade17_input.get()
    grade18 = grade18_input.get()
    grade19 = grade19_input.get()
    grade20 = grade20_input.get()
    grades_list = [grade01, grade02, grade03, grade04, grade05, grade06, grade07, grade08, grade09, grade10,
                   grade11, grade12, grade13, grade14, grade15, grade16, grade17, grade18, grade19, grade20]
    
    grades_array = []

    for any_grade in grades_list:
        if not any_grade.isdigit():
            new_text = "One of the inputs is text, decimal, or at least one entry is blank, \n please enter a whole number between 75 to 100."
            output_label.config(text=new_text)
        elif not (75 <= int(any_grade) <= 100):
            new_text = "Please enter valid values between 75 to 100."
            output_label.config(text=new_text)
        else:
            grades_array.append(any_grade)

    grades_final = [grades_array]
    if len(grades_final[0]) == 20:
        new_classify = classifier.predict(grades_final)
        new_text = new_classify[0]
        output_label.config(text= "The recommended industry for this student is \n" + new_text)

output_text = None

# Create the Widgets
title_label = tk.Label(
    root, 
    text="EduAid: INDUSTRY RECOMMENDER SYSTEM", 
    font=("Helvetica", 30, "bold"), 
    fg="maroon", 
    bg="lightgray", 
    padx=50, 
    pady=10
)
title_label.grid(row = 0, column = 0, columnspan = 8)

dept_label = tk.Label(
    root, 
    text="College of Computer Studies and Engineering \n LORMA Colleges, Inc", 
    font=("Helvetica", 21, "bold"), 
    fg="maroon", 
    bg="lightgray", 
    padx=10, 
    pady=10
)
dept_label.grid(row = 1, column = 0, columnspan = 8)

instruc_label = tk.Label(
    root, 
    text="Instructions: Input the grades (whole number) of the student on each of the subject identified. Click the 'Recommend' button to recommend an industry", 
    font=("Helvetica", 12, "italic"), 
    bg="lightgray", 
    padx=10, 
    pady=10
)
instruc_label.grid(row = 2, column = 0, columnspan = 8)

ccwhat = Image.open('C:/Users/beelink/Documents/VALLE/CCSE_Logo.png')
resized_ccse_logo = ccwhat.resize((144,144))
ccse_logo = ImageTk.PhotoImage(resized_ccse_logo)
picture_label = tk.Label(root, image = ccse_logo, bg = "lightgray")
picture_label.grid(row=1,column=6, columnspan=2)

lorma_logo = tk.PhotoImage(file = 'C:/Users/beelink/Documents/VALLE/LORMA_Logo.png')
picture_label = tk.Label(root, image = lorma_logo, bg = "lightgray")
picture_label.grid(row=1,column=0, columnspan=2)

label_font = ("Arial",12,"bold")
output_font = ("Arial",15,"bold")

grade01_label = tk.Label(root, text="CIRCUIT1:", bg = "lightgray", font = label_font)
grade01_label.grid(row = 3, column = 0, pady = 5)

grade01_input = tk.Entry(root, justify = "center")
grade01_input.grid(row = 3, column = 1, pady = 5)

grade02_label = tk.Label(root, text="CIRCUIT2:", bg = "lightgray", font = label_font)
grade02_label.grid(row = 3, column = 2, pady = 5)

grade02_input = tk.Entry(root, justify = "center")
grade02_input.grid(row = 3, column = 3, pady = 5)

grade03_label = tk.Label(root, text="COMPAD1:", bg = "lightgray", font = label_font)
grade03_label.grid(row = 3, column = 4, pady = 5)

grade03_input = tk.Entry(root, justify = "center")
grade03_input.grid(row = 3, column = 5, pady = 5)

grade04_label = tk.Label(root, text="COMPAD2:", bg = "lightgray", font = label_font)
grade04_label.grid(row = 3, column = 6, pady = 5)

grade04_input = tk.Entry(root, justify = "center")
grade04_input.grid(row = 3, column = 7, pady = 5)

grade05_label = tk.Label(root, text="COMPARC:", bg = "lightgray", font = label_font)
grade05_label.grid(row = 4, column = 0, pady = 5)

grade05_input = tk.Entry(root, justify = "center")
grade05_input.grid(row = 4, column = 1)

grade06_label = tk.Label(root, text="COMPLAW:", bg = "lightgray", font = label_font)
grade06_label.grid(row = 4, column = 2, pady = 5)

grade06_input = tk.Entry(root, justify = "center")
grade06_input.grid(row = 4, column = 3)

grade07_label = tk.Label(root, text="COMPNET:", bg = "lightgray", font = label_font)
grade07_label.grid(row = 4, column = 4, pady = 5)

grade07_input = tk.Entry(root, justify = "center")
grade07_input.grid(row = 4, column = 5)

grade08_label = tk.Label(root, text="COMPORG:", bg = "lightgray", font = label_font)
grade08_label.grid(row = 4, column = 6, pady = 5)

grade08_input = tk.Entry(root, justify = "center")
grade08_input.grid(row = 4, column = 7)

grade09_label = tk.Label(root, text="DATACOM:", bg = "lightgray", font = label_font)
grade09_label.grid(row = 5, column = 0, pady = 5)

grade09_input = tk.Entry(root, justify = "center")
grade09_input.grid(row = 5, column = 1)

grade10_label = tk.Label(root, text="DATASTRUC:", bg = "lightgray", font = label_font)
grade10_label.grid(row = 5, column = 2, pady = 5)

grade10_input = tk.Entry(root, justify = "center")
grade10_input.grid(row = 5, column = 3)

grade11_label = tk.Label(root, text="DESPRO1:", bg = "lightgray", font = label_font)
grade11_label.grid(row = 5, column = 4, pady = 5)

grade11_input = tk.Entry(root, justify = "center")
grade11_input.grid(row = 5, column = 5)

grade12_label = tk.Label(root, text="DESPRO2:", bg = "lightgray", font = label_font)
grade12_label.grid(row = 5, column = 6, pady = 5)

grade12_input = tk.Entry(root, justify = "center")
grade12_input.grid(row = 5, column = 7)

grade13_label = tk.Label(root, text="DIGIPRO:", bg = "lightgray", font = label_font)
grade13_label.grid(row = 6, column = 0, pady = 5)

grade13_input = tk.Entry(root, justify = "center")
grade13_input.grid(row = 6, column = 1)

grade14_label = tk.Label(root, text="ELECTRO1:", bg = "lightgray", font = label_font)
grade14_label.grid(row = 6, column = 2, pady = 5)

grade14_input = tk.Entry(root, justify = "center")
grade14_input.grid(row = 6, column = 3)

grade15_label = tk.Label(root, text="ELECTRO2:", bg = "lightgray", font = label_font)
grade15_label.grid(row = 6, column = 4, pady = 5)

grade15_input = tk.Entry(root, justify = "center")
grade15_input.grid(row = 6, column = 5)

grade16_label = tk.Label(root, text="LCAST1:", bg = "lightgray", font = label_font)
grade16_label.grid(row = 6, column = 6, pady = 5)

grade16_input = tk.Entry(root, justify = "center")
grade16_input.grid(row = 6, column = 7)

grade17_label = tk.Label(root, text="LCAST2:", bg = "lightgray", font = label_font)
grade17_label.grid(row = 7, column = 0, pady = 5)

grade17_input = tk.Entry(root, justify = "center")
grade17_input.grid(row = 7, column = 1)

grade18_label = tk.Label(root, text="MICROPR:", bg = "lightgray", font = label_font)
grade18_label.grid(row = 7, column = 2, pady = 5)

grade18_input = tk.Entry(root, justify = "center")
grade18_input.grid(row = 7, column = 3)

grade19_label = tk.Label(root, text="OPERSYS:", bg = "lightgray", font = label_font)
grade19_label.grid(row = 7, column = 4, pady = 5)

grade19_input = tk.Entry(root, justify = "center")
grade19_input.grid(row = 7, column = 5)

grade20_label = tk.Label(root, text="PRACTICUM:", bg = "lightgray", font = label_font)
grade20_label.grid(row = 7, column = 6, pady = 5)

grade20_input = tk.Entry(root, justify = "center")
grade20_input.grid(row = 7, column = 7)

predict_button = tk.Button(root, text="Recommend", font = ("Arial", 18, "bold"), command = clickButton)
predict_button.grid(row = 8, column=0, columnspan=2, pady=10)

output_label = tk.Label(root, bg = "lightgray", font = output_font, text=output_text)
output_label.grid(row = 8, column=2, columnspan=6, pady=10)

# Run the Tkinter event loop
root.mainloop()

