import socket
import threading


# Chat Client Class
class ChatClient:
    '''
    '''
    def __init__(self, ip_address: str = "localhost", port_number: int = 8001) -> None:
        '''
        '''
        # Creating the server socket
        # socket.AF_INET = Internet IPv4
        # socket.SOCK_STREAM = TCP Connection
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client.connect((ip_address, port_number))

        self.__username: str = input("Enter a username:")

    # A method to recieve message from server
    def __recieve(self) -> None:
        '''
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
        '''
        pass

    def start_client(self) -> None:
        '''
        '''
        pass


if __name__ == '__main__':
    pass
