from tkinter import *

import speedtest

root=Tk()
root.title("Internet Speed test")
root.geometry("360x600")
root.resizable(False,False)
root.configure(background="black")

def Check():
    test=speedtest.Speedtest()
    uploading =round(test.upload()//(1024*1024),2)
    upload.config(text=uploading)

    downloading=round(test.download()//(1024*1024),2)
    download.config(text=downloading)
    Download.config(text=downloading)

    servernames= []
    test.get_servers(servernames)
    ping.config(text=test.results.ping)

#icon
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

#image
Top=PhotoImage(file="top.png")
Label(root,image=Top,bg="black").pack()

Main=PhotoImage(file="main.png")
Label(root,image=Main,bg="black").pack(pady=(40,0))

button = PhotoImage(file="button.png")
Button=Button(root,image=button,bg="black",bd=0,activebackground="black",cursor="hand2",command=Check)
Button.pack(pady=10)

#label
Label(root,text="PING",font="TimesNewRoman 10 bold",bg="#384056").place(x=50,y=0)
Label(root,text="DOWMLOAD",font="TimesNewRoman 10 bold",bg="#384056").place(x=140,y=0)
Label(root,text="UPLOAD",font="TimesNewRoman 10 bold",bg="#384056").place(x=260,y=0)

Label(root,text="MS",font="TimesNewRoman 15 bold",bg="#384056",fg="white").place(x=60,y=80)
Label(root,text="MBPS",font="TimesNewRoman 15 bold",bg="#384056",fg="white").place(x=165,y=80)
Label(root,text="MBPS",font="TimesNewRoman 15 bold",bg="#384056",fg="white").place(x=275,y=80)

Label(root,text="Download",font="TimesNewRoman 13 bold",bg="#384056",fg="white").place(x=140,y=280)
Label(root,text="MBPS",font="TimeNewRoman 13 bold",bg="#384056",fg="white").place(x=155,y=380)

ping=Label(root,text="00",font="TimesNewRoman 13 bold",bg="#384056",fg="white")
ping.place(x=70,y=60,anchor="center")

download=Label(root,text="00",font="TimesNewRoman 13 bold",bg="#384056",fg="white")
download.place(x=180,y=60,anchor="center")

upload=Label(root,text="00",font="TimesNewRoman 13 bold",bg="#384056",fg="white")
upload.place(x=290,y=60,anchor="center")

Download=Label(root,text="00",font="TimesNewRoman 40 bold",bg="#384056")
Download.place(x=185,y=350,anchor="center")

root.mainloop()