def convert():
    rates = CurrencyRates()
    OutputVar.set(round((rates.get_rate(InputCurrencyChoice.get(),OutputCurrencyChoice.get()))*int(TextVar.get()),2))

def main():
    
    #Setting up the screen
    Screen = Tk()
    Screen.title("Currency Converter")

    currency_opts = ["USD","EUR","GBP","JPY","CHF","TRY"]

    global InputCurrencyChoice
    global OutputCurrencyChoice

    InputCurrencyChoice = StringVar()
    OutputCurrencyChoice = StringVar()
    InputCurrencyChoice.set("USD")
    OutputCurrencyChoice.set("TRY")
    
    #Choice for input currency
    InputCurrencyChoiceMenu = OptionMenu(Screen,InputCurrencyChoice,*currency_opts)
    Label(Screen,text="Convert FROM").grid(row=0,column=2)
    InputCurrencyChoiceMenu.grid(row=1,column=2)
 
    #Choice for output currency
    OutputCurrencyChoiceMenu = OptionMenu(Screen,OutputCurrencyChoice,*currency_opts)
    Label(Screen,text="Convert TO").grid(row=0,column=4)
    OutputCurrencyChoiceMenu.grid(row=1,column=4)

    #Setting up labels
    Label(Screen,text="Enter Amount").grid(row=2,column =0)
    global TextVar 
    TextVar = StringVar()
    TextBox = Entry(Screen,textvariable=TextVar).grid(row=2,column = 2)
    
    Label(Screen,text="Converted Amount").grid(row=2,column =4)
    global OutputVar
    OutputVar = StringVar()
    TextBox = Entry(Screen,textvariable=OutputVar).grid(row=2,column = 6)

    #Button for calling function
    B = Button(Screen,text="CONVERT",command=convert) #The reason global vars was needed
    B.grid(row=3,column=2,columnspan = 3)

    Screen.mainloop()

if __name__ == "__main__":
    from forex_python.converter import CurrencyRates
    from tkinter import *
    main()
