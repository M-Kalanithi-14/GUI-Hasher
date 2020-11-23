import tkinter as tk, hashlib as hl
from PIL import ImageTk, Image
from os import urandom
from tkinter import ttk
from tkinter import messagebox as mb

global result

root = tk.Tk()
root.title("Hasher")
root.resizable(False, False)

# =============================== Variables ======================
Input = tk.StringVar(root)
Algorithm = tk.StringVar(root)
AlgorithmList = ['blake2b', 'blake2s', 'md4', 'md5',
                'mdc2', 'ripemd160', 'sha1', 'sha224', 'sha256',
                'sha384', 'sha3_224', 'sha3_256', 'sha3_384',
                'sha3_512', 'sha512', 'shake_128', 'shake_256', 'sm3', 'whirlpool']
salt = urandom(512)
img = Image.open("Down Arrow.gif")
img = img.resize((150, 150), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

# ================================== Widgets ======================
lblInput = tk.Label(root , font = ('arial' , 16 , 'bold') , \
                                text = 'Enter the String you want to hash : ' , bd = 7)
lblInput.grid(row = 1 , column = 0 , sticky = 'n')
txtInput = tk.Entry(root , font = ('arial' , 16 , 'bold') , \
                            textvariable = Input , bd = 7 , insertwidth = 2)
txtInput.grid(row = 1 , column = 1)

lblArrow = tk.Label(root, image=img)
lblArrow.grid(row = 2 , column = 1 , sticky = 'n')

lblAlgorithm = tk.Label(root , font = ('arial' , 16 , 'bold') , \
                                text = 'Choose an Algorithm : ' , bd = 7)
lblAlgorithm.grid(row = 3 , column = 0 , sticky = 'n')
txtAlgorithm = ttk.Combobox(root , font = ('arial' , 16 , 'bold') , \
                                textvariable = Algorithm)
txtAlgorithm['values'] = AlgorithmList
txtAlgorithm.grid(row = 3 , column = 1)

lblArrow = tk.Label(root, image = img)
lblArrow.grid(row = 4 , column = 1 , sticky = 'n')

lblResult = tk.Label(root , font = ('arial' , 16 , 'bold') , \
                                text = 'Result' , bd = 7)
lblResult.grid(row = 5 , column = 0 , sticky = 'n')
txtResult = tk.Text(root , width = 70 , height = 10 , font = ('arial' , 16 , 'bold'),
                    foreground='black', background='white', state='disabled')
txtResult.grid(row = 5 , column = 1)

#================================= Function =============================
def Hash(event):
    if Algorithm.get() == '': mb.showerror("Hasher", "You Haven't selected any Hashing Algorithm")
    elif Algorithm.get() in AlgorithmList:
        if Algorithm.get() == 'blake2b' :
            result = hl.blake2b(Input.get().encode('utf-32')).hexdigest()

        elif Algorithm.get() == 'blake2s' :
            result = hl.blake2s(Input.get().encode('utf-32')).hexdigest()

        elif Algorithm.get() == 'md5' :
            result = hl.md5(Input.get().encode('utf-32')).hexdigest()

        elif Algorithm.get() == 'sha1' :
            result = hl.sha1(Input.get().encode('utf-32')).hexdigest()

        elif Algorithm.get() == 'sha224' :
            result = hl.sha224(Input.get().encode('utf-32')).hexdigest()

        elif Algorithm.get() == 'sha256' :
            result = hl.sha256(Input.get().encode('utf-32')).hexdigest()

        elif Algorithm.get() == 'sha384' :
            result = hl.sha384(Input.get().encode('utf-32')).hexdigest()

        elif Algorithm.get() == 'sha3_224' :
            result = hl.sha3_224(Input.get().encode('utf-32')).hexdigest()

        elif Algorithm.get() == 'sha3_256' :
            result = hl.sha3_256(Input.get().encode('utf-32')).hexdigest()

        elif Algorithm.get() == 'sha3_384' :
            result = hl.sha3_384(Input.get().encode('utf-32')).hexdigest()

        elif Algorithm.get() == 'sha3_512' :
            result = hl.sha3_512(Input.get().encode('utf-32')).hexdigest()

        elif Algorithm.get() == 'sha512' :
            result = hl.sha512(Input.get().encode('utf-32')).hexdigest()

        elif Algorithm.get() == 'shake_128' :
            result = hl.shake_128(Input.get().encode('utf-32')).hexdigest(128)

        elif Algorithm.get() == 'shake_256' :
            result = hl.shake_256(Input.get().encode('utf-32')).hexdigest(128)

        else:
            mod_input = Input.get().encode('utf-32')
            result = hl.pbkdf2_hmac(Algorithm.get(), mod_input, salt, 10000).hex()

        txtResult.configure(state='normal')
        txtResult.insert('1.0', result)
    else: mb.showerror("Hasher", "Oops Sorry!!!\nThe Selected Algorithm is not there in my List...\nPlease Click the Drop-Down Box to see the list of Algorithms")

def Reset():
    Input.set('')
    Algorithm.set('')
    txtResult.delete('1.0', 'end')
    txtResult.configure(state='disabled')

# ============================== Buttons =================================
btnReset = tk.Button(root, bd = 5, #bg='#ff0000',
                    font = ('arial' , 16 , 'bold') , text = 'Reset' , command = Reset)
btnReset.grid(row=7, column=0)

btnHash = tk.Button(root, bd = 5, #bg='#ff0000',
                    font = ('arial' , 16 , 'bold') , text = 'Hash' , command = lambda : Hash("event"))
btnHash.bind("<Return>", Hash)
btnHash.grid(row = 7 , column = 1)

root.bind("<Return>", Hash)
root.mainloop()