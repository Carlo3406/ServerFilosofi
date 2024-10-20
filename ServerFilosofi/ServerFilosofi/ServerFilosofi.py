import socket
import json
import queue
import threading
import time
import random
import os
import multiprocessing



#dichiarazioni variabili globali
default=[]
A=True
lR=threading.Lock()



def init() :
 default.append('ciao')#0
 default.append('ciao!')#1
 default.append('ciao !')#2
 default.append('salve')#3
 default.append('salve!')#4
 default.append('salve !')#5
 default.append('hey')#6
 default.append('hey!')#7
 default.append('hey !')#8

 default.append('buon giorno')#9
 default.append('buon giorno!')#10
 default.append('buon giorno !')#11

 default.append('buon pomeriggio')#12
 default.append('buon pomeriggio!')#13
 default.append('buon pomeriggio !')#14

 default.append('buona sera')#15
 default.append('buona sera!')#16
 default.append('buona sera !')#17


 #Aristotele
 default.append('quando \u00E8 nato aristotele' )#18
 default.append('quando \u00E8 nato aristotele ?' )#19
 default.append('quando \u00E8 nato aristotele?' )#20

 default.append('quando \u00E8 morto aristotele' )#21
 default.append('quando \u00E8 morto aristotele ?' )#22
 default.append('quando \u00E8 morto aristotele?' )#23

 default.append('chi era aristotele' )#24
 default.append('chi era aristotele ?' )#25
 default.append('chi era aristotele?' )#26

 default.append('a che corrente filosofica apparteneva  aristotele' )#27
 default.append('a che corrente filosofica apparteneva  aristotele ?' )#28
 default.append('a che corrente filosofica apparteneva  aristotele?' )#29
 #Socrate
 default.append('quando \u00E8 nato socrate' )#30
 default.append('quando \u00E8 nato socrate ?' )#31
 default.append('quando \u00E8 nato socrate?' )#32

 default.append('quando \u00E8 morto socrate' )#33
 default.append('quando \u00E8 morto socrate ?' )#34
 default.append('quando \u00E8 morto socrate?' )#35

 default.append('chi era socrate' )#36
 default.append('chi era socrate ?' )#37
 default.append('chi era socrate?' )#38

 default.append('a che corrente filosofica apparteneva  socrate' )#39
 default.append('a che corrente filosofica apparteneva  socrate ?' )#40
 default.append('a che corrente filosofica apparteneva  socrate?' )#41
 #Platone
 default.append('quando \u00E8 nato platone' )#42
 default.append('quando \u00E8 nato platone ?' )#43
 default.append('quando \u00E8 nato platone?' )#44

 default.append('quando \u00E8 morto platone' )#45
 default.append('quando \u00E8 morto platone ?' )#46
 default.append('quando \u00E8 morto platone?' )#47

 default.append('chi era platone' )#48
 default.append('chi era platone ?' )#49
 default.append('chi era platone?' )#50

 default.append('a che corrente filosofica apparteneva  platone' )#51
 default.append('a che corrente filosofica apparteneva  platone ?' )#52
 default.append('a che corrente filosofica apparteneva  platone?' )#53



 default.append('help' )#54


def init2(a,client_socket):
    listSaluti=("ciao","hey","hola","aloha","salve")
    listN=("nato","nascita","nacque","nascera","nasceva","nascer\u00E0","nasce")
    listM=("morto","defunto","deceduto","muore")
    listD=("quando","dove",)
    listF=("aristotele","socrate","platone")
   
    listsp=("vissuto","frase")

    Ndefault(a,client_socket,listN,listM,listD,listF,listsp,listSaluti)







def main ():
    host = '0.0.0.0'  # indirizzo IP 0.0.0.0 vuol dire che il server accettera la connesione di tutti i client della rete
    
    port = 8081  # porta dove è istaurata la connessione
    init()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creazione del socket TCP
    server_socket.bind((host, port))  # assegnazione al socket dell'indirizzo  di host e porta
    
    server_socket.listen(1)  # massimo numero di connessioni in attesa

    print("Waiting for connection...")





    
    conn, address = server_socket.accept()  # accettazione della  connessione, il metodo server_socket.accept() restituisce una tupla di due valori che verranno asseganti a conn,addr conn rappresenta la connesione con il client, address l'indirizzo del client

    
    
    # Accetta la connessione del client
    
    
    ready="Digita help per conoscere i comandi"
    conn.sendall(ready.encode())
    while True:
     print("Inizio while")

        

        
     time.sleep(1)
     #questo costrutto serve per poter oltreppasare un errore: Verra eseguito il codice dentro il try, se verra generata un eccezione(Errore) tutte le variabili verranno deallocate dalla memoria e si interompera il codice ed eseguira la parte di codice nell'except 
     try:
         print("ue")
         # Riceve i dati dal client 1024 è la dimensione dei buffer di ricezione 1024 byte
         json_data = conn.recv(1024).decode()
         data1=json.loads(json_data)
         json_data2 = conn.recv(1024).decode()
         data2=json.loads(json_data2)
         print ("data1= "+str(data1))
         print ("data2= "+str(data2))
         b=threading.Thread(target=AI,args=(data1,data2,conn))
         b.start()
     except:


         print("bella")
         conn.close()
         conn, addr = server_socket.accept()  # accettazione della connessione
         
         print("!1 fase")
         conn.sendall(ready.encode())
         
         print("fine exept")
         # Accetta la connessione del client

     
        
    

    conn.close()  # chiusura della connessione

def AI(a,txt,client_socket):
    
    an1=threading.Thread(target=Default,args=(txt,a,client_socket,))
    an1.start()

    

   

    



    



def Default(txt,a,client_socket):
    
    

    if (txt in default):
        print ("Domanda conosciuta")
        #viene assegnato a mum l'indice della lista dove si trova elemento uguale a txt
        num=default.index(txt)
       
        AnDefault(num,client_socket)
    else:
        print("Domanda non conosciuta")
        p1=multiprocessing.Process(target=init2,args=(a,client_socket,))
        p1.start()
    #else unlock





    

    


def AnDefault(i,client_socket):
    a=random.randint(0,2)
    diz={}
    risp="ERRORE!!! Ripeti la domanda "
    
    if a==0:

    #dizionario utilizzato per l'assegnamento condizionale
     diz={
        0:"Ciao a te utente",
        1: "Ciao a te utente",
        2:"Ciao a te utente",
        3:"Ciao a te utente",
        4:"Ciao a te utente",
        5:"Ciao a te utente",
        6:"Ciao a te utente",
        7:"Ciao a te utente",
        8:"Ciao a te utente",

        9:"Buon giorno a te utente",
        10:"Buon giorno a te utente",
        11:"Buon giorno a te utente",
        12:"Buon pomeriggio a te utente",
        13:"Buon pomeriggio a te utente",
        14:"Buon pomeriggio a te utente",
        15:"Buona sera a te utente",
        16:"Buona sera a te utente",
        17:"Buona sera a te utente",

        18:"Nel 384 A.C",
        19: "Nel 384 A.C",
        20:"Nel 384 A.C",

        21:"Nel 322 A.C",
        22:"Nel 322 A.C",
        23: "Nel 322 A.C",

        24:'Aristotele (in greco antico: Ἀριστοτέλης, Aristotélēs, pronuncia:  Stagira, 384 a.C. o 383 a.C. – Calcide, 322 a.C.)\n è stato un filosofo, scienziato e logico greco antico,\n ritenuto una delle menti più universali, innovative, prolifiche e influenti di tutti i tempi, sia per la vastità che per la profondità dei suoi campi di conoscenza.\n Insieme a Platone, suo maestro, e a Socrate è considerato uno dei padri del pensiero filosofico occidentale, che soprattutto da lui ha ereditato problemi, termini, concetti e metodi.',
        25:'Aristotele (in greco antico: Ἀριστοτέλης, Aristotélēs, pronuncia:  Stagira, 384 a.C. o 383 a.C. – Calcide, 322 a.C.)\n è stato un filosofo, scienziato e logico greco antico,\n ritenuto una delle menti più universali, innovative, prolifiche e influenti di tutti i tempi, sia per la vastità che per la profondità dei suoi campi di conoscenza.\n Insieme a Platone, suo maestro, e a Socrate è considerato uno dei padri del pensiero filosofico occidentale, che soprattutto da lui ha ereditato problemi, termini, concetti e metodi.',
        26:'Aristotele (in greco antico: Ἀριστοτέλης, Aristotélēs, pronuncia:  Stagira, 384 a.C. o 383 a.C. – Calcide, 322 a.C.)\n è stato un filosofo, scienziato e logico greco antico,\n ritenuto una delle menti più universali, innovative, prolifiche e influenti di tutti i tempi, sia per la vastità che per la profondità dei suoi campi di conoscenza.\nInsieme a Platone, suo maestro, e a Socrate è considerato uno dei padri del pensiero filosofico occidentale, che soprattutto da lui ha ereditato problemi, termini, concetti e metodi.',

        27:" Aristotele era un descrittivista, che evolve dalla filosofia platonica in direzione dell empirismo \n: interessato alla fisica, alla botanica e alla zoologia, egli apprezza le abilità retoriche e poetiche e l'azione al punto di criticare \n il cognitivismo socratico.",
        28:" Aristotele era un descrittivista, che evolve dalla filosofia platonica in direzione dell empirismo \n: interessato alla fisica, alla botanica e alla zoologia, egli apprezza le abilità retoriche e poetiche e l'azione al punto di criticare \n il cognitivismo socratico.",
        39:" Aristotele era un descrittivista, che evolve dalla filosofia platonica in direzione dell empirismo \n: interessato alla fisica, alla botanica e alla zoologia, egli apprezza le abilità retoriche e poetiche e l'azione al punto di criticare \n il cognitivismo socratico.",

        30:"Nel 470 o 469  A.C non si sa precisamente ",
        31:"Nel 470 o 469  A.C non si sa precisamente ",
        32:"Nel 470 o 469  A.C non si sa precisamente ",

        33:"Nel 399 A.C",
        34:"Nel 399 A.C",
        35:"Nel 399 A.C",

        36:"Socrate (in greco antico: Σωκράτης, Sōkrátēs, pronuncia: [sɔː'kratɛːs]; Atene, 470 a.C./469 a.C. – Atene, 399 a.C.) è stato un filosofo greco antico, uno dei più importanti esponenti della tradizione filosofica occidentale.\n Il contributo più importante che egli ha dato alla storia del pensiero filosofico consiste nel suo metodo d'indagine: il dialogo che utilizzava lo strumento critico dell'elenchos (ἔλεγχος, élenchos = confutazione) \n applicandolo prevalentemente all'esame in comune (ἐξετάζειν, exetàzein) di concetti morali fondamentali. Per questo Socrate è riconosciuto come padre fondatore dell'etica o filosofia morale.",
        37:"Socrate (in greco antico: Σωκράτης, Sōkrátēs, pronuncia: [sɔː'kratɛːs]; Atene, 470 a.C./469 a.C. – Atene, 399 a.C.) è stato un filosofo greco antico, uno dei più importanti esponenti della tradizione filosofica occidentale.\n Il contributo più importante che egli ha dato alla storia del pensiero filosofico consiste nel suo metodo d'indagine: il dialogo che utilizzava lo strumento critico dell'elenchos (ἔλεγχος, élenchos = confutazione) \n applicandolo prevalentemente all'esame in comune (ἐξετάζειν, exetàzein) di concetti morali fondamentali. Per questo Socrate è riconosciuto come padre fondatore dell'etica o filosofia morale.",
        38:"Socrate (in greco antico: Σωκράτης, Sōkrátēs, pronuncia: [sɔː'kratɛːs]; Atene, 470 a.C./469 a.C. – Atene, 399 a.C.) è stato un filosofo greco antico, uno dei più importanti esponenti della tradizione filosofica occidentale.\n Il contributo più importante che egli ha dato alla storia del pensiero filosofico consiste nel suo metodo d'indagine: il dialogo che utilizzava lo strumento critico dell'elenchos (ἔλεγχος, élenchos = confutazione) \n applicandolo prevalentemente all'esame in comune (ἐξετάζειν, exetàzein) di concetti morali fondamentali. Per questo Socrate è riconosciuto come padre fondatore dell'etica o filosofia morale.",

        39:"Secondo Socrate, si è uomini solo tra gli uomini, perché ciò che fa divenire tali è il rapporto con gli altri. In questo senso, occuparsi di filosofia significa un esame incessante di se stesso e degli altri esseri umani:\n essere uomini ed essere filosofi sono la stessa cosa.",
        40:"Secondo Socrate, si è uomini solo tra gli uomini, perché ciò che fa divenire tali è il rapporto con gli altri. In questo senso, occuparsi di filosofia significa un esame incessante di se stesso e degli altri esseri umani:\n essere uomini ed essere filosofi sono la stessa cosa.",
        41:"Secondo Socrate, si è uomini solo tra gli uomini, perché ciò che fa divenire tali è il rapporto con gli altri. In questo senso, occuparsi di filosofia significa un esame incessante di se stesso e degli altri esseri umani:\n essere uomini ed essere filosofi sono la stessa cosa.",


        42:"Platone nacque nel 428 A.C",
        43:"Platone nacque nel 428 A.C",
        44:"Platone nacque nel 428 A.C",

        45:"Nel 347 A.C",
        46:"Nel 347 A.C",
        47:"Nel 347 A.C",

        48:"Platone, figlio di Aristone del demo di Collito e di Perictione (in greco antico: Πλάτων, Plátōn, pronuncia: [ˈpla.tɔːn]; Atene, 428/427 a.C. – Atene, 348/347 a.C.)\n, è stato un filosofo e scrittore greco antico. Insieme al suo maestro Socrate e al suo allievo Aristotele, ha posto le basi del pensiero filosofico occidentale",
        49:"Platone, figlio di Aristone del demo di Collito e di Perictione (in greco antico: Πλάτων, Plátōn, pronuncia: [ˈpla.tɔːn]; Atene, 428/427 a.C. – Atene, 348/347 a.C.)\n, è stato un filosofo e scrittore greco antico. Insieme al suo maestro Socrate e al suo allievo Aristotele, ha posto le basi del pensiero filosofico occidentale",
        50:"Platone, figlio di Aristone del demo di Collito e di Perictione (in greco antico: Πλάτων, Plátōn, pronuncia: [ˈpla.tɔːn]; Atene, 428/427 a.C. – Atene, 348/347 a.C.)\n, è stato un filosofo e scrittore greco antico. Insieme al suo maestro Socrate e al suo allievo Aristotele, ha posto le basi del pensiero filosofico occidentale",

        51:"Il filosofo greco affermava l'esistenza di una più alta verità: le Idee, delle forme ideali eterne, immutabili, e incorruttibili, da cui ha origine il mondo sensibile, quale noi lo percepiamo, soggetto al divenire, alla corruzione, e alla morte.",
        52:"Il filosofo greco affermava l'esistenza di una più alta verità: le Idee, delle forme ideali eterne, immutabili, e incorruttibili, da cui ha origine il mondo sensibile, quale noi lo percepiamo, soggetto al divenire, alla corruzione, e alla morte.",
        53:"Il filosofo greco affermava l'esistenza di una più alta verità: le Idee, delle forme ideali eterne, immutabili, e incorruttibili, da cui ha origine il mondo sensibile, quale noi lo percepiamo, soggetto al divenire, alla corruzione, e alla morte.",
 
        54: "Salve scrivimi domande su questi filosofi ed io ti rispondero:Aristotele,Platone,Socrate",

        }
     risp= diz.get(i)
     
    elif a==1:
        diz2={
         0:"Salve utente",
        1: "Salve utente",
        2:"Salve utente",
        3:"Salve utente",
        4:"Salve utente",
        5:"Salve utente",
        6:"Salve utente",
        7:"Salve utente",
        8:"Salve utente",

        9:"Buon giorno",
        10:"Buon giorno",
        11:"Buon giorno",
        12:"Buon pomeriggio",
        13:"Buon pomeriggio",
        14:"Buon pomeriggio",
        15:"Buona sera",
        16:"Buona sera",
        17:"Buona sera",

        18:"Nasce nel 384 A.C",
        19: "Nasce nel 384 A.C",
        20:"Nasce nel 384 A.C",

        21:"Muore nel 322 A.C",
        22:"Muore nel 322 A.C",
        23: "Muore nel 322 A.C",

        24:'Aristotele (in greco antico: Ἀριστοτέλης, Aristotélēs, pronuncia:  Stagira, 384 a.C. o 383 a.C. – Calcide, 322 a.C.)\n è stato un filosofo, scienziato e logico greco antico,\n ritenuto una delle menti più universali, innovative, prolifiche e influenti di tutti i tempi, sia per la vastità che per la profondità dei suoi campi di conoscenza.\n Insieme a Platone, suo maestro, e a Socrate è considerato uno dei padri del pensiero filosofico occidentale, che soprattutto da lui ha ereditato problemi, termini, concetti e metodi.',
        25:'Aristotele (in greco antico: Ἀριστοτέλης, Aristotélēs, pronuncia:  Stagira, 384 a.C. o 383 a.C. – Calcide, 322 a.C.)\n è stato un filosofo, scienziato e logico greco antico,\n ritenuto una delle menti più universali, innovative, prolifiche e influenti di tutti i tempi, sia per la vastità che per la profondità dei suoi campi di conoscenza.\n Insieme a Platone, suo maestro, e a Socrate è considerato uno dei padri del pensiero filosofico occidentale, che soprattutto da lui ha ereditato problemi, termini, concetti e metodi.',
        26:'Aristotele (in greco antico: Ἀριστοτέλης, Aristotélēs, pronuncia:  Stagira, 384 a.C. o 383 a.C. – Calcide, 322 a.C.)\n è stato un filosofo, scienziato e logico greco antico,\n ritenuto una delle menti più universali, innovative, prolifiche e influenti di tutti i tempi, sia per la vastità che per la profondità dei suoi campi di conoscenza.\nInsieme a Platone, suo maestro, e a Socrate è considerato uno dei padri del pensiero filosofico occidentale, che soprattutto da lui ha ereditato problemi, termini, concetti e metodi.',

        27:" Aristotele era un descrittivista, che evolve dalla filosofia platonica in direzione dell empirismo \n: interessato alla fisica, alla botanica e alla zoologia, egli apprezza le abilità retoriche e poetiche e l'azione al punto di criticare \n il cognitivismo socratico.",
        28:" Aristotele era un descrittivista, che evolve dalla filosofia platonica in direzione dell empirismo \n: interessato alla fisica, alla botanica e alla zoologia, egli apprezza le abilità retoriche e poetiche e l'azione al punto di criticare \n il cognitivismo socratico.",
        39:" Aristotele era un descrittivista, che evolve dalla filosofia platonica in direzione dell empirismo \n: interessato alla fisica, alla botanica e alla zoologia, egli apprezza le abilità retoriche e poetiche e l'azione al punto di criticare \n il cognitivismo socratico.",

        30:"Nel 470 o 469  A.C non si sa precisamente ",
        31:"Nel 470 o 469  A.C non si sa precisamente ",
        32:"Nel 470 o 469  A.C non si sa precisamente ",

        33:"Nel 399 A.C",
        34:"Nel 399 A.C",
        35:"Nel 399 A.C",

        36:"Socrate (in greco antico: Σωκράτης, Sōkrátēs, pronuncia: [sɔː'kratɛːs]; Atene, 470 a.C./469 a.C. – Atene, 399 a.C.) è stato un filosofo greco antico, uno dei più importanti esponenti della tradizione filosofica occidentale.\n Il contributo più importante che egli ha dato alla storia del pensiero filosofico consiste nel suo metodo d'indagine: il dialogo che utilizzava lo strumento critico dell'elenchos (ἔλεγχος, élenchos = confutazione) \n applicandolo prevalentemente all'esame in comune (ἐξετάζειν, exetàzein) di concetti morali fondamentali. Per questo Socrate è riconosciuto come padre fondatore dell'etica o filosofia morale.",
        37:"Socrate (in greco antico: Σωκράτης, Sōkrátēs, pronuncia: [sɔː'kratɛːs]; Atene, 470 a.C./469 a.C. – Atene, 399 a.C.) è stato un filosofo greco antico, uno dei più importanti esponenti della tradizione filosofica occidentale.\n Il contributo più importante che egli ha dato alla storia del pensiero filosofico consiste nel suo metodo d'indagine: il dialogo che utilizzava lo strumento critico dell'elenchos (ἔλεγχος, élenchos = confutazione) \n applicandolo prevalentemente all'esame in comune (ἐξετάζειν, exetàzein) di concetti morali fondamentali. Per questo Socrate è riconosciuto come padre fondatore dell'etica o filosofia morale.",
        38:"Socrate (in greco antico: Σωκράτης, Sōkrátēs, pronuncia: [sɔː'kratɛːs]; Atene, 470 a.C./469 a.C. – Atene, 399 a.C.) è stato un filosofo greco antico, uno dei più importanti esponenti della tradizione filosofica occidentale.\n Il contributo più importante che egli ha dato alla storia del pensiero filosofico consiste nel suo metodo d'indagine: il dialogo che utilizzava lo strumento critico dell'elenchos (ἔλεγχος, élenchos = confutazione) \n applicandolo prevalentemente all'esame in comune (ἐξετάζειν, exetàzein) di concetti morali fondamentali. Per questo Socrate è riconosciuto come padre fondatore dell'etica o filosofia morale.",

        39:"Secondo Socrate, si è uomini solo tra gli uomini, perché ciò che fa divenire tali è il rapporto con gli altri. In questo senso, occuparsi di filosofia significa un esame incessante di se stesso e degli altri esseri umani:\n essere uomini ed essere filosofi sono la stessa cosa.",
        40:"Secondo Socrate, si è uomini solo tra gli uomini, perché ciò che fa divenire tali è il rapporto con gli altri. In questo senso, occuparsi di filosofia significa un esame incessante di se stesso e degli altri esseri umani:\n essere uomini ed essere filosofi sono la stessa cosa.",
        41:"Secondo Socrate, si è uomini solo tra gli uomini, perché ciò che fa divenire tali è il rapporto con gli altri. In questo senso, occuparsi di filosofia significa un esame incessante di se stesso e degli altri esseri umani:\n essere uomini ed essere filosofi sono la stessa cosa.",


        42:"Nel 428 A.C",
        43:"Nel 428 A.C",
        44:"Nel 428 A.C",

        45:"Nel 347 A.C",
        46:"Nel 347 A.C",
        47:"Nel 347 A.C",

        48:"Platone, figlio di Aristone del demo di Collito e di Perictione (in greco antico: Πλάτων, Plátōn, pronuncia: [ˈpla.tɔːn]; Atene, 428/427 a.C. – Atene, 348/347 a.C.)\n, è stato un filosofo e scrittore greco antico. Insieme al suo maestro Socrate e al suo allievo Aristotele, ha posto le basi del pensiero filosofico occidentale",
        49:"Platone, figlio di Aristone del demo di Collito e di Perictione (in greco antico: Πλάτων, Plátōn, pronuncia: [ˈpla.tɔːn]; Atene, 428/427 a.C. – Atene, 348/347 a.C.)\n, è stato un filosofo e scrittore greco antico. Insieme al suo maestro Socrate e al suo allievo Aristotele, ha posto le basi del pensiero filosofico occidentale",
        50:"Platone, figlio di Aristone del demo di Collito e di Perictione (in greco antico: Πλάτων, Plátōn, pronuncia: [ˈpla.tɔːn]; Atene, 428/427 a.C. – Atene, 348/347 a.C.)\n, è stato un filosofo e scrittore greco antico. Insieme al suo maestro Socrate e al suo allievo Aristotele, ha posto le basi del pensiero filosofico occidentale",

        51:"Il filosofo greco affermava l'esistenza di una più alta verità: le Idee, delle forme ideali eterne, immutabili, e incorruttibili, da cui ha origine il mondo sensibile, quale noi lo percepiamo, soggetto al divenire, alla corruzione, e alla morte.",
        52:"Il filosofo greco affermava l'esistenza di una più alta verità: le Idee, delle forme ideali eterne, immutabili, e incorruttibili, da cui ha origine il mondo sensibile, quale noi lo percepiamo, soggetto al divenire, alla corruzione, e alla morte.",
        53:"Il filosofo greco affermava l'esistenza di una più alta verità: le Idee, delle forme ideali eterne, immutabili, e incorruttibili, da cui ha origine il mondo sensibile, quale noi lo percepiamo, soggetto al divenire, alla corruzione, e alla morte.",
        54: "Salve scrivimi domande su questi filosofi ed io ti rispondero:Aristotele,Platone,Socrate",

        }
        risp= diz2.get(i)
    elif a==2:
        diz3={
         0:"Hey utente!!!",
        1: "Hey utente!!!",
        2:"Hey utente!!!",
        3:"Hey utente!!!",
        4:"Hey utente!!!",
        5:"Hey utente!!!",
        6:"Hey utente!!!",
        7:"Hey utente!!!",
        8:"Hey utente!!!",

        9:"Grazie buon giorno anche a te",
        10:"Grazie buon giorno anche a te",
        11:"Grazie buon giorno anche a te",
        12:"Grazie buon pomeriggio anche a te",
        13:"Grazie buon pomeriggio anche a te",
        14:"Grazie buon pomeriggio anche a te",
        15:"Grazie buona sera anche a te",
        16:"Grazie buona sera anche a te",
        17:"Grazie buona sera anche a te",

        18:"Aristotale nacque nel 384 A.C",
        19: "Aristotale nacque nel 384 A.C",
        20:"Aristotale nacque nel 384 A.C",

        21:"Aristotale mori nel 322 A.C",
        22:"Aristotale mori nel 322 A.C",
        23: "Aristotale mori nel 322 A.C",

        24:'Aristotele (in greco antico: Ἀριστοτέλης, Aristotélēs, pronuncia:  Stagira, 384 a.C. o 383 a.C. – Calcide, 322 a.C.)\n è stato un filosofo, scienziato e logico greco antico,\n ritenuto una delle menti più universali, innovative, prolifiche e influenti di tutti i tempi, sia per la vastità che per la profondità dei suoi campi di conoscenza.\n Insieme a Platone, suo maestro, e a Socrate è considerato uno dei padri del pensiero filosofico occidentale, che soprattutto da lui ha ereditato problemi, termini, concetti e metodi.',
        25:'Aristotele (in greco antico: Ἀριστοτέλης, Aristotélēs, pronuncia:  Stagira, 384 a.C. o 383 a.C. – Calcide, 322 a.C.)\n è stato un filosofo, scienziato e logico greco antico,\n ritenuto una delle menti più universali, innovative, prolifiche e influenti di tutti i tempi, sia per la vastità che per la profondità dei suoi campi di conoscenza.\n Insieme a Platone, suo maestro, e a Socrate è considerato uno dei padri del pensiero filosofico occidentale, che soprattutto da lui ha ereditato problemi, termini, concetti e metodi.',
        26:'Aristotele (in greco antico: Ἀριστοτέλης, Aristotélēs, pronuncia:  Stagira, 384 a.C. o 383 a.C. – Calcide, 322 a.C.)\n è stato un filosofo, scienziato e logico greco antico,\n ritenuto una delle menti più universali, innovative, prolifiche e influenti di tutti i tempi, sia per la vastità che per la profondità dei suoi campi di conoscenza.\nInsieme a Platone, suo maestro, e a Socrate è considerato uno dei padri del pensiero filosofico occidentale, che soprattutto da lui ha ereditato problemi, termini, concetti e metodi.',

        27:" Aristotele era un descrittivista, che evolve dalla filosofia platonica in direzione dell empirismo \n: interessato alla fisica, alla botanica e alla zoologia, egli apprezza le abilità retoriche e poetiche e l'azione al punto di criticare \n il cognitivismo socratico.",
        28:" Aristotele era un descrittivista, che evolve dalla filosofia platonica in direzione dell empirismo \n: interessato alla fisica, alla botanica e alla zoologia, egli apprezza le abilità retoriche e poetiche e l'azione al punto di criticare \n il cognitivismo socratico.",
        39:" Aristotele era un descrittivista, che evolve dalla filosofia platonica in direzione dell empirismo \n: interessato alla fisica, alla botanica e alla zoologia, egli apprezza le abilità retoriche e poetiche e l'azione al punto di criticare \n il cognitivismo socratico.",

        30:"Nel 470 o 469  A.C non c'\u00E8 una data certa",
        31:"Nel 470 o 469  A.C non c'\u00E8 una data certa",
        32:"Nel 470 o 469  A.C non c'\u00E8 una data certa",

        33:"Socrate muore nel 399 A.C",
        34:"Socrate muore nel 399 A.C",
        35:"Socrate muore nel 399 A.C",

        36:"Socrate (in greco antico: Σωκράτης, Sōkrátēs, pronuncia: [sɔː'kratɛːs]; Atene, 470 a.C./469 a.C. – Atene, 399 a.C.) è stato un filosofo greco antico, uno dei più importanti esponenti della tradizione filosofica occidentale.\n Il contributo più importante che egli ha dato alla storia del pensiero filosofico consiste nel suo metodo d'indagine: il dialogo che utilizzava lo strumento critico dell'elenchos (ἔλεγχος, élenchos = confutazione) \n applicandolo prevalentemente all'esame in comune (ἐξετάζειν, exetàzein) di concetti morali fondamentali. Per questo Socrate è riconosciuto come padre fondatore dell'etica o filosofia morale.",
        37:"Socrate (in greco antico: Σωκράτης, Sōkrátēs, pronuncia: [sɔː'kratɛːs]; Atene, 470 a.C./469 a.C. – Atene, 399 a.C.) è stato un filosofo greco antico, uno dei più importanti esponenti della tradizione filosofica occidentale.\n Il contributo più importante che egli ha dato alla storia del pensiero filosofico consiste nel suo metodo d'indagine: il dialogo che utilizzava lo strumento critico dell'elenchos (ἔλεγχος, élenchos = confutazione) \n applicandolo prevalentemente all'esame in comune (ἐξετάζειν, exetàzein) di concetti morali fondamentali. Per questo Socrate è riconosciuto come padre fondatore dell'etica o filosofia morale.",
        38:"Socrate (in greco antico: Σωκράτης, Sōkrátēs, pronuncia: [sɔː'kratɛːs]; Atene, 470 a.C./469 a.C. – Atene, 399 a.C.) è stato un filosofo greco antico, uno dei più importanti esponenti della tradizione filosofica occidentale.\n Il contributo più importante che egli ha dato alla storia del pensiero filosofico consiste nel suo metodo d'indagine: il dialogo che utilizzava lo strumento critico dell'elenchos (ἔλεγχος, élenchos = confutazione) \n applicandolo prevalentemente all'esame in comune (ἐξετάζειν, exetàzein) di concetti morali fondamentali. Per questo Socrate è riconosciuto come padre fondatore dell'etica o filosofia morale.",

        39:"Secondo Socrate, si è uomini solo tra gli uomini, perché ciò che fa divenire tali è il rapporto con gli altri. In questo senso, occuparsi di filosofia significa un esame incessante di se stesso e degli altri esseri umani:\n essere uomini ed essere filosofi sono la stessa cosa.",
        40:"Secondo Socrate, si è uomini solo tra gli uomini, perché ciò che fa divenire tali è il rapporto con gli altri. In questo senso, occuparsi di filosofia significa un esame incessante di se stesso e degli altri esseri umani:\n essere uomini ed essere filosofi sono la stessa cosa.",
        41:"Secondo Socrate, si è uomini solo tra gli uomini, perché ciò che fa divenire tali è il rapporto con gli altri. In questo senso, occuparsi di filosofia significa un esame incessante di se stesso e degli altri esseri umani:\n essere uomini ed essere filosofi sono la stessa cosa.",


        42:"Nel 428 A.C",
        43:"Nel 428 A.C",
        44:"Nel 428 A.C",

        45:"Nel 347 A.C",
        46:"Nel 347 A.C",
        47:"Nel 347 A.C",

        48:"Platone, figlio di Aristone del demo di Collito e di Perictione (in greco antico: Πλάτων, Plátōn, pronuncia: [ˈpla.tɔːn]; Atene, 428/427 a.C. – Atene, 348/347 a.C.)\n, è stato un filosofo e scrittore greco antico. Insieme al suo maestro Socrate e al suo allievo Aristotele, ha posto le basi del pensiero filosofico occidentale",
        49:"Platone, figlio di Aristone del demo di Collito e di Perictione (in greco antico: Πλάτων, Plátōn, pronuncia: [ˈpla.tɔːn]; Atene, 428/427 a.C. – Atene, 348/347 a.C.)\n, è stato un filosofo e scrittore greco antico. Insieme al suo maestro Socrate e al suo allievo Aristotele, ha posto le basi del pensiero filosofico occidentale",
        50:"Platone, figlio di Aristone del demo di Collito e di Perictione (in greco antico: Πλάτων, Plátōn, pronuncia: [ˈpla.tɔːn]; Atene, 428/427 a.C. – Atene, 348/347 a.C.)\n, è stato un filosofo e scrittore greco antico. Insieme al suo maestro Socrate e al suo allievo Aristotele, ha posto le basi del pensiero filosofico occidentale",

        51:"Il filosofo greco affermava l'esistenza di una più alta verità: le Idee, delle forme ideali eterne, immutabili, e incorruttibili, da cui ha origine il mondo sensibile, quale noi lo percepiamo, soggetto al divenire, alla corruzione, e alla morte.",
        52:"Il filosofo greco affermava l'esistenza di una più alta verità: le Idee, delle forme ideali eterne, immutabili, e incorruttibili, da cui ha origine il mondo sensibile, quale noi lo percepiamo, soggetto al divenire, alla corruzione, e alla morte.",
        53:"Il filosofo greco affermava l'esistenza di una più alta verità: le Idee, delle forme ideali eterne, immutabili, e incorruttibili, da cui ha origine il mondo sensibile, quale noi lo percepiamo, soggetto al divenire, alla corruzione, e alla morte.",
        54: "Salve scrivimi domande su questi filosofi ed io ti rispondero:Aristotele,Platone,Socrate",

        }


        risp= diz3.get(i)
        

    

    
    risp2=" "
    print(risp)

    #json_data = json.dumps(risp)
    #json_data2 = json.dumps("\n")
    #client_socket.sendall(json_data.encode())
    #client_socket.sendall(json_data2.encode())
    
    client_socket.sendall(risp.encode())
    client_socket.sendall(risp2.encode())

    
    #unlock Ai






    



def Ndefault(a,client_socket,listN,listM,listD,listF,listsp,listSaluti):
   print("hi")
   risp=" "
   risp2=" "
   Ns=True
   NumeroD=int(Ver(a,listD))
   print(NumeroD)
   #if1 principale per vedere se ci sono le domande
   if NumeroD>=0:
    #if2 if per vedere quale domanda è presente
    if NumeroD==0:

       
       if Ver(a,listN)>=0 :
           print("Quando+Nascita")
           
           if (Ver(a,listF)==0):
               print("Aristotele")
               if risp==" ":
                   risp="Aristotale nacque nel 384 A.C\n"
                   Ns=False
               else:
                   risp2="Nasce nel 384 A.C"
                   Ns=False
                   

           elif (Ver(a,listF)==1):
               print("Socrate")
               if risp==" ":
                   risp="Nel 470 o 469  A.C non c'\u00E8 una data certa\n"
                   Ns=False
               else:
                   risp2="Nel 470 o 469  A.C non c'\u00E8 una data certa"
                   Ns=False
               
           elif (Ver(a,listF)==2):
               print("Platone")
               if risp==" ":
                   risp="Nel 428 A.C\n"
                   Ns=False
               else:
                   risp2="Platone nacque nel 428 A.C"
                   Ns=False
           else:

            print("Autore mancante")
            risp="Non \u00E8 stato specificato il filosofo o non lo conosco"
            risp2=" "
            Ns=False

            
            client_socket.sendall(risp.encode())
            time.sleep(0.1)
            client_socket.sendall(risp2.encode())
            return



       if Ver(a,listM)>=0:
           print("Quando +morte")
           if (Ver(a,listF)==0):
               print("Aristotele")
               if risp==" ":
                   risp="Aristotale mori nel 322 A.C\n"
                   Ns=False
               else:
                   risp2="Morira nel 322 A.C"
                   Ns=False
                   

           elif (Ver(a,listF)==1):
               print("Socrate")
               if risp==" ":
                   risp="Socrate muore nel 399 A.C\n"
                   Ns=False
               else:
                   risp2="Morira nel 399 A.C"
                   Ns=False
               
           elif (Ver(a,listF)==2):
               print("Platone")
               if risp==" ":
                   risp="Nel 347 A.C\n"
                   Ns=False
               else:
                   risp2="Morira nel 347 A.C"
                   Ns=False
           else:

            print("Autore mancante")
            risp="Non \u00E8 stato specificato il filosofo o non lo conosco"
            risp2=" "
            Ns=False

            
            client_socket.sendall(risp.encode())
            time.sleep(0.1)
            client_socket.sendall(risp2.encode())
            return
       if Ns:
           risp="Non ho capito\n"
           risp2="Controlla la domanda"

    





    #DOVE
    if NumeroD==1:
        print("Dove")
        A=True
        if Ver(a,listN)>=0 :
           print("Dove+Nascita")
           A=False
           if (Ver(a,listF)==0):
               print("Aristotele")
               if risp==" ":
                   risp="Aristotale nacque a Stagira in Grecia\n"
                   Ns=False
               else:
                   risp2="Nasce a Stagira in Grecia"
                   Ns=False
                   

           elif (Ver(a,listF)==1):
               print("Socrate")
               if risp==" ":
                   risp="Socrate è nato ad Alopece\n"
                   Ns=False
               else:
                   risp2="Socrate è nato ad Alopece"
                   Ns=False
               
           elif (Ver(a,listF)==2):
               print("Platone")
               if risp==" ":
                   risp="Nasce ad Atene Classica,Grecia\n"
                   Ns=False
               else:
                   risp2="Nasce ad Atene Classica,Grecia"
                   Ns=False
           else:

            print("Autore mancante")
            risp="Non \u00E8 stato specificato il filosofo o non lo conosco"
            risp2=" "
            Ns=False

            
            client_socket.sendall(risp.encode())
            time.sleep(0.1)
            client_socket.sendall(risp2.encode())
            return



        if Ver(a,listM)>=0:
           print("Dove +morte")
           A=False
           if (Ver(a,listF)==0):
               print("Aristotele")
               if risp==" ":
                   risp="Aristotale mori ad Euboea Island, Grecia\n"
                   Ns=False
               else:
                   risp2="Aristotale mori ad Euboea Island, Grecia"
                   Ns=False
                   

           elif (Ver(a,listF)==1):
               print("Socrate")
               if risp==" ":
                   risp="Socrate muore ad Atene Classica,Grecia\n"
                   Ns=False
               else:
                   risp2="Socrate muore ad Atene Classica,Grecia"
                   Ns=False
               
           elif (Ver(a,listF)==2):
               print("Platone")
               if risp==" ":
                   risp="Platone muore ad Atene,Grecia\n"
                   Ns=False
               else:
                   risp2="Platone muore ad Atene,Grecia"
                   Ns=False
           else:

            print("Autore mancante")
            risp="Non \u00E8 stato specificato il filosofo o non lo conosco"
            risp2=" "
            Ns=False

            
            client_socket.sendall(risp.encode())
            time.sleep(0.1)
            client_socket.sendall(risp2.encode())
            return
        if A:
            print("Solo dove")
            if (Ver(a,listF)==0):
               print("Aristotele")
               if risp==" ":
                   risp="Aristotale ha vissuto a Stagira,Atene,Lesbo,Calcide,Macedonia\n"
                   Ns=False
               else:
                   risp2="Aristotale ha vissuto a Stagira,Atene,Lesbo,Calcide,Macedonia"
                   Ns=False
                   

            elif (Ver(a,listF)==1):
               print("Socrate")
               if risp==" ":
                   risp="Socrate ha vissuto ad Atene Classica,Grecia\n"
                   Ns=False
               else:
                   risp2="Socrate ha vissuto ad Atene Classica,Grecia"
                   Ns=False
               
            elif (Ver(a,listF)==2):
               print("Platone")
               if risp==" ":
                   risp="Platone ha vissuto ad Atene,Megara,Siracusa\n"
                   Ns=False
               else:
                   risp2="Platone ha vissuto ad Atene,Megara,Siracusa"
                   Ns=False

        if Ns:
           risp="Non ho capito\n"
           risp2="Controlla la domanda"



           
    
   else:
        print("Senza domanda")
        


        if (Ver(a,listF)==0):

               print("Aristotele")
               if(Ver(a,listN))>=0:
                print("Nascita")
                if risp==" ":

                 risp="Aristotale nacque nel 384 A.C\n"
                 Ns=False
                else:
                 risp2="Aristotale nacque nel 384 A.C\n"
                 Ns=False

               if risp==" ":
                   risp="Aristotele (in greco antico: Ἀριστοτέλης, Aristotélēs, pronuncia:  Stagira, 384 a.C. o 383 a.C. – Calcide, 322 a.C.)\n è stato un filosofo, scienziato e logico greco antico,\n ritenuto una delle menti più universali, innovative, prolifiche e influenti di tutti i tempi, sia per la vastità che per la profondità dei suoi campi di conoscenza.\n Insieme a Platone, suo maestro, e a Socrate è considerato uno dei padri del pensiero filosofico occidentale, che soprattutto da lui ha ereditato problemi, termini, concetti e metodi.\n"
                   Ns=False
               
                   risp2="L'aristotelismo ed  sta ad indicare sia la dottrina di Aristotele, sia le correnti filosofiche dei suoi discepoli che in diversi periodi ripresero e svilupparono il pensiero originale del maestro."
                   
                   

        elif (Ver(a,listF)==1):
                print("Socrate")
                if(Ver(a,listN))>=0:
                    if risp==" ":
                     risp="Nel 470 o 469  A.C non c'\u00E8 una data certa\n"
                     Ns=False
                    else:
                        risp2="Nel 470 o 469  A.C non c'\u00E8 una data certa\n"
                        Ns=False

                if risp==" ":
                   risp="Socrate (in greco antico: Σωκράτης, Sōkrátēs, pronuncia: [sɔː'kratɛːs]; Atene, 470 a.C./469 a.C. – Atene, 399 a.C.) è stato un filosofo greco antico, uno dei più importanti esponenti della tradizione filosofica occidentale.\n Il contributo più importante che egli ha dato alla storia del pensiero filosofico consiste nel suo metodo d'indagine: il dialogo che utilizzava lo strumento critico dell'elenchos (ἔλεγχος, élenchos = confutazione) \n applicandolo prevalentemente all'esame in comune (ἐξετάζειν, exetàzein) di concetti morali fondamentali. Per questo Socrate è riconosciuto come padre fondatore dell'etica o filosofia morale.\n"
                   Ns=False
               
                   risp2="Questa non la so manco io"
                   
               
        elif (Ver(a,listF)==2):
                print("Platone")
                if(Ver(a,listN))>=0:
                    if risp==" ":
                     risp="Platone nacque nel 428 A.C\n"
                     Ns=False
                    else:
                        risp2="Platone nacque nel 428 A.C\n"
                        Ns=False
                if risp==" ":
                   risp="Platone ha vissuto ad Atene,Megara,Siracusa\n"
                   Ns=False
              
                   risp2="l platonismo è una corrente filosofica risalente a Platone. Il filosofo greco affermava l'esistenza di una più alta verità: le Idee, delle forme ideali eterne, immutabili, e incorruttibili, da cui ha origine il mondo sensibile, quale noi lo percepiamo, soggetto al divenire, alla corruzione, e alla morte."
                   

        if Ns:
           risp="Non ho capito\n"
           risp2="Controlla la domanda"

   client_socket.sendall(risp.encode())
   time.sleep(0.1)
   client_socket.sendall(risp2.encode())




def Ver(a,listG):
    c=int(len(a))
    P=0
    
    for P in range(c):
        if a[P] in listG:
            f=listG.index(a[P])
            return f
    return -1

if __name__ == "__main__":
    main()