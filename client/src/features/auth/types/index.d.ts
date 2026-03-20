export type UserRole = 'Admin' | 'Creater' | 'User'

export type UserType = {
    username: string,
    role: UserRole,
    email: string,
    id: number | string,
}

export type UserAuthType = Pick<UserType, 'email' | 'username' | 'dispayName'> & { password: string }

export type AuthServerType = {
    accessToken: string,
    user: UserType,
}