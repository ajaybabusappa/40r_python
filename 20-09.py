import csv
import tkinter as tk
from tkinter import messagebox, filedialog
import mysql.connector


conn = mysql.connector.connect(
    host= 'localhost',
    user='root',
    password='Secret@123',
    database = 'employee_db'
)

cursor = conn.cursor()



#---------------Functions--------------
def file_read():
    print('Reading file')
    file_path = filedialog.askopenfilename(filetypes=[('CSV FILES2', '*.csv')])

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cursor.execute('INSERT INTO STUDENT (name, age, grade) values (%s, %s, %s)', (row))
        conn.commit()
        messagebox.showinfo('Success', 'Data inserted')


def fill_grid():
    text_box.config(state=tk.NORMAL)
    text_box.delete('1.0', tk.END)
    cursor.execute('SELECT * FROM STUDENT')
    rows = cursor.fetchall()
    for row in rows:
        text_box.insert(tk.END, f'id: {row[0]}, name: {row[1]}, age: {row[2]}, grade: {row[3]}\n')

    text_box.config(state=tk.DISABLED)



def add_entry():
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    if name and age and grade:
        cursor.execute(
            'INSERT INTO STUDENT (name, age, grade) values (%s, %s, %s)', (name, age, grade)
        )
        conn.commit()
        messagebox.showinfo('Success', 'Added entry')
        fill_grid()
    else:
        messagebox.showwarning('Warning', 'Wrong Inputs')


def update_entry():
    cursor.execute('''
                    update stu
                   set
                   name = %s

                   where id = %s       
                   ''', ())

def delete_entry():
    id = entry_id.get()
    if id:
        cursor.execute('DELETE FROM STUDENT WHERE ID = %s', (id,))
        conn.commit()
        messagebox.showinfo('Sucess', 'Delete done')
        fill_grid()
    else:
        messagebox.showwarning('Warning', 'Invalid Id')



#---------------UI---------------------
root = tk.Tk()
root.geometry('550x550')

root.title('User Managment Flow')

tk.Button(root, text='UPLOAD CSV', command=file_read).pack(pady=20)

text_box = tk.Text(root, height= 10, width=60)
text_box.pack(pady=10)
text_box.config(state=tk.DISABLED)


input_frame = tk.Frame(root)
input_frame.pack()


lable_id = tk.Label(input_frame, text='ID')
lable_id.grid(row=0, column=0, padx=10)

entry_id = tk.Entry(input_frame, width=5,)
entry_id.grid(row=0, column=1,  padx=10)


#Name
lable_name = tk.Label(input_frame, text='NAME')
lable_name.grid(row=0, column=2, padx=10)

entry_name = tk.Entry(input_frame, width=15)
entry_name.grid(row=0, column=3, padx=10)

#Age
lable_age = tk.Label(input_frame, text='AGE')
lable_age.grid(row=0, column=4, padx=10)

entry_age = tk.Entry(input_frame, width=5)
entry_age.grid(row=0, column=5, padx=10)

#grade
lable_grade = tk.Label(input_frame, text='GRADE')
lable_grade.grid(row=0, column=6, padx=10)

entry_grade = tk.Entry(input_frame, width=5)
entry_grade.grid(row=0, column=7, padx=10)



button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text='ADD', command=add_entry).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text='UPDATE', command=update_entry).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text='DELTE', command=delete_entry).grid(row=0, column=2, padx=10)

fill_grid()

root.mainloop()