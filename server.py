import socket
from _thread import *
from player import Player
import pickle
import pygame

server = "127.0.0.1"
port = 12000
currentPlayer = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = [Player(0, 0, 16, 16, (255, 0, 0)), Player(784, 0, 16, 16, (0, 0, 255))]


def threaded_client(conn, player):
    global currentPlayer
    conn.send(pickle.dumps(players[player]))
    reply = ""
    clock = pygame.time.Clock()
    while True:
        clock.tick(15)
        try:
            print("1")
            data = pickle.loads(conn.recv(10240))
            print("2")
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)
            print("3")
            conn.sendall(pickle.dumps(reply))
        except Exception as e:
            print(e)
            break

    print("Lost connection")
    conn.close()


def main():
    global currentPlayer
    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)

        start_new_thread(threaded_client, (conn, currentPlayer))
        currentPlayer += 1
    s.close()


if __name__ == '__main__':
    main()
