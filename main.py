from tkinter import *
from tkinter import filedialog
from tkinter import font


global open_status_name
open_status_name = False

global selected
selected=False



# Functio to create a new file
def new_file():
    my_text.delete(1.0, END)
    root.title("Noob Text Editor New File")
    status_bar.config(text="New File      ")
    global open_status_name
    open_status_name = False



# Function to open a  new file

def open_file():

    # Update status bar............

    my_text.delete(1.0, END)
    text_file = filedialog.askopenfilename(initialdir="C:/Users/TANISHQ/Desktop",
                                           title="Open File",
                                           filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py")))
    status_bar.config(text="Opeaned     ")

    if text_file:
        global open_status_name
        open_status_name = text_file
        #print(open_status_name)

    # Open the file...............
    text_file = open(text_file, 'r')
    stuff = text_file.read()

    my_text.insert(END, stuff)






def save_as_file():

    text_file = filedialog.asksaveasfilename(defaultextension=".txt",
                                             initialdir="C:/Users/TANISHQ/Desktop",
                                             title="Save as",
                                             filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py"))
                                             )
    if text_file:
        status_bar.config(text="Opeaned     ")
        text_file = open(text_file, 'w')
        text_file.write((my_text.get(1.0, END)))
        text_file.close()




def save_file():
    global open_status_name
    #print(open_status_name)
    if open_status_name:
        status_bar.config(text="Saved      ")
        text_file = open(open_status_name, 'w')
        text_file.write((my_text.get(1.0, END)))
        text_file.close()
        status_bar.config(text="Saved      ")

    else:
        save_as_file()






def cut_text(e):
    global selected

    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)



def copy_text(e):
    global selected

    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            root.clipboard_clear()
            root.clipboard_append(selected)



def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)





root = Tk()
root.title("Noob Text Editor")
root.geometry("1200x640")


#Create Main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Scroll Bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)


# Create Text Box
my_text = Text(my_frame, width=97, height=25, font=('Helvetica', 16), selectbackground="blue", selectforeground="white",
               undo=True,
               bg="dark grey",
               fg="white",
               yscrollcommand=text_scroll.set)
my_text.pack()

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit")


edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False))
edit_menu.add_command(label="Copy", command=lambda: copy_text(False))
edit_menu.add_command(label="Paste", command=lambda: paste_text(False))
edit_menu.add_command(label="Redo")
edit_menu.add_command(label="Undo")




# Status bar
status_bar = Label(root, text='Ready     ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

text_scroll.config(command=my_text.yview)




# Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)



root.mainloop()
