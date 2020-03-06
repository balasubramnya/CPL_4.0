from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from functools import partial

def OpenFile(textField,flag=0):
    if flag == 1 :
        name=askdirectory() 
    else:
        name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("mxf file", "*.mxf")),
                           title = "Choose a file."
                           )
    textField.delete(0,END)
    textField.insert(0,name)
    print(name)

def ConvertFile(in_text_field,out_text_field):
    print('Convert')
    input_file_name = in_text_field.get()
    output_directory=out_text_field.get()

    print('\ninput file name '+input_file_name)
    print('\noutdirectory'+output_directory)

window = Tk(useTk=1)
window.resizable(width=FALSE, height=FALSE)


Title = window.title( "XDCAM to XAVC Converter")


input_label=Label(window, text="Input", fg='black', font=("Helvetica", 16))
input_text_field=Entry(window, text="This is Input Text Widget")
input_file_btn=Button(window, text="...", fg='blue',command=partial(OpenFile,input_text_field))

output_label=Label(window, text="Output", fg='black', font=("Helvetica", 16))
output_text_field=Entry(window, text="This is Output Text Widget")
output_file_btn=Button(window, text="...", fg='blue',command=partial(OpenFile,output_text_field,1))

Convert_btn=Button(window, text="Convert", fg='blue',command=partial(ConvertFile,input_text_field,output_text_field))

input_label.place(x=60, y=50)
input_text_field.place(x=160, y=50)
input_file_btn.place(x=300, y=50,width=20)

output_label.place(x=60, y=150)
output_text_field.place(x=160, y=150)
output_file_btn.place(x=300, y=150,width=20)

Convert_btn.place(x=150,y=200,width=60)

window.geometry("400x300+10+10")
window.mainloop()

 
