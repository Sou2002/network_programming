import socket
import threading


# Chat Client Class
class ChatClient:
    '''
    A class to perfprm chat operation on client side.

    Methods
    -------
    start_client():
        Run this method to connect the client to the server.
    '''

    def __init__(self, ip_address: str = "localhost", port_number: int = 8001) -> None:
        '''
        Constructs all necessary attributes for the ChatClient object.

        Parameters
        ----------
        ip_address: str, optional
            Selected IP Address to connect to the chat server, default value "localhost".
        port_number: int, optional
            Selected port number to uniquely identify the host service, default host port 8001.
        '''
        # Creating the server socket
        # socket.AF_INET = Internet IPv4
        # socket.SOCK_STREAM = TCP Connection
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client.connect((ip_address, port_number))

        self.__username: str = input("Enter your username: ")

    # A method to recieve message from server
    def __recieve(self) -> None:
        '''
        Receives message from the chat server.

        Parameters
        ----------
            None

        Returns
        -------
            None
        '''
        while True:
            try:
                message: str = self.__client.recv(1024).decode()

                # Check server is asking for username otherwise print the message
                if message == "SEND USERNAME":
                    self.__client.send(self.__username.encode())
                else:
                    print(message)

            except:
                print("An error occured!")
                self.__client.close()
                break

    # A method to send message to server
    def __send(self) -> None:
        '''
        Sends message to the chat server.

        Parameters
        ----------
            None

        Returns
        -------
            None
        '''
        while True:
            print ("\033[A                             \033[A")
            message: str = f"{self.__username}: {input()}"
            self.__client.send(message.encode())

    # A method to start the client
    def start_client(self) -> None:
        '''
        Run this method to connect the client to the server.

        Parameters
        ----------
            None

        Returns
        -------
            None
        '''
        # Starting receiving thread
        receiving_thread = threading.Thread(target=self.__recieve)
        receiving_thread.start()

        # Starting receiving thread
        sending_thread = threading.Thread(target=self.__send)
        sending_thread.start()


if __name__ == '__main__':
    cc = ChatClient()
    cc.start_client()
