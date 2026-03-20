import { createBrowserRouter } from "react-router";
import Layout from "../layout/layout";
import AuthPage from "../../pages/auth/AuthPage";
import RegisterPage from "../../pages/auth/RegisterPage";
import ServresPage from "../../pages/Servers/ServersPage";

export const router = createBrowserRouter([
    {
        path: '/',
        element: <Layout />,
        children: [
            {
                path: '/',
                element: <ServresPage />
            },
            {
                path: '/auth',
                element: <AuthPage />
            },
            {
                path: '/register',
                element: <RegisterPage />
            },
        ]
    }
])

export default router