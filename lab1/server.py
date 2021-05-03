import logging
import mimetypes
import socket
import threading
from math import ceil

logging.basicConfig(filename="log.txt", level=logging.INFO, filemode='w')


def start_server(port, path):
    global FILE_PATH
    FILE_PATH = path
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("localhost", port))
        logging.info(f"Server is running on localhost:{port}.")
        server.listen(5)
        logging.info("Server is waiting for connection.")
        while True:
            conn, addr = server.accept()
            logging.info(f"Server connected with {addr}")
            thread = threading.Thread(target=connected_user, args=(conn, addr))
            thread.start()


def parse_request(text, header_dict):
    if header_dict['method'] == "GET":
        return get_request(header_dict)
    elif header_dict['method'] == "POST":
        return post_request(text, header_dict)
    elif header_dict['method'] == "OPTIONS":
        return option_request()


def build_header(status_code, status_text) -> str:
    header = "HTTP/1.1 " + status_code + " " + status_text + " \r\n"
    header += "Access-Control-Allow-Origin: " + "http://localhost:8080/" + "\n"
    header += "Access-Control-Allow-Method: " + "POST, GET, OPTIONS" + "\r\n"
    return header


def parse_header(text: str):
    header_dict = dict()
    header_dict['method'] = text.split(" ")[0]
    header_dict['filepath'] = text.split(' ')[1].split('/')[1]
    try:
        header_dict['content_size'] = int(text.split('Content-Length:')[1].split('\r')[0])
    except:
        header_dict['content_size'] = len(text)
    return header_dict


def post_request(text, header_dict):
    filepath = FILE_PATH
    filepath += header_dict['filepath']
    if text.split()[0] == header_dict['method']:
        message = text.split('\r\n\r\n')[1]
        with open(filepath, "w") as file:
            file.write(message)
    else:
        message = text
        with open(filepath, "a") as file:
            file.write(message)
    try:
        with open(filepath, "rb") as file:
            response = file.read()

    except Exception:
        header = build_header('500', 'Internal Server Error')
        header += 'Content-Type: ' + mimetypes.types_map['.html'] + "\r\n"
        response = '<html><body><center><h3>Error 500: Internal Server Error</h3><p>Python HTTP ' \
                   'Server</p></center></body></html>'.encode('utf-8')
        status = 'Error'
    else:
        header = build_header('200', 'OK')
        header += "Content-Type: " + mimetypes.types_map['.json'] + '\r\n'
        status = 'OK'

    return header, response, status


def option_request():
    response = ""
    return build_header("200", "OK"), response.encode(), 'OK'


def get_request(header_dict):
    filepath = FILE_PATH
    filepath += header_dict['filepath']
    try:
        with open(filepath, 'rb') as my_file:
            response = my_file.read()
    except Exception:
        header = build_header("404", "Not Found")
        header += 'Content-Type: ' + mimetypes.types_map['.html'] + "\r\n"
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP ' \
                   'Server</p></center></body></html>'.encode('utf-8')
        status = 'Error'
    else:
        content_type = mimetypes.types_map["." + filepath.split(".")[1]]
        header = build_header("200", "OK")
        header += 'Content-Type: ' + content_type + "\r\n"
        status = 'OK'

    return header, response, status


def connected_user(conn, addr):
    logging.info(f"Server received from {conn} request.")
    package_size = 4096
    message = conn.recv(package_size)
    header_dict = parse_header(message.decode())
    header, response, status = parse_request(message.decode(), header_dict)

    if status == 'OK':
        for _ in range(ceil(header_dict['content_size'] / package_size) - 1):
            message = conn.recv(package_size)
            header, response, status = parse_request(message.decode(), header_dict)
            if status == 'Error':
                break

    print(header)
    logging.info('\n' + header)
    data = header
    data = data.encode()
    if len(response) != 0:
        data += "\r\n".encode()
        data += response
    conn.sendall(data)
    logging.info(f"Server sent {addr} message,\n message = {data} ")
