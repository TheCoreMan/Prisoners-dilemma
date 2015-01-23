import os
import threading
import webbrowser


class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Starting server")
        run_server()


def run_server():
    cur_dir = os.path.dirname(__file__)
    server_line = os.path.join(cur_dir, "manage.py") + " runserver 8080"
    print("Running " + server_line)
    os.system(server_line)


def run_browser():
    webbrowser.open("http://localhost:8080")


def main():
    thread1 = ServerThread()
    thread1.start()
    run_browser()
    thread1.join()


if __name__ == "__main__":
    main()
