from cassandra.cluster import Cluster

class ConexionCassandra():
    def __init__(self):
        self.cluster = Cluster(['127.0.0.1'])
        self.session = self.cluster.connect('tiendainstrumentos')

    def cerrarConexion(self):
        self.session.shutdown()
        self.cluster.shutdown()