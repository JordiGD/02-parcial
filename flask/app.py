from flask import Flask, request, jsonify
from neo4j import GraphDatabase
import socket
import os
import logging
from datetime import datetime

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

NEO4J_URI = os.environ.get('NEO4J_URI', 'bolt://jorge-neo4j:7687')
NEO4J_USER = os.environ.get('NEO4J_USER', 'neo4j')
NEO4J_PASSWORD = os.environ.get('NEO4J_PASSWORD', 'supersecurepassword')

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

INSTANCE_ID = os.environ.get('HOSTNAME', socket.gethostname())

@app.route("/", methods=["GET"])
def root():
    """Endpoint básico para pruebas de Traefik"""
    return jsonify({
        "message": "Flask API is running",
        "service": "flask-api",
        "instance_id": INSTANCE_ID,
        "hostname": socket.gethostname(),
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route("/legendario", methods=["GET"])
def legendario():
    """Endpoint legendario para pruebas de enrutado específico"""
    log_message = f"LEGENDARIO REQUEST - Instance: {INSTANCE_ID} | Timestamp: {datetime.now().isoformat()}"
    logger.info(log_message)
    print(f"{log_message}")
    
    return jsonify({
        "message": "¡Endpoint Legendario!",
        "instance_id": INSTANCE_ID,
        "hostname": socket.gethostname(),
        "type": "LEGENDARIO",
        "timestamp": datetime.now().isoformat()
    }), 200


    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)