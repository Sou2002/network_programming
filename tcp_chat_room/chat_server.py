import socket
import threading


# Chat Server Class
class ChatServer:
    '''
    A class to host the chat server.

    Methods
    -------
    start_server():
        Run this method to start the server.
    '''

    def __init__(self, ip_address: str = "localhost", port_number: int = 8001) -> None:
        '''
        Constructs all necessary attributes for the ChatServer object.

        Parameters
        ----------
        ip_address: str, optional
            Selected IP Address to host the chat service, default value "localhost".
        port_number: int, optional
            Selected port number to uniquely identify the service, default port 8001.
        '''
        # Creating the server socket
        # socket.AF_INET = Internet IPv4
        # socket.SOCK_STREAM = TCP Connection
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((ip_address, port_number))

        self.__clients: dict = {}

    # A method to brodcast message
    def __broadcast(self, message: bytes) -> None:
        '''
        Broadcasts the message among all users who are connected to the chat server.

        Parameters
        ----------
        message: bytes
            Encoded message in bytes format.

        Returns
        -------
            None
        '''
        for socket in self.__clients:
            socket.send(message)

    # A method to handle clients
    def __manage_client(self, client_socket) -> None:
        '''
        Receives message from user and broadcast the message to every user.

        Parameters
        ----------
        client_socket: socket
            Socket of client. 

        Returns
        -------
            None
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

    # A method to accept clients
    def __accept_client(self) -> socket:
        '''
        Accepts client to join the server.

        Parameters
        ----------
            None

        Returns
        -------
        client_socket: socket
            Socket of the accepted client.
        '''
        client_socket, client_address = self.__server.accept()
        print(f"{str(client_address)} connected!")

        # Sending req to client to send username
        client_socket.send("SEND USERNAME".encode())
        username: str = client_socket.recv(1024).decode()

        # Adding user in the clients dict
        self.__clients[client_socket] = username
        self.__broadcast(f"{username} joined the chat!".encode())

        return client_socket

    # A method to receive message
    def __receive(self) -> None:
        '''
        Creates receiving thread for accepted user.

        Parameters
        ----------
            None

        Returns
        -------
            None
        '''
        while True:
            client_socket = self.__accept_client()

            # Creating thread for handling multiple simultaneously
            user_thread = threading.Thread(
                target=self.__manage_client, args=(client_socket,))
            user_thread.start()

    # A method to start the chat server
    def start_server(self) -> None:
        '''
        Run this method to start the server.

        Parameters
        ----------
            None

        Returns
        -------
            None
        '''
        # Starting server
        self.__server.listen()
        print("Server started.")
        print("Waiting for user to join...")
        self.__receive()


if __name__ == '__main__':
    cs = ChatServer()
    cs.start_server()
