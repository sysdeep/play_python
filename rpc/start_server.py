from app.server.server import Server


def main():

    server = Server()
    server.start('localhost', 9191)


if __name__ == '__main__':

    main()
