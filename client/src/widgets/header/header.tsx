import { NavLink } from 'react-router'

import './header.css'

function Header() {
    return (
        <>
            <header className="header">
                <nav className='header__nav nav'>
                    <NavLink to={'/'} className={({ isActive }) => isActive ? 'nav__item' : 'nav__item item--active'}>Сервера</NavLink>
                    <NavLink to={'/auth/login'} className={({ isActive }) => isActive ? 'nav__item' : 'nav__item item--active'}>Авторизация</NavLink>
                    <NavLink to={'/auth/register'} className={({ isActive }) => isActive ? 'nav__item' : 'nav__item item--active'}>Регистрация</NavLink>
                </nav>
            </header>
        </>
    )
}

export default Header