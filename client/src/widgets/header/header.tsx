import { NavLink } from 'react-router'

function Header() {
  return (
    <>
        <nav>
            <NavLink to={'/'} style={({ isActive }) => ({ backgroundColor: isActive ? '#e6e6e6ea' : '' })}>Сервера</NavLink>
            <NavLink to={'/auth'} style={({ isActive }) => ({ backgroundColor: isActive ? '#e6e6e6ea' : '' })}>Auth</NavLink>
            <NavLink to={'/register'} style={({ isActive }) => ({ backgroundColor: isActive ? '#e6e6e6ea' : '' })}>Regsiter</NavLink>
        </nav>
    </>
  )
}

export default Header