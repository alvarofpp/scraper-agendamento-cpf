from typing import List


class Transform:
    @staticmethod
    def convert_tr_to_row(now, tr) -> List:
        tds = tr.find_all('td')
        return [
            now.strftime('%Y-%m-%d'),
            now.strftime('%H:%M'),
            tr['id'],
            tds[0].text,
            tds[1].text.replace('\r\n', ' '),
            '1' if tds[2].text == 'há vagas disponíveis' else '0',
        ]
