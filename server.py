# -*- coding: utf-8 -*-

import _socket
import re
import threading
from threading import  Thread
import time



def recivemsg (conn,):
     a=False
     name_bool=False

     while True:
         if a==False :
            conn.send("Create(1) or Join(2)?")
            room=conn.recv(1024)

            if room=="2":
              conn.send("Enter roon name to Join")
              room=conn.recv(1024)
              while room_list.has_key(room)==False:
                  conn.send("Room not found,enter again")
                  room=conn.recv(1024)

              if ban_list[room].has_key(conn):
                  conn.send("You ban from this room")


              conn.send("Enter Password")
              password=conn.recv(1024)
              x=room_list[room]
              while password!=x:
                  conn.send("Password incorrect")
                  password=conn.recv(1024)


              a=True


            elif room=="1":
              conn.send("Enter name room to create")
              room= conn.recv(1024)
              while room_list.has_key(room):
                  conn.send("Room already exists,choose another name")
                  room=conn.recv(1024)

              conn.send("ROOM-Ok")
              conn.send("Enter Password")
              password2=conn.recv(1024)
              conn.send("ROOM-Ok")
              if room not in room_list:
                 room_list[room]=password2
                 privete_list[room]= {}
                 name_list[room]={}
                 admin_list[room]={}
                 ban_list[room]={}


              a=True



         if name_bool==False:
              conn.send("Enter your name")
              name=conn.recv(1024)
              while privete_list[room].has_key(name):
                  conn.send("Name already exists,choose another name")
                  name=conn.recv(1024)
              if name=='Exit':
               conn.close()

              else:
                name_bool=True
                name_list[room][conn]=name
                privete_list[room][name]=conn
                conn.send("Hello "+name+" You conntecd to the server.")
                for client in name_list[room]:
                 if client is not conn:
                  client.send(name_list[room][conn]+" has connected")

                 if len(admin_list[room])==0:
                          conn.send(" You are admin now.")
                          admin_list[room][conn]="1"
                          time.sleep(1)
                          conn.send("Atadmin1829sksdw")



         data=conn.recv(1024)
         if(data=="Exit"):
             for client in name_list[room]:
                 if client is not conn:
                     client.send(name_list[room][conn]+" has disconnected ")

                 else:
                     client.send("You are disconnectd")

             del name_list[room][conn]
             del privete_list[room][name]

             if admin_list[room].has_key(conn):
                 del admin_list[room][conn]
                 if len(admin_list[room])==0:
                     for user in name_list[room]:
                         user.send("You are admin")
                         admin_list[room][user]="1"
                         time.sleep(1)
                         user.send("Atadmin1829sksdw")
                         print "hhfgh"
                         pass


             conn.send("Exit")
             conn.close()
             pass




         elif(data.startswith("/@")):

            data= re.split(r'[/@:]',data)
            print data
            if privete_list[room].has_key(data[2]):
             privete_list[room][data[2]].send("Private massage from "+name_list[room][conn]+" :"+data[3])

            else:
                conn.send("User not found")




         elif(data.startswith("kik")):
            if(conn in admin_list[room]):
              data=data.split(":")
              if privete_list[room].has_key(data[1]):
               privete_list[room][data[1]].send("You kicked out from the server ")
               privete_list[room][data[1]].close()
               connd=privete_list[room][data[1]]
               del name_list[room][connd]
               if admin_list[room].has_key(privete_list[room][data[1]]):
                   del admin_list[room][privete_list[room][data[1]]]

               del privete_list[room][data[1]]

               for client2 in name_list[room]:
                  client2.send(data[1]+" has kicked out from the server ")

              else:
                  conn.send("User not found")



            else:
                conn.send("You are not admin")



         elif(data.startswith("ban")):
            if(conn in admin_list[room]):
              data=data.split(":")
              if privete_list[room].has_key(data[1]):
                privete_list[room][data[1]].send("You ban from the server ")
                privete_list[room][data[1]].close()
                ban_list[room][privete_list[room][data[1]]]="1"

                del name_list[room][privete_list[room][data[1]]]
                if admin_list[room].has_key(privete_list[room][data[1]]):
                  del admin_list[room][privete_list[room][data[1]]]
                  del privete_list[room][data[1]]

                for client2 in name_list[room]:
                  client2.send(data[1]+" has kicked out from the server ")

              else:
                  conn.send("User not found")






            else:
                conn.send("You are not admin")




         elif(data=='R56LioSw2'):
              if conn in admin_list[room]:
                  conn.send("Yt4712rrty")
                  time.sleep(1)
                  for name in privete_list[room]:
                      conn.send(name)

                  conn.send("STOPSEND123")

              else:
                  conn.send("Server"+": "+"no")

         elif(data.startswith("!#")):

             if(admin_list[room].has_key(conn)):
                 data=data.split("!#")
                 print data
                 if privete_list[room].has_key(data[1]):
                     if admin_list[room].has_key(privete_list[room][data[1]])==False:
                       privete_list[room][data[1]].send("You are  admin now")
                       connd2=privete_list[room][data[1]]
                       admin_list[room][privete_list[room][data[1]]]="1"
                       for client3 in name_list[room]:
                        if client3 is not connd2:
                         client3.send(data[1]+" is admin now")
                         time.sleep(1)

                        else:
                         connd2.send("Atadmin1829sksdw")

                     else:
                         conn.send("The user has been Admin")

                 else:
                     conn.send("User not found")



         else:
            for client in name_list[room]:
              if client is not conn:
                   client.send(name_list[room][conn]+": "+ data)

              else:
                  client.send("Me"+": "+data)



def addnewclient():

         (conn,conn_adress)=server.accept()
         t5=Thread(target=recivemsg,args=(conn,))
         trede_list.append(t5)







server=_socket.socket()
server.bind(('127.0.0.1',2222))
server.listen(30)
a=False
name_list={}
privete_list={}
trede_list=[]
admin_list={}
room_list={}
ban_list={}
while True:
        t=Thread(target=addnewclient,args=())
        t.start()
        t.join()

        for tr in trede_list:

          if(tr.is_alive()==False):
               tr.start()

               trede_list.remove(tr)

















