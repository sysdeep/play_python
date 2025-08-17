import docker
from app.main_window import MainWindow


def main():

    docker_client = docker.from_env()

    win = MainWindow(docker_client)
    win.mainloop()


if __name__ == "__main__":
    main()
