import * as z from 'zod'

export const registerSchema = z
.object({
    username: z.string().min(2, 'Это поле должно содержать более 2 символов'),
    email: z.email('Некорректный адрес'),
    password: z.string().min(2, 'Это поле должно содержать более 2 символов'),
})

export const authSchema = z
.object({
    email: z.email('Некорректный адрес'),
    password: z.string().min(2, 'Это поле должно содержать более 2 символов'),
})