from flask import Flask, render_template, request, jsonify, Response
from importlib.machinery import SourceFileLoader
from flask import Blueprint
import requests
import random

listkey = ["supra", "supraz"]


pesquisas_coisas = SourceFileLoader("pesquisas_coisas", "./scrapper/pesquisas.py").load_module()
videos_meme = SourceFileLoader("videos_meme", "./scrapper/videos.py").load_module()
youtube = pesquisas_coisas.youtube
meme = videos_meme.videos_meme

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/api/pesquisas')
def pesquisas():
    return render_template('pesquisas.html')

@main_bp.route('/api/videos')
def videos():
    return render_template('videos.html')


@main_bp.route('/api/videos/videosmeme', methods=['GET'])
def videos_meme_route():
    apikey = request.args.get('apikey')
    if not apikey:
        return jsonify({"erro": "apikey não fornecida"}), 400
    if apikey not in listkey:
            return render_template('chaveApi.html')
    try:
        resultado = meme() 
        video = random.choice(resultado)
        def generate():
            response = requests.get(video['video'], stream=True)
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=8192):
                yield chunk
        return Response(generate(), mimetype='video/mp4', status=200)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@main_bp.route('/api/pesquisas/youtube', methods=['GET'])
def youtube_route():
    quero = request.args.get('quero')
    apikey = request.args.get('apikey')
    if not apikey:
        return jsonify({"erro": "apikey não fornecida"}), 400
    if apikey not in listkey:
        return render_template('chaveApi.html')
    try:
        result = youtube(quero)
        return jsonify(result)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    

def setup_routes(app):

    app.register_blueprint(main_bp)

   
