# ServerFilosofi
A client-server application in Python that answers client requests.
## Description
The part in English is below.

Questo è un piccolo progetto che ho creato durante la mia carriera scolastica alle superiori.
È uno script python che fa comunicare un client ed un server, il client presenta un'interfaccia grafica basilare realizzata con tkinter.
Il funzionamento è il seguente: 
il client formula la domanda e la invia al server, il server analizzando la domanda parola per parola è in grado di capire la maggiorparte delle domande che riguardano i filosofi scelti
|Aristotele, Socrate, Platone|
Il progetto può essere usato come esempio per il funzionamento dei socket o come base per qualche progetto futuro.

This is a simple project i made during my academic career.
It is a python script that makes client and server comunicate, the client has a graphic user interface built with tkinter.
The way it works is as follows:
the client formulates the question and send it to server, The server analyzes the question word for word in order to understand it.
The questions should be about these philosophers:
|Aristotele, Socrate, Platone|
This project can be used as an example of how sockets work or as a foundation for future projects."

## Prerequisites
- Python 3.7 or higher
- It require all the libraries listed in the libraries section

## Libraries
///////////////////////////////////////////////////
                        Client
- socket
- threading
- json
- os
- tkinter
- sys
- time
//////////////////////////////////////////////////
                        Server
- socket
- json
- queue
- threading
- time
- random
- os
- multiprocessing

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Carlo3406/ServerFilosofi