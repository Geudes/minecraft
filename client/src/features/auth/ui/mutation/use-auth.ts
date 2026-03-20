import { useMutation, useQueryClient } from "@tanstack/react-query"
import { useNavigate } from "react-router"
import type { AuthType, UserAuthType } from "../../types";
import AuthApi from "../../api/auth-api";
import { authStorage } from "../../models/auth-storage";

export const useAuth = () => {
    const navigate = useNavigate();
    const queryClient = useQueryClient();

    const auth = useMutation({
        mutationFn:(form:AuthType) => AuthApi.auth(form),
        onSuccess:(data) => {
            authStorage.setAccess(data?.accessToken)
            authStorage.setUser(data?.user)
            queryClient.invalidateQueries({queryKey:['user']})
            navigate('/')
        },
    })
    const register = useMutation({
        mutationFn:(form:UserAuthType) => AuthApi.register(form),
        onSuccess:() => {
            navigate('/auth/login')
        }
    })
    const logout = useMutation({
        mutationFn:() => AuthApi.logout(),
        onSuccess:() => {
            authStorage.clear()
            queryClient.clear()
            navigate('/auth/login')
        }
    })
    return {logout , register , auth}
}