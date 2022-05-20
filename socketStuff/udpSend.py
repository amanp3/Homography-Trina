import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(("10.195.245.31", 54002))
sock.close()

# while True:
#     message = bytes("{}, {}, {}".format(time.time(), 0., 0.), "utf-8")
    
#     #sock.sendto(message, ("10.194.249.31", 61557))
#     data, addr = sock.recvfrom(1024)
    
#     data = data.decode("utf-8")
#     data_tuple = [float(s) for s in data.split(",")]
#     td = time.time() - data_tuple[0]
#     print("RTT Latency: {:.3f}".format(td))
#     time.sleep(0.1)