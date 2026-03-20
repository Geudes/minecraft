

import axiosInstance from '../../../shared/lib/api/axios-instance'
import type { CreateServer, IServer, UpdateServer } from '../models/server-type'

class ServerApi{
static async getAll():Promise<IServer[]>{ 
    const {data} = await axiosInstance.get<IServer[]>('/servers')
    return data
}
static async getOne(id: string | number):Promise<IServer>{
    const {data} = await axiosInstance.get(`/servers/${id}`)
    return data
}
static async create(form:CreateServer):Promise<IServer>{
    const {data} = await axiosInstance.post(`/servers`, form)
    return data
}
static async update(id:string | number , form:UpdateServer):Promise<IServer>{
    const {data} = await axiosInstance.put(`/servers/${id}`, form)
    return data
}
}
export default ServerApi