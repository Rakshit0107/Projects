import tkinter as tk
import webbrowser as web

def clicked():
	name = e.get()
	name.replace(" ","+")
	if var.get()==1:
		web.open_new_tab("https://www.google.com/search?q={}".format(name))
	elif var.get()==3:
		web.open_new_tab("https://www.amazon.com/s?k={}".format(name))
	else:
		web.open_new_tab("https://en.wikipedia.org/wiki/{}".format(name))

window = tk.Tk()
window.title("Unique Search")
window.geometry("500x200")

l = tk.Label(window,text="Enter to search   ", font = "arial 15")
l2 = tk.Label(window,text="Click on the website   ", font= "arial 15")

e = tk.Entry(window,width = 30)#height =10)
var = tk.IntVar()
rad1 = tk.Radiobutton(window,text="Google",variable=var,val=1)
rad2 = tk.Radiobutton(window,text="Wikipedia",variable=var,val=2)
rad3 = tk.Radiobutton(window,text="Amazon",variable=var,val=3)

btn = tk.Button(window, text="    Search   ", command = clicked)

l.grid(column = 1,row = 0)
e.grid(column =2, row =0)
btn.grid(column=3,row=0)
l2.grid(column=2,row=1)

rad1.grid(column=1,row=2)
rad2.grid(column=2,row=2)
rad3.grid(column=3,row=2)


window.mainloop()
