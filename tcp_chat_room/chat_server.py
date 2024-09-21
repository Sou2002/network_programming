import socket
import threading


# Chat Server Class
class ChatServer:
    '''
    '''

    def __init__(self, ip_address: str = "localhost", port_number: int = 8001) -> None:
        '''
        '''
        self.IP_ADDRESS: str = ip_address  # Host IP Address
        self.PORT: int = port_number  # Port Number

        # Creating the server socket
        # socket.AF_INET = Internet IPv4
        # socket.SOCK_STREAM = TCP Connection
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((self.IP_ADDRESS, self.PORT))

        self.__clients: dict = []

    # A method to brodcast message
    def __broadcast(self, message: bytes) -> None:
        '''
        '''
        for nickname, socket in self.__clients:
            socket.send(message)

    # A method to receive message
    def __receive(self) -> None:
        '''
        '''
        pass

    # A method to start the chat server
    def start_server(self) -> None:
        '''
        '''
        pass


if __name__ == '__main__':
    pass
