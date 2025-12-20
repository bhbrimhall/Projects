import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react';
import { useUser } from './utils/use_user';
import "./css/my_lists.css"
import { useApi } from './utils/api';
import { Navbar } from './Navbar.jsx'

export function MyLists(){

    const [user, userProfile] = useUser("require");
    const api = useApi();
    const [myLists, setMyLists] = useState([]);
    const [errorMessage, setErrorMessage] = useState("");
    
    // get users lists from database to display
    useEffect(() => {
        async function previewMyLists(){
            const res = await api.get("my_lists/");
            if (res.success){
                setMyLists(res.lists);
            } else {
                setErrorMessage("There was an issue when trying to retrieve your lists...")
            }
        }

        previewMyLists();
    }, []);

    function listHTML(list){
        return (
        <div key={list.id} className='list-display'>
            <div className='list-image'>
                <img src={`/get_image/${list.thumbnail}/`} className='image-el' />
            </div>
            <div className='list-properties'>
                <div className='list-properties-words'>
                    <h2 className='list-name'>{list.name}</h2> 
                    <div className='list-type'>{list.type === "raw" ? "Raw list" : "Tier list"}</div>
                </div>
                <div className='my-list-buttons'>
                    <Link to={`/view_list/${list.id}/`} className='my-list-btn'>View</Link>
                    <Link to={`/edit_list/${list.id}/`} className='my-list-btn'>Edit</Link>
                </div>
            </div>
        </div>
        )        
    }

    return(
        <>
            <Navbar  user={user} profile={userProfile} errorMessage={errorMessage} setErrorMessage={setErrorMessage}/>
            <div className="main-container">
                <div className='my-lists-container'>
                    <div className='my-lists'>
                        <div className='my-lists-actions'>
                            <Link className="my-lists-create" to="/my_lists/create_new">
                                New List
                            </Link>
                        </div>
                        <div className='my-lists-lists'>
                            {myLists.map(list => listHTML(list))}
                        </div>
                    </div>
                    
                </div>
            </div>
        </>
    )
}