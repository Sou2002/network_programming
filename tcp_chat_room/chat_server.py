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
        for socket in self.__clients:
            socket.send(message)

    # A method to handle clients
    def __manage_clients(self, client_socket) -> None:
        '''
        '''
        while True:
            try:
                # Receiving message from user and broadcast to everyone
                message = client_socket.recv(1024)
                self.__broadcast(message=message)

            except:
                # Removing user from the chat
                removed_user: str = self.__clients.pop(client_socket)
                self.__broadcast(f"{removed_user} has left!".encode())
                client_socket.close()
                break

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
