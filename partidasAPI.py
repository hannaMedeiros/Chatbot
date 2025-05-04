import requests

def buscar_partidas():
    api_key = 'keQQITksWsFOiVjqdZ4070-8m_HbqRjDYPPxke9rwXzE0glfWRY'
    url =  'https://api.pandascore.co/csgo/matches/upcoming'

    params = {
    'token': api_key,
    'per_page': 5  
    }

    response = requests.get(url, params=params)
    print(response.text)

    if response.status_code == 200:
        partidas = response.json()
        if not partidas:
            return "Nenhuma partida futura encontrada no momento."

        mensagem = "*Próximas partidas de CS:GO:*\n\n"
        for partida in partidas:
            try:
                time1 = partida['opponents'][0]['opponent']['name'] if len(partida['opponents']) > 0 else 'TBD'
                time2 = partida['opponents'][1]['opponent']['name'] if len(partida['opponents']) > 1 else 'TBD'
                horario = partida['begin_at'] or 'Horário indefinido'
                mensagem += f"🏆 *{time1}* vs *{time2}*\n🕒 {horario}\n\n"
            except Exception as e:
                mensagem += f"Erro ao processar uma partida: {str(e)}\n\n"
        return mensagem
    else:
        return f"Erro ao buscar partidas: {response.status_code} - {response.text}"