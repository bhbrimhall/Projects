import React from 'react'
import ReactDOM from 'react-dom/client'
import { Homepage } from './Homepage.jsx'
import {createHashRouter, RouterProvider} from 'react-router-dom'
import { MyLists } from './MyLists.jsx'
import "./css/main.css"
import { CreateList } from './CreateList.jsx'
import { EditItems } from './EditItems.jsx'
import { ViewList } from './ViewList.jsx'
import { ViewProfile } from './ViewProfile.jsx'

// navbar is parent element because all pages have it
const router = createHashRouter([
        {
            path: "/",
            element: <Homepage />
        },
        {
            path: "/my_lists",
            element: <MyLists />,
        },
        {
            path: "/view_profile/:id",
            element: <ViewProfile />
        },
        {
            path: "/my_lists/create_new",
            element: <CreateList />
        },
        {
            path: "/edit_list/:id",
            element: <EditItems />
        },
        {
            path: "/view_list/:id",
            element: <ViewList/>
        }
    

])


ReactDOM.createRoot(document.getElementById('root')).render(
    <RouterProvider router={router} />
);
