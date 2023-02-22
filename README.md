# algia-web
algia CLI command backed server-side rendering Nostr web client

- [algia](https://github.com/mattn/algia) is a tool and very simple client for using micro blog application with Nostr protcol developed by [mattn](https://github.com/mattn)

## Difference with other clients
- Handling of Nostr protcol is done by your machine running server program of algia-web
  - algia is simple Nostr client which can run on CLI environmet
  - At a point of view, algia-web is a kind of wrapper client of the client running on the machine (=algia)
- Your web browser only renders contents received from the server
- This architecture can save communiaction amount and buttery consumption of your smartphone and other mobile devices you use Nostr with Web browser at
- does not offers rich UI/UX and support many features as Nostr client
- is developed in assumption that it is not used as main client and is used when you do not have power supply or connect to The internet via mobile network which has restriction of total communication amount

## Requiements 
- A machine which can be accessible from your device
  - Mostly the machine must have global IP address

## Needed steps to use algia-web client
- Setup of algia and executing server program of algia-web at your machine mentioned above
  - Includes making 8080 port (default) accecible from The internet

## Usage
- Please read [algia-serv.py](https://github.com/ryogrid/algia-web/blob/main/algia-serv.py) and modify it if you need!

## Screen capture (on Smartphone)
<img src="https://user-images.githubusercontent.com/24614/220373073-41f74529-309d-4d0a-b23a-9a3741480aac.png" width="411px" height="960px" border="5" >
