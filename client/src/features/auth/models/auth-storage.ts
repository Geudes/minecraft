import type { UserType } from "../types";

export const authStorage = {
    getAccess: (): string | null => localStorage.getItem('accessToken'),
    setAccess: (token: string): void => localStorage.setItem('accessToken', token),
    getRefresh: (): string | null => localStorage.getItem('refreshToken'),
    setRefresh: (token: string): void => localStorage.setItem('refreshToken', token),
    getUser: (): UserType | null => {
        const user = localStorage.getItem('user')
        if(user) {
            return JSON.parse(user)
        }

        return null
    },
    setUser: (user: UserType | undefined): void => {
        if(user) {
            localStorage.setItem('user', JSON.stringify(user))
        }
    },
    clear: (): void => {
        localStorage.removeItem('accessToken')
        localStorage.removeItem('accessToken')
        localStorage.removeItem('accessToken')
    }
}