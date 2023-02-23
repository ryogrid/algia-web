# algia-web
algia CLI command backed server-side rendering Nostr web client

- [algia](https://github.com/mattn/algia) is a tool and very simple client for using micro blog application with Nostr protcol developed by [mattn](https://github.com/mattn)

## Difference with other clients
- Handling of Nostr protcol is done by your machine running server program of algia-web
  - algia is simple Nostr client which can run on CLI environmet
  - At a point of view, algia-web is a kind of wrapper client of the client running on the machine (=algia)
- This architecture can save communiaction amount and buttery consumption of your smartphone and other mobile devices you use Nostr with Web browser at
- Your web browser only renders contents received from the server
  - **Almost all of clients for mobile devices handle messages received from relay server by myself. But the job consumes not small amount of computation and network resources**
  - **Above job is ofen not acceptable for some people who use mobile devices out of doors**
- does not offers rich UI/UX and support many features as Nostr client
- is developed in assumption that it is not used as main client and is used when you do not have power supply or connect to The internet via mobile network which has restriction of total communication amount

## Requiements 
- A machine which can be accessible from your device
  - Mostly the machine must have global IP address

## Needed steps to use algia-web client
- Setup of algia and executing server program of algia-web at your machine mentioned above
  - Includes making 8080 port (default) accecible from The internet
- Procedure
  1. Setup [algia](https://github.com/mattn/algia) for your Nostr account
  1. Setup python environment
  1. Setup algia-web server
     1. $ git clone https://github.com/ryogrid/algia-web.git
     1. $ cd algia-web
     1. $ pip install -r requirements.txt
     1. $ python algia-serv.py
        - bind port is 8080 (default). if you want change port edit last line of algia-serv.py
     1. Make the server program accecible from the Internet
        - In many cases, you should configure firewall software on your machine (iptables, firewalld ... etc)
  1. Access http://[global address of your server machine]:8080/
## Usage detail
- Please read [algia-serv.py](https://github.com/ryogrid/algia-web/blob/main/algia-serv.py) and [index.html](https://github.com/ryogrid/algia-web/blob/main/templates/index.html). And Please modify these if you need!

## Screen capture (on Smartphone)
<img src="https://user-images.githubusercontent.com/24614/220607489-c1256934-1b7d-4a75-83b3-861b8d05be32.png"  width="411px" height="960px">
