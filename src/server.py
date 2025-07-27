"""
# server.py
This module is just to see how to create a server using Python's socket library and handle basic connections.

Run this script to start a server that listens on localhost at port 4221.
with this command:
    ```bash
    pyhon -m src.server
    ```
"""

import socket

class Server():
    def __init__(self, host:str, port: int):
        """
        Initialize the server with a host and port.

        Args:
            host (str): The hostname or IP address to bind the server to.
            port (int): The port number to bind the server to.
        """
        self.host = host
        self.port = port
        self.server_scoket = self.create_server()

    def create_server(self) -> None:
        """
        Create a server connection using specified host and port.

        Args: 
            host(str):  The hostname or IP address to bind the server to.
            port(int):  The port number to bind the srever to.

        Returns:
            socket.socket: A socket object representing the server.
        """ 

        server_socket = socket.create_server((self.host, self.port), reuse_port = True)
        # above line crates a socket that listens for incoming connections but resuse poert does not work on Windows

        server_socket.listen()

        # print(f" server listening on {host}:{port}")
        # while True:
        #     client_socket, addr = server_socket.accept()
        #     print(f"Connection from {addr} has been established.")

        #     client_socket.close()  # Close the client socket after handling it

    def recieve_data(self) -> str:
        """
        Recieve the data or request from the client.
        """
        client_socket = self.server_scoket.accept()[0]  # Accept a connection and get the client socket
        data = client_socket.recv(1024)
        if not data:
            return ""
        return data.decode('utf-8')
    
    def send_data(self, data: str):
        """
        Send data to the client.

        Args:
            data (str): The data to send to the client.
        """
        client_socket = self.server_scoket.accept()[0]

        client_socket.sendall(data.encode('utf-8'))
        client_socket.close()  # Close the client socket after sending data


if __name__ == "__main__":

    server = Server("localhost", 4221)

    data = "Hello World!"

    server.send_data(data)

    print("Server is running and sent data to the client.")

    server_data = server.recieve_data()

    print(f"Received data from client: {server_data}")

