
import socket
from robot.api.deco import library, keyword


ROBOT_AUTO_KEYWORDS = False


@library(scope="GLOBAL")
class TcpClient(object):
    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    @keyword("TCP Client connect to server")
    def connect(self, ip: str, port: int, timeout: int = 2):
        self._sock.connect((ip, port))
        self._sock.settimeout(timeout)
        
    @keyword("TCP Client send data to server")
    def send(self, msg)
        self._sendall(msg, 0)
      
    @keyword("TCP Client recv data from server")
    def recv(self):
        msg = self._sock.recv(8164, 0)
        return msg
