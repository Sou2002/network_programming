import os
import socket
import tqdm


# A class to transfer files
class FileTransfer:
    '''
    '''

    def __init__(self, port_number: int=8000) -> None:
        '''
        '''
        self.__PORT: int = port_number # Port Number

    # A method to send file
    def send(self, file_path: str, HOST: str="localhost") -> None:
        '''
        '''
        # Creating a sender socket
        # socket.AF_INET = Internet IPv4
        # socket.SOCK_STREAM = TCP Connection
        __sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connecting with receiver
        __sender_socket.connect((HOST, self.__PORT))

        # Reading the file
        __file = open(file_path, 'rb')
        __file_size: int = os.path.getsize(file_path)

        # Sending the file size for progress bar
        __sender_socket.send(str(__file_size).encode())

        # Sending the file
        try:
            __sent_size: int = __sender_socket.sendfile(__file)

            if __file_size == __sent_size:
                print("File sent successfully!")
                print(f"File size = {format(__sent_size / (2 ** 20), '.2f')} MB")

        except socket.error as err:
            print(err)

        # Closing file and socket
        __file.close()
        __sender_socket.close()

    # A method to receive file
    def receive(self, rec_file_path: str, IP_ADDRESS: str="localhost") -> None:
        '''
        '''
        # Creating a receiver socket
        # socket.AF_INET = Internet IPv4
        # socket.SOCK_STREAM = TCP Connection
        __receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        __receiver_socket.bind((IP_ADDRESS, self.__PORT))

        # Listening to incoming request
        __receiver_socket.listen()

        # Accepting sender
        __sender_socket, __sender_address = __receiver_socket.accept()

        # Receiving the file size for progress bar
        file_size: int = int(__sender_socket.recv(1024).decode())

        # Progress bar
        progress_bar = tqdm.tqdm(unit="MB", unit_scale=True, unit_divisor=1024, total=file_size)

        # Receiving data
        __file_byte = b""

        while True:
            __data = __sender_socket.recv(1024)

            if not __data:
                break

            __file_byte += __data

            progress_bar.update(1)

        # Writing data in a file
        __file = open(rec_file_path, 'wb')
        __file.write(__file_byte)

        # Closing file and socket
        __file.close()
        __sender_socket.close()
        __receiver_socket.close()


if __name__ == '__main__':
    PATH = 'data/img.png'
    ft = FileTransfer()
    ft.send(PATH)
