import { useNavigate} from 'react-router-dom'
import { useState } from 'react';
import { Navbar } from './Navbar';
import { useUser } from './utils/use_user';
import { useApi } from './utils/api';
import "./css/create_list.css"

export function CreateList(){

    const [user, userProfile] = useUser("require");
    const [title, setTitle] = useState("");
    const [listType, setListType] = useState(null);
    const api = useApi();
    const navigate = useNavigate();
    const [errorMessage, setErrorMessage] = useState("");
 
    // returns true if the user has chosen a title and type
    function validNewList(){
        return title !== "" && (listType === "tier" || listType === "raw");
    }

    // creates the list in database and redirects to the edit page
    async function createList(){
        const res = await api.post("create_list/", {title, listType});
        if (res.success){
            navigate(`/edit_list/${res.id}/`)
        } else{
            console.log("ERROR")
            setErrorMessage("Unable to create list...")
        }
    }

    return(
        <>         
            <Navbar  user={user} profile={userProfile} errorMessage={errorMessage} setErrorMessage={setErrorMessage}/>
            <div className="main-container">   
                <div className='set-list-title'>
                    <input type="text" 
                    value={title} 
                    onChange={e => setTitle(e.target.value)} 
                    placeholder='List Title' 
                    className='set-list-title-input'/>
                </div>
                <div className='set-list-type-container'>
                    <div className='set-list-type tier' data-list-type={listType} onClick={() => setListType("tier")}>
                        <div className='set-list-type-image'>
                            <img src="get_image/tier/" className='image-el' />
                        </div>
                        <div className='set-list-type-name' >
                            Tier List
                        </div>
                    </div>
                    <div className='set-list-type raw' data-list-type={listType} onClick={() => setListType("raw")}>
                        <div className='set-list-type-image'>
                            <img src="get_image/raw/" className='image-el' />
                        </div>
                        <div className='set-list-type-name'>
                            Raw List
                        </div>
                    </div>
                </div>
            
                <div className='create-list' onClick={createList} data-show={validNewList()}>
                    <div>Create List</div>
                </div>
                
            </div>
        </>
    )
}