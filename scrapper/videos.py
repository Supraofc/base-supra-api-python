import requests
from bs4 import BeautifulSoup
import random

def videos_meme():
    try:
        rads = random.randint(1, 52)
        response = requests.get(f'https://melhoresmemes.com/videos?page={rads}')
        response.raise_for_status()

        resposta = []
        soup = BeautifulSoup(response.text, 'html.parser')
        for supra in soup.select('div > div > div > div.col-6'):
            url = supra.find('a')['href']
            datas = requests.get(url)
            datas.raise_for_status()
            
            soup_datas = BeautifulSoup(datas.text, 'html.parser')
            video = soup_datas.select_one('video > source')['src']

            resultado = {
                'video': video
            }
            resposta.append(resultado)

        return resposta

    except Exception as e:
        print(f"Erro: {e}")
        return []


