# -*- coding: utf-8 -*-

__author__ = 'RAVIV'
import wx
import wx.grid
import sys,time
import _socket
from threading import Thread

def OnCloseFrame(e):
    dialog = wx.MessageDialog(frame, message = "Are you sure you want to quit?", caption = "Caption", style = wx.YES_NO, pos = wx.DefaultPosition)
    response = dialog.ShowModal()

    if (response == wx.ID_YES):
        OnExitApp(e)



def OnExitApp(e):
    frame.Destroy()
    client_1.send("Exit")



def onMinimize(e):
        """
        When minimizing, hide the frame so it "minimizes to tray"
        """
        adminFrame.Hide()



def AmIadmin(e):
    name=" "
    client_1.send("R56LioSw2")
    textbox.Clear()



def GetUser(e):
    pass



def recvi():
      while True:
        data=client_1.recv(1024)
        done="True"
        if data=="Atadmin1829sksdw":
            adminbtn.Show()




        elif data=="Exit":
            pass

        elif data=="ROOM-Ok":
            textbox2.Clear()


        elif data=="Yt4712rrty":
            done = "False"
            print "ok"
            data=client_1.recv(1024)
            while data != "STOPSEND123":
             if data not in user_list:
              user_list.append(data)
             data=client_1.recv(1024)


            for i in range (len(user_list)):
                gs.SetCellValue(i,0,user_list[i])



            adminFrame.Show()
            done = "True"




        else:
         if done == "True":
           textbox2.AppendText(data+"\n")

def send(e):
    data=textbox.GetValue()
    data = data.encode('ascii', 'ignore').decode('ascii')

    client_1.send(data)
    textbox.Clear()

client_1=_socket.socket()
client_1.connect(('127.0.0.1',2222))

app = wx.App()
user_list=[]
done="True"
frame = wx.Frame(None, -1, 'simple.py')
adminFrame=wx.Frame(None, -1, 'admin.py')
adminpanel=wx.Panel(adminFrame,-1)
gs = wx.grid.Grid(adminFrame, -1)
vbox = wx.BoxSizer(wx.VERTICAL)
gs.CreateGrid(9, 2)
adminFrame.Bind(wx.EVT_CLOSE, onMinimize)
vbox.Add(gs, proportion=5, flag=wx.EXPAND)
adminFrame.SetSizer(vbox)
frame.SetSize((600,500))
frame.Move((300,200))
panel=wx.Panel(frame,-1)
panel.Move((300,200))
textbox=wx.TextCtrl(panel, pos=(3, 300), size=(200, 150),style=wx.TE_MULTILINE)
textbox2=wx.TextCtrl(panel, pos=(3, 3), size=(200, 150),style=wx.TE_READONLY|wx.TE_MULTILINE)
textbox.SetValue("Enter your name")

sbtn = wx.Button(panel, label='Send', pos=(300, 300))
sbtn.Bind(wx.EVT_BUTTON,send)
adminbtn = wx.Button(panel, label='admin', pos=(200, 150))
adminbtn.Bind(wx.EVT_BUTTON,AmIadmin)
adminbtn.Hide()
frame.Bind(wx.EVT_CLOSE,OnCloseFrame)


t=Thread(target=recvi,args=())
t.start()
frame.Show()


app.MainLoop()
