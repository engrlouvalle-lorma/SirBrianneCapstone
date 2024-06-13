import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from sklearn import svm
import numpy as np
import pandas as pd
import random

# SVM Classifier for Computer Engineering
# Load the data from CSV file
maindata = pd.read_csv('C:/Users/LOU BENEDIC/Documents/LORMA 17.0/MIS Brianne/CpE_to_Field.csv', encoding='latin1')

# Separate the contents of the dataframe into input and output variables
x1_data = maindata[['CIRCUIT1', 'CIRCUIT2', 'COMPAD1', 'COMPAD2', 'COMPARC', 'COMPLAW', 'COMPNET', 'COMPORG', 'DATACOM',
                   'DATASTRUC', 'DESPRO1', 'DESPRO2', 'DIGIPRO', 'ELECTRO1', 'ELECTRO2', 'LCAST1', 'LCAST2', 'MICROPR', 'OPERSYS', 'PRACTICUM']]
y1_data = maindata[['PSOC2012']]

# Convert the separated data frame into arrays
x1_array = np.asarray(x1_data)
y1_array = np.asarray(y1_data)

# Apply SVM
classifier_coe = svm.SVC(kernel='linear')
classifier_coe.fit(x1_array, y1_array.ravel())

# SVM Classifier for Information Technology and Computer Science
# Load the data from CSV file
maindata = pd.read_csv('C:/Users/LOU BENEDIC/Documents/LORMA 17.0/MIS Brianne/ITCS_to_Field.csv', encoding='latin1')

# Separate the contents of the dataframe into input and output variables
x2_data = maindata[['COMFUND', 'COMPRO1', 'COMPRO2', 'DATASTRUC', 'WEBAPP1', 'DBMSYS1', 'DATACOM', 'SOFTENG', 'PROFETH',
                   'PRACTIC']]
y2_data = maindata[['PSOC2012']]

# Convert the separated data frame into arrays
x2_array = np.asarray(x2_data)
y2_array = np.asarray(y2_data)

# Apply SVM
classifier_itcs = svm.SVC(kernel='linear')
classifier_itcs.fit(x2_array, y2_array.ravel())

# Upload the suggester dataset
suggester = pd.read_csv('C:/Users/LOU BENEDIC/Documents/LORMA 17.0/MIS Brianne/PSOC2012_to_HTE.csv', encoding='latin1')

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
def clickButton1(output_label, grade_inputs_coe, suggestion):
    grades_list = [entry.get() for entry in grade_inputs_coe]

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
        new_classify_coe = classifier_coe.predict(grades_final)
        new_text_coe = new_classify_coe[0]
        output_label.config(text="Your skills is most fit for: \n" + new_text_coe)
        hte_reco = suggester.loc[suggester['PSOC2012'] == new_classify_coe[0], 'Suggestion']
        if not hte_reco.empty:
            recommendation = hte_reco.values[0]
            suggestion.config(text="You are recommended to have your OJT at: \n" + recommendation)
        else:
            suggestion.config(text="No recommendation found for the given PSOC2012 value.")

def clickButton2(output_label, grade_inputs_itcs, suggestion):
    grades_list = [entry.get() for entry in grade_inputs_itcs]

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
    if len(grades_final[0]) == 10:
        new_classify_itcs = classifier_itcs.predict(grades_final)
        new_text = new_classify_itcs[0]
        output_label.config(text="Your skills is most fit for: \n" + new_text)
        hte_reco = suggester.loc[suggester['PSOC2012'] == new_classify_itcs[0], 'Suggestion']
        if not hte_reco.empty:
            recommendation = hte_reco.values[0]
            suggestion.config(text="You are recommended to have your OJT at: \n" + recommendation)
        else:
            suggestion.config(text="No recommendation found for the given PSOC2012 value.")

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

grade_labels_coe = [
        "CIRCUIT1:", "CIRCUIT2:", "COMPAD1:", "COMPAD2:", "COMPARC:", "COMPLAW:",
        "COMPNET:", "COMPORG:", "DATACOM:", "DATASTRUC:", "DESPRO1:", "DESPRO2:",
        "DIGIPRO:", "ELECTRO1:", "ELECTRO2:", "LCAST1:", "LCAST2:", "MICROPR:",
        "OPERSYS:", "PRACTICUM:"
    ]
    
grade_inputs_coe = []
    
for i, label in enumerate(grade_labels_coe):
    row, col = divmod(i, 4)
    grade_label = tk.Label(tab1, text=label, bg="lightgray", font=label_font)
    grade_label.grid(row=row+3, column=col*2, pady=5)
        
    grade_input = tk.Entry(tab1, justify="center")
    grade_input.grid(row=row+3, column=col*2+1, pady=5)
        
    grade_inputs_coe.append(grade_input)

    output_label1 = tk.Label(tab1, bg="lightgray", font=output_font)
    output_label1.grid(row=8, column=2, columnspan=6, pady=10)

    output_label3 = tk.Label(tab1, bg="lightgray", font=output_font)
    output_label3.grid(row=9, column=2, columnspan=6, pady=10)

    predict_button = tk.Button(tab1, text="Recommend", font=("Arial", 18, "bold"), command=lambda: clickButton1(output_label1, grade_inputs_coe, output_label3))
    predict_button.grid(row=8, column=0, columnspan=2, rowspan = 2, pady=10)

## Information Technology / Computer Science

label_font = ("Arial", 12, "bold")
output_font = ("Arial", 15, "bold")

grade_labels_itcs = [
        "COMFUND:", "COMPRO1:", "COMPRO2:", "DATASTRUC:", "WEBAPP1:", "DBMSYS1:",
        "DATACOM:", "SOFTENG:", "PROFETH:", "PRACTIC:"
    ]
    
grade_inputs_itcs = []
    
for i, label in enumerate(grade_labels_itcs):
    row, col = divmod(i, 4)
    grade_label = tk.Label(tab2, text=label, bg="lightgray", font=label_font)
    grade_label.grid(row=row+3, column=col*2, pady=5)
        
    grade_input = tk.Entry(tab2, justify="center")
    grade_input.grid(row=row+3, column=col*2+1, pady=5)
        
    grade_inputs_itcs.append(grade_input)

    output_label2 = tk.Label(tab2, bg="lightgray", font=output_font)
    output_label2.grid(row=8, column=2, columnspan=6, pady=10)

    output_label4 = tk.Label(tab2, bg="lightgray", font=output_font)
    output_label4.grid(row=9, column=2, columnspan=6, pady=10)    

    predict_button = tk.Button(tab2, text="Recommend", font=("Arial", 18, "bold"), command=lambda: clickButton2(output_label2, grade_inputs_itcs, output_label4))
    predict_button.grid(row=8, column=0, columnspan=2, rowspan = 2, pady=10)

add_common_widget(tab1)
add_common_widget(tab2)

# Run the Tkinter event loop
root.mainloop()
