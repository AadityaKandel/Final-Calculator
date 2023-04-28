from tkinter import *
import tkinter.messagebox as tmsg
import threading
import subprocess


root = Tk()
root.minsize(385,450)
root.maxsize(385,450)
root.title('Calculator')


# Creating Functions
def create(frame_name,text):

    button = Button(
        frame_name,
        text=text,
        bg="black",
        fg="white",
        font="comicsansms 14 italic",
        width=10,
        command=lambda:l1.config(text=f"{l1['text']}{text}"),
        borderwidth=0
    )

    button.pack(side=LEFT)
    return button

def create1():

    frame = Frame(
        border=10,
        bg="black"
    )

    return frame

def options():
    b19.config(text="Less",command=options1)
    root.minsize(385,570)
    root.maxsize(385,570)


def options1():
    b19.config(text="More",command=options)
    root.minsize(385,450)
    root.maxsize(385,450)

def history():
    try:
        subprocess.Popen(['notepad.exe', 'history.txt'])
    except:
        pass

def clear():
    l1.config(text="")

def cut():
    l1.config(text=f"{l1['text'][0:-1]}")

def small_bracket():
    global check_small_brackets
    if check_small_brackets==0:
        l1.config(text=f"{l1['text']}(")
        check_small_brackets = 1
    elif check_small_brackets==1:
        l1.config(text=f"{l1['text']})")
        check_small_brackets = 0

def big_bracket():
    global check_big_brackets
    if check_big_brackets==0:
        l1.config(text=f"{l1['text']}[")
        check_big_brackets = 1
    elif check_big_brackets==1:
        l1.config(text=f"{l1['text']}]")
        check_big_brackets = 0

def medium_bracket():
    global check_medium_brackets
    if check_medium_brackets==0:
        l1.config(text=f"{l1['text']}{{")
        check_medium_brackets = 1
    elif check_medium_brackets==1:
        l1.config(text=f"{l1['text']}}}")
        check_medium_brackets = 0

def equals():
    big_number = l1['text']
    replaced = big_number.replace('[','(').replace(']',')').replace('}',')').replace('{','(').replace('^','**')
    if len(str(eval(replaced)))>21:
        tmsg.showwarning('Warning','Answer Is Too Long')
    else:
        try:
            l1.config(text=f"{eval(replaced)}")
            new_answer = l1['text']
            f = open('history.txt','a')
            f.write('\n'+big_number+'='+new_answer)
            f.close()
        except:
            tmsg.showwarning('Warning','Wrong Input')

def how_much():
    l1.config(text=f"{l1['text']}^")

def detect_key(event):

    def press(name,name1,name2):
        if event.keysym == name1:
            name.invoke()
        elif event.keysym == name2:
            name.invoke()

    press(b4,"1",1)
    press(b5,"2",2)
    press(b6,"3",3)
    press(b7,"4",4)
    press(b8,"5",5)
    press(b9,"6",6)
    press(b10,"7",7)
    press(b11,"8",8)
    press(b12,"9",9)
    press(b13,"0",0)
    press(b14,"+","plus")
    press(b15,"-","minus")
    press(b16,"*","asterisk")
    press(b17,"/","slash")
    press(b18,"=","equal")

# Creating Variables
check_shift = 0
check_small_brackets = 0
check_big_brackets = 0
check_medium_brackets = 0

l1 = Label(
    bg="black",
    fg="white",
    font="comicsansms 16 italic",
    width=21,
    state=DISABLED,
)

l1.pack()

f1 = create1()
f2 = create1()
f3 = create1()
f4 = create1()
f5 = create1()
f6 = create1()
f7 = create1()
f8 = create1()
f9 = create1()



# Frame 1
b1 = create(f1,"History")
b2 = create(f1,"C")
b3 = create(f1,"(X)")
f1.pack(anchor=W)

# Frame 2
b4 = create(f2,"1")
b5 = create(f2,"2")
b6 = create(f2,"3")
f2.pack(anchor=W)

# Frame 3
b7 = create(f3,"4")
b8 = create(f3,"5")
b9 = create(f3,"6")
f3.pack(anchor=W)

# Frame 4
b10 = create(f4,"7")
b11 = create(f4,"8")
b12 = create(f4,"9")
f4.pack(anchor=W)

# Frame 5
b13 = create(f5,"0")
b14 = create(f5,"+")
b15 = create(f5,"-")
f5.pack(anchor=W)

# Frame 6
b16 = create(f6,"*")
b17 = create(f6,"/")
b18 = create(f6,"=")
f6.pack(anchor=W)

# Frame 7
b19 = create(f7,"More")
f7.pack(anchor=W)

# Frame 8
b20 = create(f8,"^2")
b21 = create(f8,"^3")
b22 = create(f8,"^?")
f8.pack(anchor=W)

#Frame 9
b23 = create(f9,"()")
b24 = create(f9,"{}")
b25 = create(f9,"[]")
f9.pack(anchor=W)

#Configures
b19.config(
    borderwidth=2,
    pady=10,
    width=32,
    command=options
)
b1.config(command=history)
b2.config(command=clear)
b3.config(command=cut)
b23.config(command=small_bracket)
b24.config(command=medium_bracket)
b25.config(command=big_bracket)
b18.config(command=equals)
b22.config(command=how_much)

root.config(bg="black")
root.bind('<Key>',detect_key)
root.mainloop()
