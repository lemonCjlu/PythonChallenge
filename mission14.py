import xmlrpc.client
#XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP as a transport. With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.

#获取evil4.jpg图片的内容，就是要打电话的人即evil
with open('evil4.jpg') as f:
    print(f.read())

server_proxy = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php') #A ServerProxy instance is an object that manages communication with a remote XML-RPC server.
methods = server_proxy.system.listMethods() #This method returns a list of strings, one for each (non-system) method supported by the XML-RPC server.
print(methods)
print(server_proxy.system.methodHelp('phone'))
print(server_proxy.phone('Bert'))#调用远程服务器的phonw方法