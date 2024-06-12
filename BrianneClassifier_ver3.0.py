import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from sklearn import svm
import numpy as np
import pandas as pd
import random

# Load the data from CSV file
maindata = pd.read_csv('C:/Users/LOU BENEDIC/Documents/LORMA 17.0/MIS Brianne/Brianne_Training_Data.csv', encoding='latin1')

# Separate the contents of the dataframe into input and output variables
x_data = maindata[['CIRCUIT1', 'CIRCUIT2', 'COMPAD1', 'COMPAD2', 'COMPARC', 'COMPLAW', 'COMPNET', 'COMPORG', 'DATACOM',
                   'DATASTRUC', 'DESPRO1', 'DESPRO2', 'DIGIPRO', 'ELECTRO1', 'ELECTRO2', 'LCAST1', 'LCAST2', 'MICROPR', 'OPERSYS', 'PRACTICUM']]
y_data = maindata[['FIELD']]

# Convert the separated data frame into arrays
x_array = np.asarray(x_data)
y_array = np.asarray(y_data)

# Apply SVM
classifier = svm.SVC(kernel='linear')
classifier.fit(x_array, y_array.ravel())

# Function to print the SVM model details
def print_svm_model():
    support_vectors = classifier.support_vectors_
    coefficients = classifier.coef_
    intercept = classifier.intercept_

    model_details = f"SVM Model Details:\n\nSupport Vectors:\n{support_vectors}\n\nCoefficients:\n{coefficients}\n\nIntercept:\n{intercept}"
    print(model_details)

# Generate an array of 20 random numbers from 80 to 100 for testing
random_grades = [[random.randint(80, 100) for _ in range(20)]]

# Test the classifier
field_predict = classifier.predict(random_grades)

# Build the User Interface
# Create main Tkinter window
root = tk.Tk()
root.title("Grade to Industry Recommender")
root.configure(bg="lightgray")

# Create a Notebook widget for tabs
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, columnspan=8, rowspan=10, sticky='nsew')

# Create frames for each tab
tab1 = tk.Frame(notebook, bg="lightgray")
tab2 = tk.Frame(notebook, bg="lightgray")

# Add frames to notebook
notebook.add(tab1, text='BS Computer Engineering')
notebook.add(tab2, text='BS Info. Tech. and BS Comp. Scie.')

# Upload and/or resize the photos
ccwhat = Image.open('C:/Users/LOU BENEDIC/Documents/LORMA 17.0/MIS Brianne/CCSE_Logo.png')
resized_ccse_logo = ccwhat.resize((144, 144))
ccse_logo = ImageTk.PhotoImage(resized_ccse_logo)

lorma_logo = tk.PhotoImage(file='C:/Users/LOU BENEDIC/Documents/LORMA 17.0/MIS Brianne/LORMA_Logo.png')

# Define the function needed
def clickButton(output_label, grade_inputs):
    grades_list = [entry.get() for entry in grade_inputs]

    grades_array = []

    for any_grade in grades_list:
        if not any_grade.isdigit():
            new_text = "One of the inputs is text, decimal, or at least one entry is blank, \n please enter a whole number between 75 to 100."
            output_label.config(text=new_text)
            return
        elif not (75 <= int(any_grade) <= 100):
            new_text = "Please enter valid values between 75 to 100."
            output_label.config(text=new_text)
            return
        else:
            grades_array.append(any_grade)

    grades_final = [grades_array]
    if len(grades_final[0]) == 20:
        new_classify = classifier.predict(grades_final)
        new_text = new_classify[0]
        output_label.config(text="The recommended industry for this student is \n" + new_text)

# Function to create common widget in each frame
def add_common_widget(frame):
    title_label = tk.Label(
        frame,
        text="EduAid: INDUSTRY RECOMMENDER SYSTEM",
        font=("Helvetica", 30, "bold"),
        fg="maroon",
        bg="lightgray",
        padx=50,
        pady=10
    )
    title_label.grid(row=0, column=0, columnspan=8)

    dept_label = tk.Label(
        frame,
        text="College of Computer Studies and Engineering \n LORMA Colleges, Inc",
        font=("Helvetica", 21, "bold"),
        fg="maroon",
        bg="lightgray",
        padx=10,
        pady=10
    )
    dept_label.grid(row=1, column=0, columnspan=8)

    instruc_label = tk.Label(
        frame,
        text="Instructions: Input the grades (whole number) of the student on each of the subject identified. Click the 'Recommend' button to recommend an industry",
        font=("Helvetica", 12, "italic"),
        fg="white",
        bg="maroon",
        padx=10,
        pady=10
    )
    instruc_label.grid(row=2, column=0, columnspan=8)

    
    picture_label = tk.Label(frame, image=ccse_logo, bg="lightgray")
    picture_label.grid(row=1, column=6, columnspan=2)

    picture_label = tk.Label(frame, image=lorma_logo, bg="lightgray")
    picture_label.grid(row=1, column=0, columnspan=2)

    author_label = tk.Label(frame, bg="lightgray", font=("Arial", 8, "italic"), text="Brianne Mark T. Aquino \n Candidate, MIS 2024")
    author_label.grid(row=10, column=6, columnspan=2)

# Add the widgets specific for each frame

## Computer Engineering

label_font = ("Arial", 12, "bold")
output_font = ("Arial", 15, "bold")

grade_labels = [
        "CIRCUIT1:", "CIRCUIT2:", "COMPAD1:", "COMPAD2:", "COMPARC:", "COMPLAW:",
        "COMPNET:", "COMPORG:", "DATACOM:", "DATASTRUC:", "DESPRO1:", "DESPRO2:",
        "DIGIPRO:", "ELECTRO1:", "ELECTRO2:", "LCAST1:", "LCAST2:", "MICROPR:",
        "OPERSYS:", "PRACTICUM:"
    ]
    
grade_inputs = []
    
for i, label in enumerate(grade_labels):
    row, col = divmod(i, 4)
    grade_label = tk.Label(tab1, text=label, bg="lightgray", font=label_font)
    grade_label.grid(row=row+3, column=col*2, pady=5)
        
    grade_input = tk.Entry(tab1, justify="center")
    grade_input.grid(row=row+3, column=col*2+1, pady=5)
        
    grade_inputs.append(grade_input)

    output_label = tk.Label(tab1, bg="lightgray", font=output_font)
    output_label.grid(row=8, column=2, columnspan=6, pady=10)
    
    predict_button = tk.Button(tab1, text="Recommend", font=("Arial", 18, "bold"), command=lambda: clickButton(output_label, grade_inputs))
    predict_button.grid(row=8, column=0, columnspan=2, pady=10)

## Information Technology / Computer Science

label_font = ("Arial", 12, "bold")
output_font = ("Arial", 15, "bold")

grade_labels = [
        "APPDEV:", "COMPRO1:", "COMPRO2:", "DATASTRUC:", "DISTRUC1:", "IAS1:",
        "IAS2:", "INFOMAN1:", "INFOMAN2:", "INTROCOM:", "MOBDEV1:", "OOP:",
        "QUANTI:", "SOFTENG1:", "TECHNO:", "UI/UX:", "WEBDEV1:", "CAPSPRO1:",
        "CAPSPRO2:", "PRACTIC:"
    ]
    
grade_inputs = []
    
for i, label in enumerate(grade_labels):
    row, col = divmod(i, 4)
    grade_label = tk.Label(tab2, text=label, bg="lightgray", font=label_font)
    grade_label.grid(row=row+3, column=col*2, pady=5)
        
    grade_input = tk.Entry(tab2, justify="center")
    grade_input.grid(row=row+3, column=col*2+1, pady=5)
        
    grade_inputs.append(grade_input)

    output_label = tk.Label(tab2, bg="lightgray", font=output_font)
    output_label.grid(row=8, column=2, columnspan=6, pady=10)
    
    predict_button = tk.Button(tab2, text="Recommend", font=("Arial", 18, "bold"), command=lambda: clickButton(output_label, grade_inputs))
    predict_button.grid(row=8, column=0, columnspan=2, pady=10)

add_common_widget(tab1)
add_common_widget(tab2)

# Run the Tkinter event loop
root.mainloop()
