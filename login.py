from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif usernameEntry.get() == 'Admin' and passwordEntry.get() == '1234':
        messagebox.showinfo('Success', 'Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error', 'Wrong credentials')


root = CTk()
root.geometry('930x478')
root.resizable(0, 0)
root.title('Login Page')


image_path = "/Users/akheruddinahmed/Desktop/1716735744618ems/ems/cover.jpg"
image = CTkImage(Image.open(image_path), size=(930, 478))
imageLabel = CTkLabel(root, image=image, text='')
imageLabel.place(x=0, y=0)


corner_image_path = "/Users/akheruddinahmed/Desktop/1716735744618ems/ems/Logo.jpg" 
corner_image = CTkImage(Image.open(corner_image_path), size=(300, 100))  
cornerImageLabel = CTkLabel(root, image=corner_image, text='')
cornerImageLabel.place(x=0, y=0)  


bottom_image_path = "/Users/akheruddinahmed/Desktop/1716735744618ems/ems/logo2.jpg" 
bottom_image = CTkImage(Image.open(bottom_image_path), size=(163, 200))  
bottomImageLabel = CTkLabel(root, image=bottom_image, text='')
bottomImageLabel.place(x=0, y=280)  


header_label = CTkLabel(root, text='IOCL Bongaigaon Refinery Admin Login', font=('Roboto', 30, 'bold', 'underline'), text_color='dark blue', bg_color='#FAFAFA')
header_label.place(relx=0.65, rely=0.05, anchor='center')  


usernameEntry = CTkEntry(root, placeholder_text='Enter Your Username', width=180)
usernameEntry.place(x=50, y=150)


passwordEntry = CTkEntry(root, placeholder_text='Enter Your Password', width=180, show='*')
passwordEntry.place(x=50, y=200)


loginButton = CTkButton(root, text='Login', cursor='hand2', command=login)
loginButton.place(x=70, y=250)

root.mainloop()
