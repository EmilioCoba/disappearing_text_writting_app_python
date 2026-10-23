from  customtkinter import *


app = CTk()
headline_frame=CTkFrame(app)
writing_frame=CTkFrame(app)

textbox = CTkTextbox(writing_frame,width=900,height=500,font=("Arial",20))


app.title("Disappearing Text Writing App")
app.geometry("900x900")


app.grid_columnconfigure(0, weight=1)

headline_frame.grid(row=0,column=0)

title_label=CTkLabel(headline_frame,text="Disappearing Text Writing App",font=('Arial',40))
title_label.grid(row=0,column=0,sticky="ew")

timer_label=CTkLabel(headline_frame,text="Timer: 5",font=('Arial',20))
timer_label.grid(row=1,column=0)

writing_frame.grid(row=1,column=0)

textbox.grid(row=1,column=0)
textbox.insert("0.0","Keep typing or else the text will disappear...")
textbox.bind("<FocusIn>",lambda args: textbox.delete("1.0","end"))

countdown = 5
typing_timer = None


def on_typing(event=None):
    global typing_timer

    if typing_timer is not None:
        app.after_cancel(typing_timer)

    update_timer(5)

def update_timer(seconds):
    global typing_timer

    timer_label.configure(text=f"Timer: {seconds}")

    if seconds > 0:
        typing_timer = app.after(
            1000, update_timer, seconds - 1
        )
    else:
        textbox.delete("1.0", "end")
        typing_timer = None
        
    if seconds>3:
        textbox.configure(text_color="white")
    elif seconds>1:
        textbox.configure(text_color="yellow")
    else:
        textbox.configure(text_color="red")

textbox.bind("<KeyPress>", on_typing)

app.mainloop()