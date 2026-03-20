export type UserType = {
    username: string,
    dispayName: string,
    email: string,
    id: number | string,
}

export type UserAuthType = Pick<UserType, 'email' | 'username' | 'dispayName'> & { password: string }

export type AuthServerType = {
    accessToken: string,
    user: UserType,
}