# algia-web
algia cli command backed server-side nostr web client

- [algia](https://github.com/mattn/algia) developped by [mattn](https://github.com/mattn)

## Difference with other clients
- Handling of Nostr protcol is done by your machine running server program of algia-web
  - Algia is simple Nostr client which can run on CLI environmet
  - At a point of view, algia-web is a kind of wrapper client of the client running on the machine (=algia)
- Your web browser only renders contens received from the server
- This architecture can save communiaction amount and buttery consumption of your smartphone and other mobile devices you use Nostr with Web browser at

## Requiements 
- A machine which can be accessible from your device
  - Mostly the machine must have global IP address

## Needed steps to use algia-web client
- Setup of algia and executing server program of algia-web at the machine
  - Includes Making 8080 port (default) accecible from The internet
