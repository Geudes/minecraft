export type serversDataType = {
    server_id: number | string,
    image_url: string | null,
    name: string,
    domain: string,
    ip_adress: string,
    port: string,
    version: string,
    max_player: number | string,
    online_players: number | string,
    status: 'online' | 'offline',
    type: 'выживание' | 'PvP' | 'мини-игры' | 'RPG'
}