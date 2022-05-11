from forex_python.converter import CurrencyRates, RatesNotAvailableError
from tkinter import messagebox
from tkinter import *

def convert():
    rates = CurrencyRates()
    currentinp = ""
    currentout= ""

    if InputCurrencyChoice.get() == "Other (Type the ISO Code)":
        currentinp = Other1.get()
    else:
        currentinp = InputCurrencyChoice.get()
    
    if OutputCurrencyChoice.get() == "Other (Type the ISO Code)":
        currentout = Other2.get()
    else:
        currentout = OutputCurrencyChoice.get()

    try:
        OutputVar.set(round((rates.get_rate(currentinp,currentout))*int(TextVar.get()),2))
    except RatesNotAvailableError:
        messagebox.showinfo("Error", "Please provide a correct ISO code.")
    except ValueError:
        messagebox.showinfo("Error", "Please type in a number.")

def main():
    
    #Setting up the screen
    Screen = Tk()
    Screen.title("Currency Converter")
    Screen.geometry("550x100")

    currency_opts = ["USD","EUR","GBP","JPY","CHF","TRY","Other (Type the ISO Code)"]

    global InputCurrencyChoice
    global OutputCurrencyChoice

    InputCurrencyChoice = StringVar()
    OutputCurrencyChoice = StringVar()
    InputCurrencyChoice.set("USD")
    OutputCurrencyChoice.set("TRY")
    
    #Choice for input currency
    InputCurrencyChoiceMenu = OptionMenu(Screen,InputCurrencyChoice,*currency_opts)
    Label(Screen,text="Convert FROM").grid(row=0,column=1)
    InputCurrencyChoiceMenu.grid(row=1,column=0)

    global Other1 
    Other1 = StringVar()
    OtherBox1 = Entry(Screen,textvariable=Other1).grid(row=1,column=1)
 
    #Choice for output currency
    OutputCurrencyChoiceMenu = OptionMenu(Screen,OutputCurrencyChoice,*currency_opts)
    Label(Screen,text="Convert TO").grid(row=0,column=6)
    OutputCurrencyChoiceMenu.grid(row=1,column=5)

    global Other2 
    Other2 = StringVar()
    OtherBox2 = Entry(Screen,textvariable=Other2).grid(row=1,column=6)

    #Setting up labels
    Label(Screen,text="Enter Amount").grid(row=2,column =0)
    global TextVar 
    TextVar = StringVar()
    TextBox = Entry(Screen,textvariable=TextVar).grid(row=2,column = 1)
    
    Label(Screen,text="Converted Amount").grid(row=2,column =5)
    global OutputVar
    OutputVar = StringVar()
    TextBox = Entry(Screen,textvariable=OutputVar).grid(row=2,column = 6)

    #Button for calling function
    B = Button(Screen,text="CONVERT",command=convert) #The reason global vars was needed
    B.grid(row=3,column=2,columnspan = 3)

    Screen.mainloop()

if __name__ == "__main__":
    main()
