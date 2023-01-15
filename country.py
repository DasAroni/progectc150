from tkinter import*
import random

root = Tk()
root.title("Lucky Friend Wheel")
root.geometry("500x500")
root.configure(background="Yellow")

entry_name = Entry(root)
entry_name.place(relx=0.5, rely=0.2, anchor=CENTER)

entry_name1 = Entry(root)
entry_name1.place(relx=0.5, rely=0.2, anchor=CENTER)

country_name_list = Label(root)
city_name_list = Label(root)


list1 = []


def addcountyr():
    country_name = entry_name.get()
    list1.append(country_name)
    country_name_list["text"] = "country:"+str(list1)

    city_name = entry_name.get()
    list1.append(city_name)
    city_name_list["text"] = "city:"+str(list1)




btn = Button(root, text="Add To The Friend List", command=addfriend)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

country_name_list.place(relx=0.5, rely=0.5, anchor=CENTER)

city_name_list.place(relx=0.5, rely=0.7, anchor=CENTER)


root.mainloop()
