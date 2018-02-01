class connection_test:

    def __int__(self, ip_addr, ip_port):
        self.ip_addr = ip_addr
        self.ip_port = ip_port

    def try_connect(self, page=None):
        self.page = page
        connect_info = (self.ip_addr, self.ip_port)
        page_core = "/ HTTP/1.1"
        page_get = "GET "
        page_close = "\r\n\r\n"
        if page == None:
            page_final = page_get + page_core + page_close
        else:
            page_final = page
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(connect_info)
            s.send(page_final.encode(encoding='utf-8'))
            msg = []
            msg.append(s.recv(1024).decode('ascii'))
            s.close()
            return msg
        except (ConnectionError,TimeoutError) as e:
            print(e)

    def get_msg_distance(self, msg):
        self.msg = msg
        print(i.decode('ascii'))

import socket

result = []
new_test1 = connection_test()
new_test2 = connection_test()

new_test1.ip_addr = "spiraledthoughts.com"
new_test1.ip_port = 80
new_test2.ip_addr = "maps.googleapis.com"
new_test2.ip_port = 80

endstr = []
word = ""
result = new_test2.try_connect("GET /maps/api/distancematrix/json?origins=Flagstaff+AZ&destinations=Phoenix+AZ&mode=driving&sensor=false\r\n")
for i in result:
    for j in i:
        print(j)
        word += j
    endstr.append(word)

print(len(endstr))
print(endstr[len(endstr)-1])
