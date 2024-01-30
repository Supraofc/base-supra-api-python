import requests

def youtube(quero):
    url = f'https://magneum.vercel.app/api/youtube_sr?q={quero}'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        result = data.get('youtube_search', [])

        if not result:
            raise Exception("Nenhum resultado encontrado")

        video_info = result[0]

        idvideo = video_info.get('YT_ID', '')
        titulo = video_info.get('TITLE', '')
        postado = video_info.get('UPLOADED', '')
        views = video_info.get('VIEWS', '')
        duracao = video_info.get('DURATION_FULL', '')
        canal = video_info.get('AUTHOR_NAME', '')
        linkcanal = video_info.get('AUTHOR_CHANNEL', '')
        linkvideo = video_info.get('LINK', '')
        img = video_info.get('THUMB', '')
        descricao = video_info.get('DESCRIPTION', '')

        resultado = {
            'criador': '@SupraOfc',
            'idvideo': idvideo,
            'titulo': titulo,
            'postado': postado,
            'views': views,
            'duracao': duracao,
            'canal': canal,
            'linkcanal': linkcanal,
            'linkvideo': linkvideo,
            'img': img,
            'descricao': descricao
        }

        return resultado

    except Exception as e:
        raise Exception(f"Erro ao obter dados do YouTube: {str(e)}")
