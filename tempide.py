
from tkinter import *
from tkinter.filedialog  import asksaveasfilename,askopenfilename
import subprocess
import requests




compiler=Tk()
compiler.title('IDE')
compiler.geometry('1200x800')
file_path=''

def set_file_path(path):
    global file_path
    file_path=path

def open_file():
    path=askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path,'r') as file:
        code=file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        set_file_path(path)


def save_as():
    if file_path=='':
        path=asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path=file_path
    with open(path,'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path=='':
        save_prompt=Toplevel()
        text=Label(save_prompt,text='Please save your code')
        text.pack()
        return
    command=f'python {file_path}'
    process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output,error=process.communicate()
    code_output.insert('1.0',output)
    code_output.insert('1.0',error)
    
    error_message=error.decode('utf-8')
    if error_message:
        rectify(error_message)
    

    # *****************************************


    
def rectify(E):
    print(E+"u0993909i090/n/n/n/n/n")

    url = "https://simple-chatgpt-api.p.rapidapi.com/ask"

    payload = { "question": "can you provide solution for this error :  "+E }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "2b23244403mshc63cf447f620304p190427jsnd07be47c9753",
        "X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    a= response.json()
    print(a['answer'])
    code_output.insert('1.0',"possible Solution : \n"+a['answer'])
    
    code_output.insert("1.0","done")


# *****************************************
menu_bar=Menu(compiler)

file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_as)
file_menu.add_command(label='Save as',command=save_as)
file_menu.add_command(label='Exit',command=exit)
menu_bar.add_cascade(label='File',menu=file_menu)

run_bar=Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run',command=run)
menu_bar.add_cascade(label='Run',menu=run_bar)

rectify_bar=Menu(menu_bar,tearoff=0)
rectify_bar.add_command(label='Rectify',command=rectify)
menu_bar.add_cascade(label='Rectify',menu=rectify_bar)

compiler.config(menu=menu_bar)

editor=Text()
editor.pack()


code_output=Text(height=10)
code_output.pack()
compiler.mainloop()
