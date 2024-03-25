#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:03:54 2024

@author: kabur
"""

# app.py
from routes.joueur_routes import joueur_bp
from routes.tournoi_routes import tournoi_bp
from routes.equipe_routes import equipe_bp
from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='MonProjetFlask/static')

# Tes blueprints ici
app.register_blueprint(joueur_bp, url_prefix='/api/joueur')
app.register_blueprint(tournoi_bp, url_prefix='/api/tournoi')
app.register_blueprint(equipe_bp, url_prefix='/api/equipe')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        
        return send_from_directory(app.static_folder, path)
    else:
        
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)