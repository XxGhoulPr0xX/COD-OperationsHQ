import com.mongodb.*;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.List;

public class BaseDeDatos {
    private final static String HOST = "localhost";
    private final static int PORT = 27017;

public static MongoClient conectar() {
    try {
        MongoClient mongoClient = new MongoClient(HOST, PORT);
        return mongoClient;
    } catch (UnknownHostException e) {
        System.err.println("Error al conectar con el host: " + e.getMessage());
        return null;
    }
}

    public static void insertarMusica(DB db, String id, String formato, String autor, int anio, String titulo) {
        DBCollection coll = db.getCollection("Musica");
        BasicDBObject doc = new BasicDBObject("_id", id)
                .append("Formato", formato)
                .append("Autor", autor)
                .append("Anio", anio)
                .append("Titulo", titulo);
        coll.insert(doc);
    }

        public static List<DBObject> consultarMusicaPorId(DB db, String id) {
            List<DBObject> resultados = new ArrayList<>();
            DBCollection coll = db.getCollection("Musica");
            BasicDBObject query = new BasicDBObject("_id", id); // Filtro por el campo _id
            DBCursor cursor = coll.find(query);
            while (cursor.hasNext()) {
                resultados.add(cursor.next());
            }
            return resultados;
        }


    public static void main(String args[]) throws UnknownHostException {
        try {
            MongoClient mongoClient = conectar();
            DB db = mongoClient.getDB("Musica");
            List<DBObject> resultados = consultarMusicaPorId(db,"14964");
            for (DBObject resultado : resultados) {
                System.out.println(resultado);
            }
            mongoClient.close();
        } catch (MongoException e) {
            System.err.println("Error al interactuar con la base de datos: " + e.getMessage());
        }
    }
}
