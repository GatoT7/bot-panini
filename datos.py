import requests
from bs4 import BeautifulSoup

import threading
import time




"***BOT DE TELEGRAM***"

def telegram_bot_sendtext(bot_message):
    
    bot_token = '5565581494:AAGd0_O2Oi7gSvMBT34vrxrsHNQWhDLyMGA'
    bot_chatID = '1938680709'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    


def flow():
    "***WEB SCRAPING***"

    url = 'https://www.zonakids.com/productos/pack-x-25-sobres-de-figuritas-fifa-world-cup-qatar-2022/'
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, 'html.parser')

    input_tag = soup.find(attrs={
        "class": "btn btn-primary full-width js-prod-submit-form js-addtocart nostock m-bottom-half"
        })
    output = input_tag['value']
    
    while output == 'Sin stock':
        
        
        print('No hay figus :(')
        
        if output != 'Sin stock': 
            print('HAY FIGUS!!!!')
            telegram_bot_sendtext("HAY CROMOS !!! \nREVIVIO EL ESFERICO !!! HAY QUE SALTAR HAY QUE SALTAR, EL QUE NO SALTA NO VA A QATAR\nEnlace: https://www.zonakids.com/productos/pack-x-25-sobres-de-figuritas-fifa-world-cup-qatar-2022/ ")
            break
        time.sleep(180)
        
            

class Timer(threading.Thread):
    def __init__(self):
        self._timer_runs = threading.Event()
        self._timer_runs.set()
        super().__init__()
    def run(self):
        while self._timer_runs.is_set():
            self.timer()
            time.sleep(self.__class__.interval) 
    def stop(self):
        self._timer_runs.clear()

class HayFigusTimer(Timer):
    interval = 180   # Intervalo en segundos.
    # Función a ejecutar.
    def timer(self):
        flow()


if __name__ == "__main__":
    """
    while True:
        HayFigusTimer().start()
        if flow() == False:
            break
    """
    flow()
    