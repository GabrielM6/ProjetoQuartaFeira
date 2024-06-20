from xmlrpc.server import SimpleXMLRPCServer
import threading
import xmlrpc.client
import time

nodes = {}
files = {}

sair = False

def AddNo(node_host, node_port, node_files):
    nodes[(node_host, node_port)] = node_files
    return True

def RegistrarArq(node_host, node_port, filename, checksum):
    if filename not in files:
        files[filename] = []
    files[filename].append((node_host, node_port, checksum))
    return True

def EncontrarArq(filename):
    if filename in files:
        return files[filename]
    return []

def ChecarArqNo():
    while not sair:
        print("Checando arquivos nos nós:")
        for (node_host, node_port), node_files in nodes.items():
            print(f"Nó {node_host}:{node_port} possui estes arquivos:")
            for filename, checksum in node_files.items():
                print(f"{filename}")
        print("")

        time.sleep(2)

def monitorar_entrada():
    global sair
    input("Aperte Enter para sair\n")
    sair = True
        
        

def EncontrarNoArq(filename):
    for (node_host, node_port), node_files in nodes.items():
        if filename in node_files:
            return (node_host, node_port)
    return None

def AcharNoArq(edge_node_host, edge_node_port):
    server = SimpleXMLRPCServer((edge_node_host, edge_node_port), allow_none=True)
    server.register_function(AddNo, "AddNo")
    server.register_function(RegistrarArq, "RegistrarArq")
    server.register_function(EncontrarArq, "EncontrarArq")
    server.register_function(EncontrarNoArq, "EncontrarNoArq")

    
    threading.Thread(target=server.serve_forever).start()
    threading.Thread(target=ChecarArqNo).start()
    print(f"Nó de borda operando em: {edge_node_host}:{edge_node_port}")

if __name__ == "__main__":
    edge_node_host = '0.0.0.0'
    edge_node_port = 8000
    AcharNoArq(edge_node_host, edge_node_port)
    monitorar_entrada()
