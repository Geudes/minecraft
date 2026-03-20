import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { registerSchema } from "../../models/auth-schemes"

import './forms.css'

function RegisterForm() {

  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    resolver: zodResolver(registerSchema)
  })

  return (
    <form onSubmit={handleSubmit} className="auth-form">
      <div className="auth-form__field field">
        <label htmlFor="username">Имя пользователя</label>
        <input type="text" {...register('username')}/>
        {errors.username && (<span className="field__error error">{errors.username.message}</span>)}
      </div>
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