from tkinter import * 

win = Tk()
win.geometry("312x324") 
win.resizable(0, 0)  
win.title("Calculator")

def btn_click(item):
    global exp
    exp = exp + str(item)
    input_text.set(exp)



def bt_clear(): 
    global exp 
    exp = "" 
    input_text.set("")


def bt_equal():
    global exp
    res = str(eval(exp))
    input_text.set(res)
    exp = ""

exp = ""

input_text = StringVar()

input_frame = Frame(win, width = 600, height= 25, highlightbackground="black",highlightcolor= "black",highlightthickness=2)

input_frame.pack()


input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input_field.pack()


but_frame = Frame(win, width= 300, height= 250, bg= "orange")

but_frame.pack()

clear = Button(but_frame, text= "C", fg= "black", width= 32, height= 3, bd = 0, bg = "#eee", cursor="hand2",command= lambda: bt_clear()).grid(row=0,column= 0,padx=1,pady=1)

div = Button(but_frame, text= "/", fg= "black", width= 10, height= 3, bd = 0, bg = "#eee", cursor="hand2",command= lambda: btn_click("/")).grid(row=0,column= 3,padx=1,pady=1)


seven = Button(but_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(but_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(but_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(but_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 

# def add(a,b):
#     return a + b;

# def sub(a,b):
#     return a - b;

# def  mul(a,b):
#     return a * b;

# def div(a,b):
#     return a / b; 
win.mainloop()