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
    status: string,
    type: string
}

export type userType = { 
    username: string,
    email: string,
    role: 'Admin' | 'User' | 'Creater'
}

export type registerType = { passsowrd: string } & userType