#!/usr/bin/env python3

import socket
import  threading
import json
import os
import tkinter as tk
import sys
import time

a=[]

Unlock=threading.Event()
# Funzione che sblocca il thread che gestisce la connessione cosi da poter inviare le stringhe al server utilizzando  l'oggetto entry che genera la text area per l'input e quando viene cliccato il pulsante viene prelevato il testo presente nella text area
def hello () :
    #per notificare il thread che gestisce la connessione che il messaggio da inviare è pronto
     time.sleep(1)
     #questo per evitare che invii dati vuoti
     if entry.get()=="":
         return
     Unlock.set()
     
    
   


    
# Creazione della finestra
root = tk.Tk()
root.title("Avete capito!!!")

# Creazione della label e dell'entry per l'input
label = tk.Label(root, text="Inserisci domanda:")

label.pack()
entry = tk.Entry(root, width=100)
entry.pack()

# Creazione del pulsante
button = tk.Button(root, text="Invia", command=hello)
button.pack()


# Creazione della textarea per l'output
text = tk.Text(root,height=100, width=500)
text.pack()

#tutte questi metodi non serviranno a niente se non si avvia il metodo principale mainloop()

def Ui () :
   #qui parte il thread secondario per la connessione  con il protocollo tcp
   Main=threading.Thread(target=main,)
   Main.start()
   
   # avvia la finestra e crea un loop 
   root.mainloop()














def main():
    
     try:
        
        host = 'localhost'  # indirizzo IP del server
        port = 8081  # porta del server su cui ascolta
       
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port ))#richiesta di connesione al server 
        p=s.recv(1024).decode()
        text.delete("1.0", tk.END)
        text.insert(tk.END, p)
        
        while True:
         
        
         txt=""
         #mette in attesa il thread fin quando non verra notificato il thread principale
         Unlock.wait()
         
        
              
         #ottiene il valore della txtbar di input   
            
         txt=entry.get()
         
         entry.delete(0, tk.END)
         #la cancellazione inizia dalla riga 2, colonna 0 (il primo carattere), e finisce alla fine del widget (indirizzata dal "tk.END"). 
         text.delete("2.0", tk.END)
            
         i=0
              
         
         a=txt.split()
            
    
         c=int(len(a))
         i=0
         for i in range (c) :
          a[i]=a[i].lower()
         
         txt=txt.lower()
         #utilizzo dei file json
         json_data = json.dumps(a)
         json_data2 = json.dumps(txt)
   
         s.sendall(json_data.encode())
         s.sendall(json_data2.encode())
         
         data1=s.recv(1024).decode()
         
        # print(data1)
         a1=data1
         
         data2=s.recv(1024).decode()
         a2=data2
        
         print(str(a1))
         text.insert(tk.END, "\n")
         text.insert(tk.END, a1)
         text.insert(tk.END, a2)

         print(str(a2))
         txt=""
         
         Unlock.clear() # Resettiamo Unlock cosi che si possa bloccare di nuovo nel prossimo ciclo
     except:
        text.delete("1.0", tk.END)
        text.insert(tk.END, "Connessione Fallita Riconnessione tra ")
        time.sleep(1)
        text.insert(tk.END, "1..")
        time.sleep(2)
        text.insert(tk.END, "2...")
        time.sleep(2)
        text.insert(tk.END, "3")
        Unlock.clear()
        main()


         
         


        
   




    
   
    






    

if __name__ == "__main__":
    
    Ui()
    #main()