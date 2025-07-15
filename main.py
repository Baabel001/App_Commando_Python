import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationaly_combobox.get()
        
        # Course info
        registration_status = reg_status_var.get()
        numcourses = numcourses_spinbox.get()
        numsemesters = numsemesters_spinbox.get()
        
        print(f"First name: {firstname} Last name: {lastname}")
        print(f"Title: {title} Age: {age} Nationality: {nationality}")
        print("--"*10)
        print(f"Courses' number: {numcourses} Semesters' number: {numsemesters} Status: {registration_status}")
    else:
        messagebox.showwarning(title="Error", message="You have not accepted the terns")
        

window = tk.Tk()
window.title("Data Entry Form")

frame = tk.Frame(window)
frame.pack()

user_info_frame = tk.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0,column=0,padx=20,pady=20)

first_name_label = tk.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = tk.Label(user_info_frame, text="last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Ms."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tk.Label(user_info_frame, text="Age")
age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=100)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationaly_label = tk.Label(user_info_frame, text="Nationaly")
nationaly_combobox = ttk.Combobox(user_info_frame, values=["French", "Africa"])
nationaly_label.grid(row=2, column=1)
nationaly_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tk.LabelFrame(frame, text="")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

registered_label = tk.Label(courses_frame, text="Registration Status")

reg_status_var = tk.StringVar(value="Not Registered")
registered_check = tk.Checkbutton(courses_frame, text="Currently Registered",
                                  variable=reg_status_var,
                                  onvalue="Registered",
                                  offvalue="Not registered")
registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

numcourses_label = tk.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tk.Spinbox(courses_frame, from_=0, to='Infinity')
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

numsemesters_label = tk.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tk.Spinbox(courses_frame, from_=0, to='Infinity')
numsemesters_label.grid(row=0,column=2)
numsemesters_spinbox.grid(row=1,column=2)


for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Accept terms
terms_frame = tk.LabelFrame(frame, text="Terms and Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and conditions",
                             variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0,column=0)


# Button
button = tk.Button(frame, text="Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

window.mainloop()