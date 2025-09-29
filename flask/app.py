from flask import Flask, request, jsonify
from neo4j import GraphDatabase
import socket
import os

app = Flask(__name__)

# Usar variables de entorno para las credenciales de Neo4j
NEO4J_URI = os.environ.get('NEO4J_URI', 'bolt://jorge-neo4j:7687')
NEO4J_USER = os.environ.get('NEO4J_USER', 'neo4j')
NEO4J_PASSWORD = os.environ.get('NEO4J_PASSWORD', 'supersecurepassword')

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

INSTANCE_ID = os.environ.get('HOSTNAME', socket.gethostname())

@app.route("/", methods=["GET"])
def root():
    """Endpoint raíz para verificar que la API está funcionando"""
    return jsonify({
        "message": "Flask API is running",
        "service": "flask-api",
        "instance_id": INSTANCE_ID,
        "hostname": socket.gethostname(),
        "endpoints": ["/health", "/usuarios"]
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)