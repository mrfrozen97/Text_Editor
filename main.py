from tkinter import *
from tkinter import filedialog
from tkinter import font
import pandas as pd

global open_status_name
open_status_name = False

global selected
selected=False





class Node:

    def __init__(self, value):

        self.value = value
        self.children = []
        self.end = False


    def add_child(self, child):

        self.children.append(child)

    def get_children(self):
        return self.children

    def get_value(self):
        return self.value

    def set_end(self):
        self.end = True



class Tries:

    def __init__(self):

        self.root = Node('#')
        self.search_list = []

    def add_word(self, word):
        curr = self.root
        for i in word:
            cur_list = [abc.value for abc in curr.get_children()]
            if i in cur_list:
                curr = curr.get_children()[cur_list.index(i)]
            else:
                temp = Node(i)
                curr.add_child(temp)
                curr = temp
        curr.set_end()

    def print_trie(self, root1):
        self.recurssion("", root1)

    def recurssion(self,str1, node):

        if node.end:
            self.search_list.append(str1)
            #print(str1)
       # print([ae.value for ae in node.children])
        for i in node.get_children():
            self.recurssion(str1+i.value, i)

















class FILETXT:

    def __init__(self):
        self.stack_undo = []
        self.stack_redo = []
        pass

    def undo(self):
        print(len(self.stack_undo))
        if len(self.stack_undo)==0:
            print("END")
            return "$end$"

        temp = self.stack_undo.pop()
        self.stack_redo.append(temp)
        return temp

    def redo(self):
        if len(self.stack_redo)==0:
            return -1
        temp = self.stack_redo.pop()

        self.stack_undo.append(temp)
        return temp

    def add_stack(self, txt):
        txt1 = my_text.get(1.0, END)
        #txt1 = txt1.replace(self.get_text(), "")
        self.stack_undo.append(txt1)
        print(self.stack_undo)

    def get_text(self):

        text1 = ""
        for i in self.stack_undo:
            text1+=i
        return text1






text1 = FILETXT()



# Functio to create a new file
def new_file():
    my_text.delete(1.0, END)
    root.title("Noob Text Editor New File")
    status_bar.config(text="New File      ")
    global open_status_name
    open_status_name = False
    text1.stack_undo =[]
    text1.stack_undo= []



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



def undo(e):
    temp_text = text1.undo()
    print(temp_text)
    if temp_text=="$end$":
        my_text.delete(1.0, END)
    else:
        #print(temp_text)
        my_text.delete(1.0, END)
        my_text.insert(1.0, temp_text)



def redo(e):
    temp_text = text1.redo()
    #print(temp_text)
    if temp_text == -1:
        my_text.delete(1.0, END)

    else:
        #print(temp_text)
        my_text.delete(1.0, END)
        my_text.insert(1.0, temp_text)






def recomendation(a):
    text = "abc"
    text_search = my_text.get(1.0, END).split()
    if len(text_search)>0:
        text_search=text_search[-1]
    str2 = ""
    abc = tree.root
    flag = False
    tree.search_list = []
    for i in text_search:
        curr_list = [j.value for j in abc.get_children()]
        # print(curr_list)
        if i in curr_list:
            abc = abc.get_children()[curr_list.index(i)]
            str2 += abc.value
        else:
            flag = True
            break


    tree.recurssion(str2, abc)
    text=""
    for i in tree.search_list[:min(12, len(tree.search_list))]:
        text+=(i+"\n")

    label = Label(root, text=text, bg='#80c1ff', font=30, anchor='nw', justify='left', bd=10)
    label.place(relx=0.83, rely=0.0061, relwidth=0.15, relheight=0.45)







words = []
words_list = pd.read_csv("dictionary.csv")
for i in words_list['A'][:]:
    #print(i)
    j = str(i)

    words.append(j)




tree = Tries()
for i in words:
   tree.add_word(i)













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
               undo=False,
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
edit_menu.add_command(label="Redo", command=lambda: redo(False))
edit_menu.add_command(label="Undo", command=lambda: undo(False))




# Status bar
status_bar = Label(root, text='Ready     ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

text_scroll.config(command=my_text.yview)




# Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-Key-z>', undo)
root.bind('<Control-Key-y>', redo)
root.bind('<Return>', text1.add_stack)
root.bind_all('<Key>', recomendation)



root.mainloop()
