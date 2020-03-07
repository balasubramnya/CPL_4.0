from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from functools import partial
import argparse
import os
import platform
import shlex
import subprocess
import ntpath

srcvideo = os.path.join('C:/','Users','Admin','Desktop','nj','CPL4.0','test_content','Video','Benaam','Benaam.mov')
destfile = os.path.join('C:/','Users','Admin','Desktop','nj','CPL4.0','test_content','Video','Benaam','Benaam_output.mxf')
clpath = os.path.join('C:/','Users','Admin','Desktop','nj','CPL4.0','tools','CatalystCL.exe')
transcoder = 'Catalyst.transcoder.kXAVCLong'

def OpenFile(textField,flag=0):
    if flag == 1 :
        name=askdirectory() 
    else:
        name = askopenfilename(initialdir="C:/Users/Documents/",
                           filetypes =(("mxf file", "*.mxf"),("mp4 file", "*.mp4"),("mov file", "*.mov")),
                           title = "Choose a file."
                           )
    textField.delete(0,END)
    textField.insert(0,name)
    textField.icursor(END)
    textField.xview_moveto(1)
    print(name)

def createArgs(script, args):
        s = clpath
        s += ' --script'
        s += ' "' + script + '"'
        s += ' --args "{'
        index = 0
        for (key, value) in args.items():
            if index > 0:
                s += ','
            s += '\\"' + key + '\\"' + ':' + '\\"' + value + '\\"'
            index += 1
        s += '}"'
        return s

def renderMedia( clpath, srcvideo, destfile, format):
        jscript = os.path.join('C:/','Users','Admin','Desktop','nj','CPL4.0','sample_scripts','rtf_scripts','MediaRenderer.js')
        if platform.system() == 'Windows':
            tempfile = destfile.replace("\\", "\\\\")
            srcvideo = srcvideo.replace("\\", "\\\\")
            clpath = clpath.replace("\\", "\\\\")
        else:
            tempfile = destfile

        args = { 'transcoder': transcoder, 'srcvideo': srcvideo,
                'dest': tempfile}
        arg_string = createArgs(jscript, args)
        if not args:
            return False
        # to do refactor
        if platform.system() != 'Windows':
            arg_string = shlex.split(arg_string)
        #print arg_string 
        process = subprocess.Popen(arg_string, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   shell=False)
        out, err = process.communicate()
        if err:
            print err;

        return not process.returncode

def ConvertFile(in_text_field,out_text_field):
    print('Convert')
    input_file_path = in_text_field.get()
    output_directory = out_text_field.get()
    if not len(input_file_path) == 0:
        head,tail=ntpath.split(input_file_path)
        in_file_name=tail.split('.')
        output_directory_with_filename=output_directory+'/'+in_file_name[0]+'_to_xavc'
        #print('hello output  '+output_directory_with_filename)

    renderMedia(clpath,input_file_path,output_directory_with_filename,transcoder)
    print('\n input file name '+input_file_path)
    print('\n outdirectory'+output_directory_with_filename)
 
window = Tk(useTk=1)
#window.resizable(width=FALSE, height=FALSE)


Title = window.title( "XDCAM to XAVC Converter")


input_label=Label(window, text="Input File", fg='black', font=("Helvetica", 10))
input_text_field=Entry(window, text="This is Input Text Widget",width=50)
input_file_btn=Button(window, text="...", fg='blue',command=partial(OpenFile,input_text_field))

output_label=Label(window, text="Output Folder", fg='black', font=("Helvetica", 10))
output_text_field=Entry(window, text="This is Output Text Widget",width=50)
output_file_btn=Button(window, text="...", fg='blue',command=partial(OpenFile,output_text_field,1))

Convert_btn=Button(window, text="Convert", fg='blue',command=partial(ConvertFile,input_text_field,output_text_field))

input_label.place(x=60, y=50)
input_text_field.place(x=160, y=50)
input_file_btn.place(x=480, y=50,width=30)

output_label.place(x=60, y=150)
output_text_field.place(x=160, y=150)
output_file_btn.place(x=480, y=150,width=30)

Convert_btn.place(x=250,y=200,width=60)

window.geometry("600x300+10+10")
window.mainloop()

 
