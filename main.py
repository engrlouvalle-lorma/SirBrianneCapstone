import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from sklearn import svm
import numpy as np
import pandas as pd
import random

# Load the data from CSV file
maindata = pd.read_csv('C:/Users/slaps/OneDrive/Desktop/tkin/Brianne_Training_Data.csv', encoding='latin1')

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
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Add frames to notebook
notebook.add(tab1, text='Grade to Industry 1')
notebook.add(tab2, text='Grade to Industry 2')
notebook.add(tab3, text='Grade to Industry 3')

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

def create_widgets(tab):
    title_label = tk.Label(
        tab,
        text="EduAid: INDUSTRY RECOMMENDER SYSTEM",
        font=("Helvetica", 30, "bold"),
        fg="maroon",
        bg="lightgray",
        padx=50,
        pady=10
    )
    title_label.grid(row=0, column=0, columnspan=8)

    dept_label = tk.Label(
        tab,
        text="College of Computer Studies and Engineering \n LORMA Colleges, Inc",
        font=("Helvetica", 21, "bold"),
        fg="maroon",
        bg="lightgray",
        padx=10,
        pady=10
    )
    dept_label.grid(row=1, column=0, columnspan=8)

    instruc_label = tk.Label(
        tab,
        text="Instructions: Input the grades (whole number) of the student on each of the subject identified. Click the 'Recommend' button to recommend an industry",
        font=("Helvetica", 12, "italic"),
        fg="white",
        bg="maroon",
        padx=10,
        pady=10
    )
    instruc_label.grid(row=2, column=0, columnspan=8)

    ccwhat = Image.open('C:/Users/slaps/OneDrive/Desktop/tkin/CCSE_Logo.png')
    resized_ccse_logo = ccwhat.resize((144, 144))
    ccse_logo = ImageTk.PhotoImage(resized_ccse_logo)
    picture_label = tk.Label(tab, image=ccse_logo, bg="lightgray")
    picture_label.grid(row=1, column=6, columnspan=2)

    lorma_logo = tk.PhotoImage(file='C:/Users/slaps/OneDrive/Desktop/tkin/LORMA_Logo.png')
    picture_label = tk.Label(tab, image=lorma_logo, bg="lightgray")
    picture_label.grid(row=1, column=0, columnspan=2)

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
        grade_label = tk.Label(tab, text=label, bg="lightgray", font=label_font)
        grade_label.grid(row=row+3, column=col*2, pady=5)
        
        grade_input = tk.Entry(tab, justify="center")
        grade_input.grid(row=row+3, column=col*2+1, pady=5)
        
        grade_inputs.append(grade_input)

    output_label = tk.Label(tab, bg="lightgray", font=output_font)
    output_label.grid(row=8, column=2, columnspan=6, pady=10)
    
    predict_button = tk.Button(tab, text="Recommend", font=("Arial", 18, "bold"), command=lambda: clickButton(output_label, grade_inputs))
    predict_button.grid(row=8, column=0, columnspan=2, pady=10)

    # Button to print the SVM model details
    print_model_button = tk.Button(tab, text="Print Model Details", font=("Arial", 18, "bold"), command=print_svm_model)
    print_model_button.grid(row=9, column=0, columnspan=2, pady=10)

    author_label = tk.Label(tab, bg="lightgray", font=("Arial", 8, "italic"), text="Brianne Mark T. Aquino \n Candidate, MIS 2024")
    author_label.grid(row=10, column=6, columnspan=2)

    return ccse_logo, lorma_logo  # Return references to images to avoid garbage collection

# Create widgets for each tab
ccse_logo1, lorma_logo1 = create_widgets(tab1)
ccse_logo2, lorma_logo2 = create_widgets(tab2)
ccse_logo3, lorma_logo3 = create_widgets(tab3)

# Run the Tkinter event loop
root.mainloop()
