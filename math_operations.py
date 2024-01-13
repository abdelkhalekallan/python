import socket

# إنشاء مأخذ TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ربط المأخذ بعنوان ومنفذ
server_address = ('localhost', 8080)
server_socket.bind(server_address)

# الاستماع للاتصالات الواردة
server_socket.listen()

print('Waiting for a connection...')

# قبول الاتصال
client_socket, client_address = server_socket.accept()
print(f'Connection from {client_address}')

# قراءة وطباعة البيانات المستلمة
data = client_socket.recv(1024)
print(f'Received: {data.decode()}')

# إرسال بيانات إلى العميل
client_socket.send(b'Hello, client!')

# إغلاق المأخذ
client_socket.close()
server_socket.close()
