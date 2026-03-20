pip install --index-url http://packages.webflare.ru:8888/simple --trusted-host packages.webflare.ru pyjwt

GET /api/v1/servers - получение списка серверов
params {
	
	offset = 0
	limit = 100
	status = Active
	type = All
	
	
	
}

GET /api/v1/servers/{id} - детальная информация

POST /api/v1/servers - добавление сервера (для админов, creater)


PUT /api/v1/servers/{id} - обновление информации


Сервер

server_id - уникальный идентификатор сервера

img_url - фото сервера (необезятельное)

name - название сервера

domain - доменное имя для подключения

ip_address - IP-адрес сервера

port - порт для подключения (по умолчанию 25565)

version - версия Minecraft

max_players - максимальное количество игроков

online_players - текущее количество игроков

status - статус сервера (онлайн/оффлайн)

type - тип сервера (выживание, PvP, мини-игры, RPG)


Пользователь

username

password

email 

role (Admin, User, Creater)
