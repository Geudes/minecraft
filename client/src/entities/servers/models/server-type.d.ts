export interface IServer{
    server_id:string;
    name:string;
    domain:string;
    ip_address:string;
    version:string;
    max_players:number;
    online_players:number;
    status:'online' | 'offline';
    type:'survial' | 'pvp' | 'minigames'  | 'rpg';
    port?:number;
    img_url:string;
 }

 export type CreateServer = Omit<IServer, 'serverId' | 'online_players'>;
 export type UpdateServer = Partial<CreateServer >