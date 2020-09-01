#Grant Slattery
#9/1/20
#Using Python to display the current price of BTC in USD, GBP and EUR
#Project inspired by https://realpython.com/python-bitcoin-ifttt/ 
#API & data Powered by CoinDesk: https://www.coindesk.com/price/bitcoin
#The result is displayed in a GUI for future data testing.

import tkinter
import requests

bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(bitcoin_api_url)
response_json = response.json()


#First round of raw data cleaning
timeStamp = response_json.get("time")
coindeskDisclaimer = response_json.get("disclaimer")
priceData = response_json.get("bpi")


#Final price related data cleaning
usdData = priceData.get("USD")
gbpData = priceData.get("GBP")
eurData = priceData.get("EUR")

usdBtcPrice = usdData.get("rate")
gbpBtcPrice = gbpData.get("rate")
eurBtcPrice = eurData.get("rate")


#Final time related data cleaning
time1 = timeStamp.get("updated")
time2 = timeStamp.get("updatedISO")
time3 = timeStamp.get("updateduk")


#Display clean data
print(coindeskDisclaimer)
print("Updated: [" + time1 + "], [" + time2 + "], [" + time3 + "]")
print("1 BTC = $" + usdBtcPrice +" USD")
print("1 BTC = £" + gbpBtcPrice +" GBP")
print("1 BTC = €" + eurBtcPrice +" EUR")


class BitcoinPriceGUI:
    def __init__(self):


        # Create the main window.
        self.main_window = tkinter.Tk()
        # Create five frames to group widgets.
        self.top1_frame = tkinter.Frame()
        self.top2_frame = tkinter.Frame()
        self.mid1_frame = tkinter.Frame()
        self.mid2_frame = tkinter.Frame()
        self.mid3_frame = tkinter.Frame()

        
        self.disclaimer = tkinter.Label(self.top1_frame, \
                                          text=coindeskDisclaimer)
        self.time = tkinter.Label(self.top2_frame, \
                                          text="Updated: [" + time1 + "], [" + time2 + "], [" + time3 + "]")
        self.prompt_label = tkinter.Label(self.mid1_frame, \
                                          text="1 BTC = $" + usdBtcPrice + " USD")
        self.prompt_label2 = tkinter.Label(self.mid2_frame, \
                                          text="1 BTC = £" + gbpBtcPrice + " GBP")
        self.prompt_label3 = tkinter.Label(self.mid3_frame, \
                                          text="1 BTC = €" + eurBtcPrice + " EUR")


       # Pack the frame's widgets.
        self.disclaimer.pack(side='left')
        self.time.pack(side='left')
        self.prompt_label.pack(side='left')
        self.prompt_label2.pack(side='left')
        self.prompt_label3.pack(side='left')

     

        # Pack the frames.
        self.top1_frame.pack()
        self.top2_frame.pack()
        self.mid1_frame.pack()
        self.mid2_frame.pack()
        self.mid3_frame.pack()
        # Enter the tkinter main loop.
        tkinter.mainloop()


# Create an instance of the BitcoinPriceGUI class.
bitcoinPriceInstance = BitcoinPriceGUI()
