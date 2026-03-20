export type UserRole = 'Admin' | 'Creater' | 'User'

export type UserType = {
    id: number | string,
    username: string,
    email: string,
    role: UserRole,
    displayName?: string,
}


export type UserAuthType = Pick<UserType, 'email' | 'username' | 'displayName'> & { password: string }

export type AuthType = Omit<UserType, 'username' | 'id' | 'role'> & { password: string }

export type AuthServerType = {
    accessToken: string,
    user: UserType,
}
