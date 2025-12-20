import { Link, useParams, } from 'react-router-dom'
import { useEffect, useState } from 'react';
import { useUser } from './utils/use_user';
import "./css/view_profile.css"
import { useApi } from './utils/api';
import { Navbar } from './Navbar.jsx'

export function ViewProfile(){

    const {id} = useParams();
    const api = useApi()
    const [user, userProfile, setUserProfile] = useUser("nav");
    const [profile, setProfile] = useState({
        image: "profile",
        username: "Loading...",
        about: "Loading..."});
    const [profileLists, setProfileLists] = useState();
    const [editingProfile, setEditingProfile] = useState(false)
    const [imagePopup, setImagePopup] = useState(false);
    const [updateMyImages, setUpdateMyImages] = useState(true); // broadcast
    const [imageHTML, setImageHTML] = useState([]);
    const [errorMessage, setErrorMessage] = useState("")


    function listHTML(list){
        return (
        <div key={list.id} className='list-display'>
            <div className='list-image'>
                <img src={`/get_image/${list.thumbnail}/`} className='image-el' />
            </div>
            <div className='list-properties'>
                <div>
                    <h2 className='list-name'>{list.name}</h2> 
                    <div className='list-type'>{list.type === "raw" ? "Raw list" : "Tier list"}</div>
                </div>
                <div className='my-list-buttons'>
                    <Link to={`/view_list/${list.id}/`} className='my-list-btn'>View</Link>
                </div>
            </div>
        </div>
        )        
    }

    function profileEditPopupHTML(){
        return(
            <>
                <div className='blackout'>
                    <div className='popup-container'>
                        {imagePopup && 
                        <div className='popup-images-container'>
                            <div className='popup-images'>
                                <label>
                                    <span>Upload:</span>
                                    <input type="file" className='upload-img-button' onChange={selectNewImage}/>
                                </label>
                                <div className='user-images'>
                                    {imageHTML}
                                </div>
                            </div>
                        </div>
                        }

                        <div className='popup-edit-l'>
                            <h1 className='popup-header'>Edit Profile</h1>
                            <div className='popup-specs'>
                                <div className='edit-list-image'>
                                    <img src={`/get_image/${profile.image}/`} className='image-el' onClick={() => setImagePopup(!imagePopup)} />
                                </div>
                                <div className='edit-list-inputs'>
                                    <label>
                                        About:
                                        <input type="text" value={profile.about} onChange={(e) => setProfile({...profile, about: e.target.value})}/>
                                    </label>
                                    <div className='edit-list-submit' onClick={saveProfileChanges}>
                                        <div>Save Changes</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </>)

    }

    // saves the list changes
    async function saveProfileChanges(){
    
        const res = await api.post("configure_profile/", profile);
        if (!res.success){
            setErrorMessage("There was an issue when trying to save your changes...")
        }
        setEditingProfile(false);
        setUserProfile(profile)
        setImagePopup(false);
    }

    // creates new image
    async function selectNewImage(e){
    
        const res = await api.postImage(e.target.files[0]);
        if (!res.success){
            setErrorMessage("There was an issue when uploading your image...")
        }
        // this pretty much triggers the use effect that gets the users images
        setUpdateMyImages(!updateMyImages)
        
    }

    //get the profile and lists
    useEffect(() => {
        async function getProfile(){
            const res = await api.get(`get_profile/${id}/`)
            if (res.success){
                setProfile(res.profile)
                setProfileLists(res.lists)
            }else{
                setErrorMessage("There was an issue when trying to retrieve the profile and lists...")
            }
        }
        getProfile()
    }, [])

    // get images when the user logged in owns the list
    useEffect(() => {
        if (userProfile && profile && userProfile.id === profile.id){

            async function getImages(){
                const res = await api.get('my_images/');
                if (res.success){
                    let new_image_HTML = []

                    new_image_HTML.push(
                        <div key={-1} className='user-image-container'>
                                <div className='user-image' onClick={() => setProfile({...profile, image: "profile"})}>
                                    <img src={`/get_image/profile/`} className='image-el'/>
                                </div>
                                <div className='no-image-desc-box'>
                                    <div className='no-image-desc'>Default</div>
                                </div>
                            </div>
                        )
                    for(const image of res.images){
                        // add the html to the list
                        new_image_HTML.push(
                            <div key={image.id} className='user-image-container'>
                                <div className='user-image' onClick={() => setProfile({...profile, image: `${image.id}`})}>
                                    <img src={`/get_image/${image.id}/`} className='image-el'/>
                                </div>
                                <div className='user-image-delete-button' onClick={() => deleteImage(image.id)}>
                                    <div className='material-icons'>delete_forever</div>
                                </div>
                            </div>
                            )
                    }

                    setImageHTML(new_image_HTML)

                } else {
                    setErrorMessage("There was an issue when trying to retrieve your images...")
                }
            }
            getImages()
        }
    }, [userProfile, profile, updateMyImages])

    return(
        <>
            <Navbar user={user} profile={userProfile} errorMessage={errorMessage} setErrorMessage={setErrorMessage}/>
            <div className="main-container">
                <div className='profile'>
                    <div className='profile-view'>
                        <div className='profile-view-image'>
                            <img src={`get_image/${profile.image}/`} className='image-el'/>
                        </div>
                        <div className='profile-view-attributes'>
                            <div className='profile-name'>{profile.username}</div>
                            <div className='profile-about'>{profile.about}</div>
                        </div>

                        {userProfile && profile && userProfile.id === profile.id &&
                        <div className='profile-edit-button' onClick={() => setEditingProfile(true)}>
                            Edit Profile
                        </div>}
                    </div>
                    <div className='profile-lists-container'>
                        <h2 className='profile-lists-header'>{profile.username}'s lists:</h2>
                        <div className='profile-lists'>
                            {profileLists && profileLists.map(list => listHTML(list))}
                        </div>
                    </div>
                </div>
                {editingProfile && profileEditPopupHTML()}
            </div>
        </>
    )
   
}