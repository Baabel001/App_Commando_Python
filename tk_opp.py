import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class DataEntryForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Entry Form")

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        frame = tk.Frame(self.root)
        frame.pack()

        # User Information Frame
        self.user_info_frame = tk.LabelFrame(frame, text="User Information")
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=20)

        self.create_user_info_widgets()

        # Course Information Frame
        self.courses_frame = tk.LabelFrame(frame, text="Course Information")
        self.courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

        self.create_course_info_widgets()

        # Terms and Conditions Frame
        self.terms_frame = tk.LabelFrame(frame, text="Terms and Conditions")
        self.terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

        self.create_terms_widgets()

        # Submit Button
        submit_button = tk.Button(frame, text="Enter Data", command=self.enter_data)
        submit_button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

    def create_user_info_widgets(self):
        # First Name and Last Name
        tk.Label(self.user_info_frame, text="First Name").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.user_info_frame, text="Last Name").grid(row=0, column=1, padx=10, pady=5)

        self.first_name_entry = tk.Entry(self.user_info_frame)
        self.last_name_entry = tk.Entry(self.user_info_frame)
        self.first_name_entry.grid(row=1, column=0, padx=10, pady=5)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)

        # Title
        tk.Label(self.user_info_frame, text="Title").grid(row=0, column=2, padx=10, pady=5)
        self.title_combobox = ttk.Combobox(self.user_info_frame, values=["Mr.", "Ms."])
        self.title_combobox.grid(row=1, column=2, padx=10, pady=5)

        # Age
        tk.Label(self.user_info_frame, text="Age").grid(row=2, column=0, padx=10, pady=5)
        self.age_spinbox = tk.Spinbox(self.user_info_frame, from_=18, to=100)
        self.age_spinbox.grid(row=3, column=0, padx=10, pady=5)

        # Nationality
        tk.Label(self.user_info_frame, text="Nationality").grid(row=2, column=1, padx=10, pady=5)
        self.nationality_combobox = ttk.Combobox(self.user_info_frame, values=["French", "African", "Other"])
        self.nationality_combobox.grid(row=3, column=1, padx=10, pady=5)

    def create_course_info_widgets(self):
        # Registration Status
        tk.Label(self.courses_frame, text="Registration Status").grid(row=0, column=0, padx=10, pady=5)
        self.reg_status_var = tk.StringVar(value="Not Registered")
        self.registered_check = tk.Checkbutton(
            self.courses_frame,
            text="Currently Registered",
            variable=self.reg_status_var,
            onvalue="Registered",
            offvalue="Not Registered"
        )
        self.registered_check.grid(row=1, column=0, padx=10, pady=5)

        # Number of Courses
        tk.Label(self.courses_frame, text="# Completed Courses").grid(row=0, column=1, padx=10, pady=5)
        self.num_courses_spinbox = tk.Spinbox(self.courses_frame, from_=0, to=100)
        self.num_courses_spinbox.grid(row=1, column=1, padx=10, pady=5)

        # Number of Semesters
        tk.Label(self.courses_frame, text="# Semesters").grid(row=0, column=2, padx=10, pady=5)
        self.num_semesters_spinbox = tk.Spinbox(self.courses_frame, from_=0, to=20)
        self.num_semesters_spinbox.grid(row=1, column=2, padx=10, pady=5)

    def create_terms_widgets(self):
        self.accept_var = tk.StringVar(value="Not Accepted")
        self.terms_check = tk.Checkbutton(
            self.terms_frame,
            text="I accept the terms and conditions",
            variable=self.accept_var,
            onvalue="Accepted",
            offvalue="Not Accepted"
        )
        self.terms_check.grid(row=0, column=0, padx=10, pady=5)

    def enter_data(self):
        accepted = self.accept_var.get()
        if accepted == "Accepted":
            # User Info
            firstname = self.first_name_entry.get()
            lastname = self.last_name_entry.get()
            title = self.title_combobox.get()
            age = self.age_spinbox.get()
            nationality = self.nationality_combobox.get()

            # Course Info
            registration_status = self.reg_status_var.get()
            num_courses = self.num_courses_spinbox.get()
            num_semesters = self.num_semesters_spinbox.get()

            # Display Data
            print(f"First name: {firstname} Last name: {lastname}")
            print(f"Title: {title} Age: {age} Nationality: {nationality}")
            print("--" * 10)
            print(f"Courses: {num_courses} Semesters: {num_semesters} Status: {registration_status}")
        else:
            messagebox.showwarning("Error", "You have not accepted the terms")


if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryForm(root)
    root.mainloop()