import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer
import threading
import os
import hashlib
import base64

def CalcularChecksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

def PegarArquivosLocais():
    files = {}
    for file in os.listdir('.'):
        if os.path.isfile(file):
            checksum = CalcularChecksum(file)
            files[file] = checksum
    return files

def RegistrarnoBorda(edge_node_host, edge_node_port, node_host, node_port):
    with xmlrpc.client.ServerProxy(f'http://{edge_node_host}:{edge_node_port}/') as proxy:
        local_files = PegarArquivosLocais()
        proxy.AddNo(node_host, node_port, local_files)
        for file, checksum in local_files.items():
            proxy.RegistrarArq(node_host, node_port, file, checksum)

def BaixarArquivodoNo(node_host, node_port, filename):
        with xmlrpc.client.ServerProxy(f'http://{node_host}:{node_port}/') as proxy:
            file_data = proxy.download(filename)
            file_data_bytes = base64.b64decode(file_data)
            with open(filename, 'wb') as f:
                f.write(file_data_bytes)
            return f"'{filename}' foi baixado com sucesso!"


def handle_download_request(filename):
    print(f"Foi solicitado o download do arquivo: {filename}")
    return BaixarArquivodoNo(filename)

def start_node(node_host, node_port, edge_node_host, edge_node_port):
    server = SimpleXMLRPCServer((node_host, node_port), allow_none=True)
    
    def download_file(filename):
        if os.path.isfile(filename):
            with open(filename, 'rb') as f:
                return base64.b64encode(f.read()).decode('utf-8')
        else:
            raise FileNotFoundError(f"O arquvio: '{filename}' não foi encontrado.")

    server.register_function(download_file, "download")
    
    threading.Thread(target=server.serve_forever).start()
    RegistrarnoBorda(edge_node_host, edge_node_port, node_host, node_port)
    print(f"Nó rodando em: {node_host}:{node_port}")

if __name__ == "__main__":
    node_host = 'localhost'
    node_port = 8002
    edge_node_host = '35.230.44.29'
    edge_node_port = 8000
    start_node(node_host, node_port, edge_node_host, edge_node_port)

    while True:
        filename = input("Digite o nome do arquivo ou 'sair': ")
        if filename.lower() == 'sair':
            break
        
        try:
            with xmlrpc.client.ServerProxy(f'http://{edge_node_host}:{edge_node_port}/') as proxy:
                node_info = proxy.EncontrarNoArq(filename)
                if node_info:
                    node_host, node_port = node_info
                    print(f"Arquivo '{filename}' foi encontrado no nó {node_host}:{node_port}. Baixando...")
                    result = BaixarArquivodoNo(node_host, node_port, filename)
                    print(result)
                else:
                    print(f"Arquivo não encontrado")
        except Exception as e:
            print(f"Erro ao se conectar com o borda: {e}")
