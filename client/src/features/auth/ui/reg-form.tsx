import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { registerSchema } from "../models/auth-schemes"

function RegisterForm() {

  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    resolver: zodResolver(registerSchema)
  })

  return (
    <form className="auth-form">

    </form>
  )
}

export default RegisterForm