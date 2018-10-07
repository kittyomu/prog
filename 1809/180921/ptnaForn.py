import tkinter as tk
from ptna import *


entry = None
response_area = None
action = None
lb = None
ptna = Ptna("ptna")

def putlog(str):
    lb.insert(tk.END, str)

def prompt():
    p = ptna.name
    if (action.get()) == 0:
        p += " : " + ptna.responder.name
    return p + "> "

def talk():
    value = entry.get()
    if not value:
        response_area.configure(text="なに？")
    else:
        response = ptna.dialogue(value)
        response_area.configure(text=response)
        putlog("> " + value)
        putlog(prompt() + response)
        entry.delete(0, tk.END)
        
def run():
    global entry, response_area, lb, action
    root = tk.Tk()
    root.geometry("880x560")
    root.title("Inteligent Agent : ")
    #フォント
    font = ("Helevetica", 14)
    font_log = ("Helevetica", 11)

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    filemenu = tk.Menu(menubar)
    menubar.add_cascade(label="ファイル", menu=filemenu)
    filemenu.add_command(label="閉じる", command=root.destroy)

    action = tk.IntVar()
    optionmenu = tk.Menu(menubar)
    menubar.add_cascade(label="オプション", menu=optionmenu)
    optionmenu.add_radiobutton(
        label="Responderを表示",
        variable=action,
        value = 0
    )
    optionmenu.add_radiobutton(
        label="Responderを表示しない",
        variable=action,
        value = 1
    )

    canvas = tk.Canvas(
        root,
        width=500,
        height=300,
        relief=tk.RIDGE,
        bd = 2
    )
    canvas.place(x=370, y=0)
    
    img = tk.PhotoImage(file = 'img1.gif')
    canvas.create_image(
        0,
        0,
        image=img,
        anchor = tk.NW
    )

    response_area = tk.Label(
        root,
        width=50,
        height=10,
        bg="yellow",
        font=font,
        relief=tk.RIDGE,
        bd=2
    )
    response_area.place(x=370, y=305)

    frame = tk.Frame(
        root,
        relief=tk.RIDGE,
        borderwidth = 4
    )

    entry = tk.Entry(
        frame,
        width=70,
        font= font
    )
    entry.pack(side=tk.LEFT)
    entry.focus_set()

    button = tk.Button(
        frame,
        width=15,
        text="話す",
        command=talk
    )
    button.pack(side=tk.LEFT)
    frame.place(x=30, y=520)
    
    lb = tk.Listbox(
        root,
        width=42,
        height=30,
        font= font_log
    )

    sb1 = tk.Scrollbar(
        root,
        orient=tk.VERTICAL,
        command = lb.yview
    )

    sb2 = tk.Scrollbar(
        root,
        orient=tk.HORIZONTAL,
        command = lb.xview
    )

    lb.configure(yscrollcommand=sb1.set)
    lb.configure(yscrollcommand=sb2.set)

    lb.grid(row=0, column=0)
    
    sb1.grid(row=0, column=1, sticky=tk.NS)
    sb2.grid(row=1, column=2, sticky=tk.EW)

    root.mainloop()

if __name__ == "__main__":
    run()
    