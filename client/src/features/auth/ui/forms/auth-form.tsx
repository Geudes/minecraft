import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { authSchema } from "../../models/auth-schemes"

import './forms.css'
import { useAuth } from "../mutation/use-auth"
import type { AuthType } from "../../types"

function RegisterForm() {
 const { auth: authMutation } = useAuth()
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    resolver: zodResolver(authSchema)
  })
  const onAuth = (form:AuthType) => {
    authMutation.mutate(form)
  }
  return (
    <form onSubmit={handleSubmit(onAuth)} className="auth-form">
      <div className="auth-form__field field">
        <label htmlFor="email">Электронная почта</label>
        <input type="text" id="email" {...register('email')}/>
        {errors.email && (<span className="field__error error">{errors.email.message}</span>)}
      </div>
      <div className="auth-form__field field">
        <label htmlFor="username">Пароль</label>
        <input type="password" {...register('password')}/>
        {errors.password && (<span className="field__error error">{errors.password.message}</span>)}
      </div>
      <button type="submit">Регистрация</button>
    </form>
  )
}

export default RegisterForm