import { createBrowserRouter } from "react-router";
import Layout from "../layout/layout";
import ServresPage from "../../pages/Servers/ServersPage";
import AuthLayout from "../../features/auth/ui/auth-layout";
import AuthPage from "../../pages/auth/auth-page";
import RegisterPage from "../../pages/auth/register-page";

export const router = createBrowserRouter([
    {
        path: '/',
        element: <Layout />,
        children: [
            {
                index: true,
                element: <ServresPage />
            },
            {
                path: 'auth',
                element: <AuthLayout />,
                children: [
                    {
                        path: 'login',
                        element: <AuthPage />
                    },
                    {
                        path: 'register',
                        element: <RegisterPage />
                    }
                ]
            }
        ]
    }
])

export default router