
import axiosInstance from "../../../shared/lib/api/axios-instance";
import type { AuthServerType, UserAuthType } from "../types";

class AuthApi{
static async auth(form:UserAuthType):Promise<AuthServerType>{
    const {data} = await axiosInstance.post<AuthServerType>('/auth/login', form)
    return data
} 
static async register(form:UserAuthType):Promise<AuthServerType>{
    const {data} = await axiosInstance.post<AuthServerType>('/auth/register' , form)
    return data
}
static async logout():Promise<void>{
    await axiosInstance.post('/auth/logout')
}
}
export default AuthApi