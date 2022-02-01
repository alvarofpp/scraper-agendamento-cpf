from bs4 import BeautifulSoup
import requests


class Extract:
    @staticmethod
    def get_trs():
        url = 'https://www3.itep.rn.gov.br/agendamento/Agendamento'
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.find_all('tr', {
            'class': 'table-row',
        })
