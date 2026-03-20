import axios from "axios";
import { authStorage } from "../../../features/auth/models/auth-storage";

const baseURL: string = import.meta.env.VITE_BACK_URL

const axiosInstance = axios.create({
    baseURL,
    headers: {
        'Content-Type': 'application'
    }
})


axiosInstance.interceptors.request.use(
    (config) => {
        const accessToken = authStorage.getAccess()
        if(accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`
        }

        return config
    }, (error) => Promise.reject(error)
)

export default axiosInstance