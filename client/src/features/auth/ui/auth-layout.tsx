import { Outlet } from "react-router"

function AuthLayout() {
  return (
    <div className="auth">
      <Outlet />
    </div>
  )
}

export default AuthLayout