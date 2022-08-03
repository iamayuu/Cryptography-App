from tkinter import *
from tkinter import messagebox
import pybase64
import os

def decrypt():
        password=code.get()
        
        if password=="1234":
                screen2=Toplevel(screen)
                screen2.title("encryption")
                screen2.geometry("400x200")
                screen2.configure(bg="green")
                
                message=text1.get(1.0,END)
                decode_message=message.encode("ascii")
                base64_bytes=pybase64.b64decode(decode_message)
                decrypt=base64_bytes.decode("ascii")
                print(decrypt)
                
                Label(screen2, text="ENCRYPTED TEXT", font="Arial",fg="white",bg="green").place(x=10,y=0)
                text3=Text(screen2,font="Arial 10",bg="white", relief=SUNKEN, warp=WORD,bd=2)
                text3.place(x=10,y=40,width=380, height=150)
                text3.insert(END,decrypt)
                
        elif password=="":
                messagebox.showerror("encryption","Input Password")
                
        elif password !="":
                messagebox.showerror("encryption","Invalid Password")
        
def encrypt():
        password=code.get()
        
        if password=="1234":
                screen1=Toplevel(screen)
                screen1.title("encryption")
                screen1.geometry("400x200")
                screen1.configure(bg="red")
                
                message=text1.get(1.0,END)
                encode_message=message.encode("ascii")
                base64_bytes=pybase64.b64encode(encode_message)
                encrypt=base64_bytes.decode("ascii")
                print(encrypt)
                
                Label(screen1, text="ENCRYPTED TEXT", font="Arial",fg="white",bg="red").place(x=10,y=0)
                text2=Text(screen1,font="Arial 10",bg="white",relief=SUNKEN,warp=WORD,bd=2)
                text2.place(x=10,y=40,width=380, height=150)
                
                text2.insert(END,encrypt)
                
        elif password=="":
                messagebox.showerror("encryption","Input Password")
                
        elif password !="":
                messagebox.showerror("encryption","Invalid Password")
                        
def main_screen():
        
        global screen
        global code
        global text1
        
        screen=Tk()
        #screen_size
        screen.geometry("500x550")
        #icons
        image_icons=PhotoImage(file="Project1\icon.png")
        screen.iconphoto(False,image_icons)
        screen.title("Encryp-Decryp APP")
        
        #reset_command
        def reset():
                code.set("")
                text1.delete(1.0,END)
        
        Label(text="Enter your message -",fg="black",bg="light gray",font=("calbri",25),).place(x=10,y=10)
        text1=Text(font="Robote 20", bg="white",relief=SUNKEN,wrap=WORD,bd=3)
        text1.place(x=10,y=65, width=480,height=200)
        
        Label(text="ENTER THE KEY-",bg="light gray",fg="black",font=("Ariel Black",25)).place(x=10,y=300)
        
        code=StringVar()
        Entry(textvariable=code,width=20,bd=3,font=("arial",25), show="*").place(x=10,y=350)
        
        Label(text="made by Ayuu",fg="black",font=("Aerial Black", 15, 'bold','underline')).place(x=330,y=500)
        
        Button(text="ENCRYPT", height="2", width=23, bg="red",fg="white",bd=2, command=encrypt).place(x=10,y=400)
        Button(text="DECRYPT", height="2", width=23, bg="green",fg="white",bd=2, command=decrypt).place(x=205,y=400)
        Button(text="RESET", height="2", width=51, bg="BLUE",fg="white",bd=2, command=reset).place(x=10,y=450)
        
        
        
        
        
        
        screen.mainloop()
        
main_screen()
