import tkinter as tk
from tkinter import ttk, messagebox
import re
import mysql.connector


class mainpage:
    def __init__(self, root):
        self.root = root
        self.root.title('Main Page')
        self.root.geometry('600x400+400+150')
        self.root.resizable(False, False)
        self.frame = tk.Frame(self.root, width=600, height=400, bg='white')
        self.frame.place(x=0, y=0)

        self.title_label = tk.Label(self.frame, text='Parent-Teacher Interaction', bg='white', fg='steel blue', font=('Arial', 20, 'bold'))
        self.title_label.place(relx=0.5, rely=0.1, anchor='center')

        self.title_label = tk.Label(self.frame, text='Select Login Page', bg='white', fg='steel blue', font=('Arial', 16, 'bold'))
        self.title_label.place(relx=0.5, rely=0.3, anchor='center')

        self.teacher_btn = tk.Button(self.frame, text='Teacher Login', bg='white', fg='steel blue', font=('Arial', 14), command=self.authenticate1)
        self.teacher_btn.place(relx=0.5, rely=0.5, anchor='center')

        self.parent_btn = tk.Button(self.frame, text='Parent Login', bg='white', fg='steel blue', font=('Arial', 14), command=self.authenticate2)
        self.parent_btn.place(relx=0.5, rely=0.7, anchor='center')

    def authenticate1(self):
        self.frame.destroy()
        self.teacherlogin = TeacherLogin(self.root)
    
    def authenticate2(self):
        self.frame.destroy()
        self.parentlogin = ParentLogin(self.root)


class ParentLogin:
    def __init__(self, root):
        self.root = root
        self.root.title('Parent Login') 
        self.root.geometry('600x400+400+150')
        self.root.resizable(False, False)
        self.frame = tk.Frame(self.root, width=600, height=400, bg='white', bd=4, relief='ridge')
        self.frame.place(x=0, y=0)

        self.title_label = tk.Label(self.frame, text='Parent Login', bg='white', fg='steel blue', font=('Arial', 20, 'bold'))
        self.title_label.place(relx=0.5, rely=0.1, anchor='center')

        self.name_lbl = tk.Label(self.frame, text='Parent Login', bg='white', fg='steel blue', font=('Arial', 12))
        self.name_lbl.place(relx=0.2, rely=0.3, anchor='center')

        self.pass_lbl = tk.Label(self.frame, text='Password', bg='white', fg='steel blue', font=('Arial', 12))
        self.pass_lbl.place(relx=0.2, rely=0.4, anchor='center')

        self.name_entry = tk.Entry(self.frame, font=('Arial', 12))
        self.name_entry.place(relx=0.5, rely=0.3, anchor='center')

        self.pass_entry = tk.Entry(self.frame, show='*', font=('Arial', 12))
        self.pass_entry.place(relx=0.5, rely=0.4, anchor='center')

        self.submit_btn = tk.Button(self.frame, text='LOGIN', bg='white', fg='steel blue', font=('Arial', 12), command=self.authenticate)
        self.submit_btn.place(relx=0.5, rely=0.6, anchor='center')

        self.submit_btn = tk.Button(self.frame, text='BACK', bg='white', fg='steel blue', font=('Arial', 12), command=self.back_button)
        self.submit_btn.place(relx=0.5, rely=0.7, anchor='center')


    def back_button(self):
        self.frame.destroy()
        self.home = mainpage(self.root)

    def authenticate(self):
        name = self.name_entry.get()
        password = self.pass_entry.get()
        self.name_entry.delete(0, 'end')
        self.pass_entry.delete(0, 'end')
        if name == '' or password == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            cursor.execute('SELECT * FROM Nstudent_t ')
            data = cursor.fetchall()
            data1 = [data[0] for data in data]
            pas = [data[1] for data in data]
            if name in data1 and password in pas:
                messagebox.showinfo('Welcome', 'Login is success')
                self.frame.destroy()
                self.home = Home2(self.root, name)
            else:
                messagebox.showerror('Error', 'Invalid username or password')

class Home2:
    def __init__(self, root, reg):
        self.root= root
        self.root.title('Parent Home Page') 
        self.root.geometry('600x400+400+150')
        self.root.resizable(False, False)
        self.dash_frame = tk.Frame(self.root, width=600, height=400, bg='white') 
        self.dash_frame.place(x=0, y=0)

        self.title_label = tk.Label(self.dash_frame, text='Parent Home Page', bg='white', fg='steel blue', font=('Arial', 20, 'bold'))
        self.title_label.place(relx=0.5, rely=0.1, anchor='center')

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ruthika.k",
            database="slogin"
        )

        if self.connection.is_connected():
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM student_data WHERE regdno = %s', (reg,))
            data = cursor.fetchall()
            for row in data:
                regdno_label = tk.Label(self.dash_frame, text=f'Registration No: {row[0]}', bg='white', fg='steel blue', font=('Arial', 12))
                regdno_label.place(x=170, y=100)
                conducted_label = tk.Label(self.dash_frame, text=f'Conducted: {row[1]}', bg='white', fg='steel blue', font=('Arial', 12))
                conducted_label.place(x=170, y=130)
                attended_label = tk.Label(self.dash_frame, text=f'Attended: {row[2]}', bg='white', fg='steel blue', font=('Arial', 12))
                attended_label.place(x=170, y=160)
                totalfee_label = tk.Label(self.dash_frame, text=f'Total Fee: {row[3]}', bg='white', fg='steel blue', font=('Arial', 12))
                totalfee_label.place(x=170, y=190)
                feepaid_label = tk.Label(self.dash_frame, text=f'Fee Paid: {row[4]}', bg='white', fg='steel blue', font=('Arial', 12))
                feepaid_label.place(x=170, y=220)
                feepaid_label = tk.Label(self.dash_frame, text=f'Fee Due: {row[3]-row[4]}', bg='white', fg='steel blue', font=('Arial', 12))
                feepaid_label.place(x=170, y=250)

        else:
            print("Failed to connect to MySQL database")

        cursor.close()
        self.connection.close()

        self.fee_btn = tk.Button(self.dash_frame, text='LOGOUT', bg='white', fg='steel blue', font=('Arial', 12), command=self.back_button)
        self.fee_btn.place(x = 500,y = 10)

    def back_button(self):
        self.dash_frame.destroy()
        self.home = mainpage(self.root)



class TeacherLogin:
    def __init__(self, root):
        self.root = root
        self.root.title('Teacher Login') 
        self.root.geometry('600x400+400+150')
        self.root.resizable(False, False)
        self.frame = tk.Frame(self.root, width=600, height=400, bg='white', bd=4, relief='ridge')
        self.frame.place(x=0, y=0)

        self.title_label = tk.Label(self.frame, text='Teacher Login', bg='white', fg='steel blue', font=('Arial', 20, 'bold'))
        self.title_label.place(relx=0.5, rely=0.1, anchor='center')

        self.name_lbl = tk.Label(self.frame, text='Teacher Name', bg='white', fg='steel blue', font=('Arial', 12))
        self.name_lbl.place(relx=0.3, rely=0.3, anchor='center')

        self.pass_lbl = tk.Label(self.frame, text='Password', bg='white', fg='steel blue', font=('Arial', 12))
        self.pass_lbl.place(relx=0.3, rely=0.4, anchor='center')

        self.name_entry = tk.Entry(self.frame, font=('Arial', 12))
        self.name_entry.place(relx=0.6, rely=0.3, anchor='center')

        self.pass_entry = tk.Entry(self.frame, show='*', font=('Arial', 12))
        self.pass_entry.place(relx=0.6, rely=0.4, anchor='center')

        self.submit_btn = tk.Button(self.frame, text='LOGIN', bg='white', fg='steel blue', font=('Arial', 12), command=self.authenticate)
        self.submit_btn.place(relx=0.5, rely=0.6, anchor='center')

        self.submit_btn = tk.Button(self.frame, text='BACK', bg='white', fg='steel blue', font=('Arial', 12), command=self.back_button)
        self.submit_btn.place(relx=0.5, rely=0.7, anchor='center')

    def authenticate(self):
        name = self.name_entry.get()
        password = self.pass_entry.get()
        self.name_entry.delete(0, 'end')
        self.pass_entry.delete(0, 'end')
        if name == '' or password == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            cursor.execute('SELECT * FROM nadmint')
            data = cursor.fetchall()
            data1 = [data[0] for data in data]
            pas = [data[1] for data in data]
            if name in data1 and password in pas:
                messagebox.showinfo('Welcome', 'Login is success')
                self.frame.destroy()
                self.home = Home1(self.root)
            else:
                messagebox.showerror('Error', 'Invalid username or password')

    def back_button(self):
        self.frame.destroy()
        self.home = mainpage(self.root)

class Home1:
    def __init__(self, root):
        self.root= root
        self.root.title('Faculty Home Page') 
        self.root.geometry('600x400+400+150')
        self.root.resizable(False, False)
        self.dash_frame = tk.Frame(self.root, width=600, height=400, bg='white') 
        self.dash_frame.place(x=0, y=0)

        self.title_label = tk.Label(self.dash_frame, text='Teacher Home Page', bg='white', fg='steel blue', font=('Arial', 20, 'bold'))
        self.title_label.place(relx=0.5, rely=0.1, anchor='center')

        self.attendance_btn = tk.Button(self.dash_frame, text='Upload Attendance', bg='white', fg='steel blue', font=('Arial', 12), command=self.redirect1)
        self.attendance_btn.place(relx=0.5, rely=0.3, anchor='center')

        self.fee_btn = tk.Button(self.dash_frame, text='Upload Fee Details', bg='white', fg='steel blue', font=('Arial', 12), command=self.redirect2)
        self.fee_btn.place(relx=0.5, rely=0.5, anchor='center')

        self.fee_btn = tk.Button(self.dash_frame, text='Add Student Details', bg='white', fg='steel blue', font=('Arial', 12), command=self.redirect3)
        self.fee_btn.place(relx=0.5, rely=0.7, anchor='center')

        self.fee_btn = tk.Button(self.dash_frame, text='LOGOUT', bg='white', fg='steel blue', font=('Arial', 12), command=self.back_button)
        self.fee_btn.place(x = 500,y = 10)
    
    def redirect1(self):
        self.dash_frame.destroy()
        self.home = uploada1(self.root)

    def redirect2(self):
        self.dash_frame.destroy()
        self.home = uploada2(self.root)
    
    def redirect3(self):
        self.dash_frame.destroy()
        self.home = uploada3(self.root)

    def back_button(self):
        self.dash_frame.destroy()
        self.home = mainpage(self.root)

class uploada1:
    def __init__(self, root):
        self.root = root
        self.root.title('Upload Attendance')
        self.root.geometry('800x500+300+100')
        self.root.resizable(False, False)

        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame)
        self.tree.pack(fill="both", expand=True)

        self.populate_table()

        self.fee_btn = tk.Button(self.frame, text='BACK', bg='white', fg='steel blue', font=('Arial', 12), command=self.back_button)
        self.fee_btn.place(relx=0.5, rely=0.8, anchor='center')

    def back_button(self):
        self.frame.destroy()
        self.home = Home1(self.root)


    def populate_table(self):
        try:
            for row in self.tree.get_children():
                self.tree.delete(row)

            cursor.execute("SELECT regdno, conducted, attended FROM student_data")
            columns = [column[0] for column in cursor.description]
            self.tree["columns"] = columns + ["Edit",]  
            self.tree["show"] = "headings"
            for col in columns:
                self.tree.heading(col, text=col)
            self.tree.heading("Edit", text="Edit")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row + ("Edit",))
            self.tree.bind("<Double-1>", self.edit_row)
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    def edit_row(self, event):
        item = self.tree.selection()[0]
        values = self.tree.item(item, "values")
        self.edit_function(values)

    def edit_function(self, values):
        self.edit_win = tk.Toplevel(self.root)
        self.edit_win.title("Edit Row")

        self.regdno_label = tk.Label(self.edit_win, text="Registration Number:")
        self.regdno_label.grid(row=0, column=0, padx=5, pady=5)
        self.regdno_entry = tk.Entry(self.edit_win)
        self.regdno_entry.grid(row=0, column=1, padx=5, pady=5)
        self.regdno_entry.insert(0, values[0])

        self.conducted_label = tk.Label(self.edit_win, text="Classes Conducted:")
        self.conducted_label.grid(row=1, column=0, padx=5, pady=5)
        self.conducted_entry = tk.Entry(self.edit_win)
        self.conducted_entry.grid(row=1, column=1, padx=5, pady=5)
        self.conducted_entry.insert(0, values[1])

        self.attended_label = tk.Label(self.edit_win, text="Classes Attended:")
        self.attended_label.grid(row=2, column=0, padx=5, pady=5)
        self.attended_entry = tk.Entry(self.edit_win)
        self.attended_entry.grid(row=2, column=1, padx=5, pady=5)
        self.attended_entry.insert(0, values[2])

        self.save_btn = tk.Button(self.edit_win, text="Save", command=lambda: self.save_edit(values[0]))
        self.save_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

    def save_edit(self, regdno):
        new_regdno = self.regdno_entry.get()
        new_conducted = self.conducted_entry.get()
        new_attended = self.attended_entry.get()

        try:
            cursor.execute("UPDATE student_data SET regdno=%s, conducted=%s, attended=%s WHERE regdno=%s",
                           (new_regdno, new_conducted, new_attended, regdno))
            conn.commit()
            self.edit_win.destroy()
            self.populate_table() 
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


class uploada2:
    def __init__(self, root):
        self.root = root
        self.root.title('Upload Fee Details')
        self.root.geometry('800x500+300+100')
        self.root.resizable(False, False)

        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame)
        self.tree.pack(fill="both", expand=True)

        self.populate_table()

        self.fee_btn = tk.Button(self.frame, text='BACK', bg='white', fg='steel blue', font=('Arial', 12), command=self.back_button)
        self.fee_btn.place(relx=0.5, rely=0.8, anchor='center')

    def back_button(self):
        self.frame.destroy()
        self.home = Home1(self.root)

    def populate_table(self):
        try:
            for row in self.tree.get_children():
                self.tree.delete(row)

            cursor.execute("SELECT regdno, totalfee, feepaid FROM student_data")
            columns = [column[0] for column in cursor.description]
            self.tree["columns"] = columns + ["Edit",]
            self.tree["show"] = "headings"
            for col in columns:
                self.tree.heading(col, text=col)
            self.tree.heading("Edit", text="Edit")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row + ("Edit",))
            self.tree.bind("<Double-1>", self.edit_row)
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    def edit_row(self, event):
        item = self.tree.selection()[0]
        values = self.tree.item(item, "values")
        self.edit_function(values)

    def edit_function(self, values):
        self.edit_win = tk.Toplevel(self.root)
        self.edit_win.title("Edit Row")

        self.regdno_label = tk.Label(self.edit_win, text="Registration Number:")
        self.regdno_label.grid(row=0, column=0, padx=5, pady=5)
        self.regdno_entry = tk.Entry(self.edit_win)
        self.regdno_entry.grid(row=0, column=1, padx=5, pady=5)
        self.regdno_entry.insert(0, values[0])

        self.totalfee_label = tk.Label(self.edit_win, text="Total Fee:")
        self.totalfee_label.grid(row=1, column=0, padx=5, pady=5)
        self.totalfee_entry = tk.Entry(self.edit_win)
        self.totalfee_entry.grid(row=1, column=1, padx=5, pady=5)
        self.totalfee_entry.insert(0, values[1])

        self.feepaid_label = tk.Label(self.edit_win, text="Fee Paid:")
        self.feepaid_label.grid(row=2, column=0, padx=5, pady=5)
        self.feepaid_entry = tk.Entry(self.edit_win)
        self.feepaid_entry.grid(row=2, column=1, padx=5, pady=5)
        self.feepaid_entry.insert(0, values[2])

        self.save_btn = tk.Button(self.edit_win, text="Save", command=lambda: self.save_edit(values[0]))
        self.save_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

    def save_edit(self, regdno):
        new_regdno = self.regdno_entry.get()
        new_totalfee = self.totalfee_entry.get()
        new_feepaid = self.feepaid_entry.get()

        try:
            cursor.execute("UPDATE student_data SET regdno=%s, totalfee=%s, feepaid=%s WHERE regdno=%s",
                           (new_regdno, new_totalfee, new_feepaid, regdno))
            conn.commit()
            self.edit_win.destroy()
            self.populate_table()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

class uploada3:
    def __init__(self, root):
        self.root = root
        self.root.title('Add Student Details') 
        self.root.geometry('600x400+400+150')
        self.root.resizable(False, False)
        self.frame = tk.Frame(self.root, width=600, height=400, bg='white', bd=4, relief='ridge')
        self.frame.place(x=0, y=0)

        self.title_label = tk.Label(self.frame, text='Regd No:', bg='white', fg='steel blue', font=('Arial', 12))
        self.title_label.place(relx=0.2, rely=0.2, anchor='center')

        self.name_lbl = tk.Label(self.frame, text='Classes Conducted:', bg='white', fg='steel blue', font=('Arial', 12))
        self.name_lbl.place(relx=0.2, rely=0.3, anchor='center')

        self.pass_lbl = tk.Label(self.frame, text='Class Attended:', bg='white', fg='steel blue', font=('Arial', 12))
        self.pass_lbl.place(relx=0.2, rely=0.4, anchor='center')

        self.pass_lbl = tk.Label(self.frame, text='Total Fee:', bg='white', fg='steel blue', font=('Arial', 12))
        self.pass_lbl.place(relx=0.2, rely=0.5, anchor='center')

        self.pass_lbl = tk.Label(self.frame, text='Fee Paid:', bg='white', fg='steel blue', font=('Arial', 12))
        self.pass_lbl.place(relx=0.2, rely=0.6, anchor='center')

        self.name_entry = tk.Entry(self.frame, font=('Arial', 12))
        self.name_entry.place(relx=0.5, rely=0.2, anchor='center')

        self.conducted_entry = tk.Entry(self.frame, font=('Arial', 12))
        self.conducted_entry.place(relx=0.5, rely=0.3, anchor='center')

        self.attended_entry = tk.Entry(self.frame, font=('Arial', 12))
        self.attended_entry.place(relx=0.5, rely=0.4, anchor='center')

        self.totalfee_entry = tk.Entry(self.frame, font=('Arial', 12))
        self.totalfee_entry.place(relx=0.5, rely=0.5, anchor='center')

        self.feepaid_entry = tk.Entry(self.frame, font=('Arial', 12))
        self.feepaid_entry.place(relx=0.5, rely=0.6, anchor='center')

        self.submit_btn = tk.Button(self.frame, text='ADD', bg='white', fg='steel blue', font=('Arial', 12), command=self.insert_data)
        self.submit_btn.place(x=280, y=300)

        self.submit_btn = tk.Button(self.frame, text='BACK', bg='white', fg='steel blue', font=('Arial', 12), command=self.back_button)
        self.submit_btn.place(x=275, y=340)


    def back_button(self):
        self.frame.destroy()
        self.home = Home1(self.root)
    
    def insert_data(self):
        regdno = self.name_entry.get()
        conducted = int(self.conducted_entry.get())
        attended = int(self.attended_entry.get())
        totalfee = float(self.totalfee_entry.get())
        feepaid = float(self.feepaid_entry.get())
        
        nSpwd = "student"
        pattern = r'^\d{2}b01a\d{2}[a-zA-Z0-9][0-9]'

        if re.match(pattern, regdno):
            messagebox.showinfo('Success!!!', 'Student data is successfully added.')
            self.insert_into_nstudent_t(regdno, nSpwd)
            self.insert_into_student_data(regdno, conducted, attended, totalfee, feepaid)
        else:
            messagebox.showerror('Validation Error', 'Input format is incorrect. Please enter valid registration number.')


    def insert_into_nstudent_t(self, nSname, nSpwd):
        try:
            conn = mysql.connector.connect(host='localhost',
                                           user='root',
                                           password='ruthika.k',
                                           database='slogin')
            cursor = conn.cursor()
            query = "INSERT INTO nstudent_t (nSname, nSpwd) VALUES (%s, %s)"
            cursor.execute(query, (nSname, nSpwd))
            conn.commit()
        except Exception as e:
            print("Error inserting into nstudent_t table:", e)
        finally:
            cursor.close()
            conn.close()

    def insert_into_student_data(self, regdno, conducted, attended, totalfee, feepaid):
        try:
            conn = mysql.connector.connect(host='localhost',
                                           user='root',
                                           password='ruthika.k',
                                           database='slogin')
            cursor = conn.cursor()
            query = "INSERT INTO student_data (regdno, conducted, attended, totalfee, feepaid) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (regdno, conducted, attended, totalfee, feepaid))
            conn.commit()
            self.frame.destroy()
            self.home = uploada3(self.root)
        except Exception as e:
            print("Error inserting into student_data table:", e)
        finally:
            cursor.close()
            conn.close()


root = tk.Tk()
conn = mysql.connector.connect(host='localhost', user='root', password='ruthika.k')
cursor = conn.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS SLOGIN')
cursor.execute('USE SLOGIN')
mainpg = mainpage(root)
root.mainloop()