#A distributed system.
This repository contains simple client-server scripts written in Python. The client script can send commands to be broadcast over the network and check ranks of the sending nodes if lower or higer and only excecutes the hiher ranked, while the server script listens for incoming requests and sends back responses and broadcasts the command to all other nodes of the nerwork.

##Prerequisites

    Python 3.x

##Usage

    Clone the repository to your local machine.

##shell

$ git clone https://github.com/stillthskin/distributed-system.git

    Run the server script in a terminal window.


$ python3 server.py

    Run the client script in another terminal window.



$ python3 client.py

    Type a command in the client terminal window and press Enter. The message will be sent to the server, which will process it and send back a response.

###Contributions

Contributions are welcome! If you find any bugs or have ideas for new features, feel free to open an issue or submit a pull request.
###License

This project is licensed under the MIT License - see the LICENSE file for details.
