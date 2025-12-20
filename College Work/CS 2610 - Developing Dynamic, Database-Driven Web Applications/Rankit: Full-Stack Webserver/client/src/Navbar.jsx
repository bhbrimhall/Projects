import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react';
import "./css/navbar.css"
import { useApi } from './utils/api';

export function Navbar({user, profile, errorMessage="", setErrorMessage}){

    const api = useApi();
    const [searching, setSearching] = useState(false);
    const [searchValue, setSearchValue] = useState("");
    const [searchLists, setSearchLists] = useState([]);
    const [searchProfiles, setSearchProfiles] = useState([]);


    function setUserLinks(){
        // If user is logged in, display these nav items. Otherwise, display the other ones
        if (user){
            return (
                <>
                    <div className='spacer'></div>
                    <Link className='profile-nav-item' to={`/view_profile/${profile.id}`}>
                        <div className='profile-link-content'>
                            <div className='profile-image'>
                                <img src={`/get_image/${profile.image}/`} className='image-el'/>
                            </div>
                            <div>{profile.username}</div> 
                        </div>
                    </Link>
                    <Link to="/my_lists" className='nav-item'>
                        <div className='nav-item-content'>My Lists</div>
                    </Link>
                    <div onClick={logout} className='nav-item'>
                        <div className='nav-item-content'>Log Out</div>
                    </div>
                </>
                    
                        
            )
        }else{
            return (
                <>
                    <div className='spacer'></div>
                    <a href="/registration/sign_in/" className='nav-item'>
                        <div className='nav-item-content'>Sign In</div>
                    </a>
                    <a href="/registration/sign_up/" className='nav-item'>
                        <div className='nav-item-content'>Make Account</div>
                    </a>
                </>
            )
        }
    }

    async function logout(e) {
        const res = await api.get("registration/logout/")
    
        if (res.success) {
            window.location = "/";

        } else {
            setErrorMessage("There was an issue with logging out of your account...")
        }
    }

    function listSearchHTML(list){
        return(
            <Link key={list.id} className='search-list' to={`/view_list/${list.id}/`}  onClick={() => setSearching(false)}>
                <div className='search-image'>
                    <img src={`get_image/${list.thumbnail}/`} className='image-el' />         
                </div>
                <div className='search-name'>
                    <div>{list.name}</div>
                    <div>{list.type === "raw" ? "Raw list" : "Tier list"}</div>
                </div>
            </Link>
        )
    }

    function profileSearchHTML(profile){
        return(
            <Link key={profile.id} className='search-list' to={`/view_profile/${profile.id}/`} onClick={() => setSearching(false)}>
                <div className='search-image'>
                    <img src={`get_image/${profile.image}/`} className='image-el' />         
                </div>
                <div className='search-name'>
                    <div>{profile.username}</div>
                    <div>Profile</div>
                </div>
            </Link>
        )
    }

    function search(){
        return(
            <>
                <div className='blackout'>
                    <div className='searchbox-container'>
                        <div className='search-input'>
                            <input type="text" 
                            value={searchValue} 
                            onChange={(e) => setSearchValue(e.target.value)}
                            placeholder='Search...'
                            />
                        </div>
                        <div className='search-results-container'>
                            <h2>Results:</h2>
                            <div className='search-results'>
                                {searchLists && searchLists.map((list) => listSearchHTML(list))}
                                {searchProfiles && searchProfiles.map((profile) => profileSearchHTML(profile))}
                            </div>
                        </div>
                    </div>
                </div>
            </>
        )
    }

    useEffect(() => {
        async function getSearch(){
            if (searchValue){
                const res = await api.post("search/", {searchValue});
                if (res.success){
                    setSearchLists(res.lists)
                    setSearchProfiles(res.profiles)
                } else{
                    setErrorMessage("There was an issue when performing the search...")
                }
            }
        }
        getSearch()
    }, [searchValue])

    return(
        <>
            <nav className='navbar-container'>
                <div className='navbar'>
                    {setUserLinks()}   
                </div>                
                             
            </nav>

            <div className='searchbar-container'>
                <div className='searchbar-box-1'>
                    <Link to="/" className='home-link'>
                        <div className='home-link-content'>Rankit</div>
                    </Link>
                </div>
                
                <div className='searchbar-box-2' onClick={() => setSearching(!searching)}>
                    <div className='searchbar'>
                        Search Profiles and Lists
                    </div>
                </div>
                
                <div className='searchbar-box-3'>
                    <div>
                        {errorMessage}
                    </div>
                </div>
                
            </div>

            {searching && search()}          
        </>
    )
}