import requests

class CallMeBot:

    def __init__(self):
        self.__base_url = 'https://api.callmebot.com/whatsapp.php'
        self.__api_key = '7188637'

    def send_message(self, message):
        response = requests.get(
            url=f'{self.__base_url}?phone=+5581979007007&text={message}&apikey={self.__api_key}'
        )

        return response.text
    