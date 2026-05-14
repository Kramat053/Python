import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image

class NewsApp:
    def __init__(self):
        
      #fetch Data
      self.data = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=73392f241b4c48faaf14dec44d2f5827").json()
      #Initial GUI load
      self.load_gui()
      #Load the first News item
      self.load_news_item(0)
    def load_gui(self):
      self.root = Tk()
      self.root.geometry("360x600")
      self.root.resizeable(0,0)
      self.root.configure(background = "black")
    def clear(self):
      for i in self.root.pack_slaves():
        i.destroy()
    def load_news_item(self,index):
      self.clear()
      
      #image
      try:
         img_url = self.data["articles"][index]["urlToImage"]
         raw_data = urlopen(img_url).read()
         im = Image.open(io.BytesIO(raw_data).resize(350,250))
         photo = ImageTk.PhotoImage(im)
      except:
         img_url = "https://ih1.redbubble.net/image.4905811447.8675/flat,750x,075,f-pad,750x1000,f8f8f8.jpg"
         raw_data = urlopen(img_url).read()
         im = Image.open(io.BytesIO(raw_data).resize(350,250))
         photo = ImageTk.PhotoImage(im)
      label = Label(self.root,image = photo)
      label.pack()
      heading = Label(self.root,text = self.data["articles"][index]["title"],bd = "black",fg = "white",wraplength = 350, justify = "center")
      heading.pack(pady = (10,20))
      heading.config(font = ("verdana",15))
      
      details = Label(self.root,text = self.data["articles"][index]["description"],bd = "black",fg = "white",wraplength = 350, justify = "center")
      details.pack(pady = (2,20))
      details.config(font = ("verdana",12))
      
      frame = Frame(self.root,bg = "black")
      frame.pack(expand = True,fill = BOTH)
      
      if index != 0:
        prev = Button(frame,text = "Prev",width = 16,height = 3,command = lambda :self.load_news_item(index-1))
        prev.pack(side = LEFT)
      
      read = Button(frame,text = "Read More",width = 16,height = 3,command = lambda :self.open_link(self.data["articles"][index]["url"]))
      read.pack(side = LEFT)
      
      if index != len(self.data["articles"])-1:
        next = Button(frame,text = "Next",width = 16,height = 3,command = lambda :self.load_news_item(index+1))
        next.pack(side = LEFT)
      
      self.root.mainloop() 
      
    def open_link(self,url):
      webbrowser.open(url)   
obj = NewsApp()    
        