import sqlite3

conn = sqlite3.connect('cs_chatbot.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS faq_cs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pergunta TEXT NOT NULL,
    resposta TEXT NOT NULL
)
''')

faq_data = [
    ('qual arma é boa no cs?', '🔫 A AWP é ótima se você tiver boa mira, mas a AK-47 é muito versátil e mata com um tiro na cabeça!'),
    ('como eu melhoro minha mira?', '🎯 Treine bastante em mapas como Aim Botz ou aim_training. A prática leva à perfeição!'),
    ('o que é um round eco?', '💸 É quando seu time economiza grana pra comprar melhor depois. Geralmente usam pistolas e granadas baratas.'),
    ('pra que serve o colete?', '🛡️ O colete (armor) ajuda a reduzir o dano dos tiros. É essencial pra sobreviver mais nos rounds.'),
    ('o que é clutch?', '🔥 É quando você está sozinho contra vários inimigos e ainda consegue ganhar o round! Jogada de herói.'),
    ('como eu subo de patente?', '📈 Jogando partidas ranqueadas, vencendo com bom desempenho e espírito de equipe.'),
    ('quais mapas tão no competitivo?', '🗺️ Os mapas do competitivo são: Mirage, Inferno, Nuke, Ancient, Anubis, Vertigo e Overpass.'),
    ('qual a função do IGL?', '🧠 O IGL (In-Game Leader) é o "cérebro" do time, que chama as táticas e coordena as jogadas.'),

    ('quem é a furia?', '🐆 A FURIA é uma organização brasileira de eSports com presença global, famosa no CS:GO e outros jogos.'),
    ('quais jogadores da furia no cs?', '🎮 A line atual tem KSCERATO, yuurih, arT, saffee e chelo. Um time cheio de talento!'),
    ('como a furia joga?', '⚡ Eles jogam de forma agressiva e imprevisível. O arT adora surpreender com rushs ousados!'),
    ('quem é o coach da furia?', '👨‍🏫 O coach é o guerri, figura chave nas estratégias e na motivação da equipe.'),
    ('a furia ganhou algum major?', '🏆 Ainda não conquistou um Major, mas já teve ótimas campanhas e vitórias em campeonatos grandes.'),
    ('onde fica a furia?', '🌎 A FURIA tem bases no Brasil e nos EUA. Eles treinam nos dois países!'),
    ('como assistir aos jogos da furia?', '📺 Assista no canal do Gaules, Twitch da ESL, ou nas redes da própria FURIA.'),
    ('quais conquistas da furia?', '🥇 Já ganharam ESL Pro League Americas, DreamHack Open e chegaram longe em Majors.'),
    ('quando nasceu a furia?', '📅 A FURIA foi fundada em 2017 por Jaime Pádua e André Akkari.'),
    ('quem são os fundadores da furia?', '🤝 André Akkari (jogador de pôquer) e Jaime Pádua fundaram a FURIA com uma visão ousada de eSports.'),

    
    ('tem loja da furia?', '🛍️ Sim! Dá uma olhada em store.furia.gg e garante seu manto oficial.'),
    ('como entrar pra furia?', '🚀 Se destaque em campeonatos, jogue bem e fique ligado nas peneiras e oportunidades que eles divulgam.'),
    ('o que significa furia?', '💥 Representa intensidade, agressividade e paixão — a alma da organização!'),


]


cursor.executemany('INSERT INTO faq_cs (pergunta, resposta) VALUES (?, ?)', faq_data)
conn.commit()
conn.close()

