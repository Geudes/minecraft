import { createBrowserRouter } from "react-router";
import Layout from "../layout/layout";

export const router = createBrowserRouter([
    {
        path: '/',
        element: <Layout />
    }
])