from lab1.server import start_server
import argparse


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument("--port", '-p', type=int, help='Set server port', default=8080)
    parse.add_argument("--directory", "-d", type=str, help='Set directory',
                       default='C:/Users/Nikita/PycharmProjects/AIPOS/lab1/server_files/')
    args = parse.parse_args()
    start_server(port=args.port, path=args.directory)
