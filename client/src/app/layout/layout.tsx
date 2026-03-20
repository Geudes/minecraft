import { Outlet } from "react-router"
import Header from "../../widgets/header/header"

import './layout.css'

function Layout() {
  return (
    <div className="app container">
      <Header />
      <main className="app__main main">
        <Outlet />
      </main>
    </div>
  )
}

export default Layout