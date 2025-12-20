import { Link, useParams } from 'react-router-dom'
import { useEffect, useState } from 'react';
import { useUser } from './utils/use_user';
import { useList } from './utils/use_list';
import "./css/view_list.css"
import { useApi } from './utils/api';
import { Navbar } from './Navbar.jsx'

export function ViewList(){

    const {id} = useParams();
    const api = useApi();
    const [user, userProfile] = useUser();
    const [list, items, listOwner, setList] = useList(id, "view");
    const [editing, setEditing] = useState(false);
    const [imagePopup, setImagePopup] = useState(false);
    const [updateMyImages, setUpdateMyImages] = useState(true); // broadcast
    const [imageHTML, setImageHTML] = useState([]);
    const [comments, setComments] = useState([]);
    const [commentContent, setCommentContent] = useState("")
    const [updateComments, setUpdateComments] = useState(true)
    const [errorMessage, setErrorMessage] = useState("")
    const tier_list_letters = ['S', 'A', 'B', 'C', 'D', 'F']

    function displayList(){
        if (list.type === "raw"){
            let list_length = 0;
            items.forEach((item) => {
                if (item.rank > list_length){
                    list_length = item.rank;
                }
            });
            const list_ranks = [...Array(Number(list_length)).keys()]; 
            return (
                <>
                    <div className='raw-list-container'>
                        <div className='raw-list'>
                        {list_ranks.map((place) => 
                            <div key={`${place + 1}`}>                               
                                <div className='place'>
                                    <div className={place <= 3 ? `place-number num${place + 1}` : "place-number"}>{place + 1 }</div>
                                    <div className='place-container'>
                                        {sortItems(`${place + 1}`)}
                                    </div>
                                </div>
                            </div>

                        )}
                        </div>
                    </div>
                </>
            )
        } else {
            return(
                <>
                    <div className='tier-list-edit'>
                        {tier_list_letters.map((letter) => 

                            <div className='tier-edit' key={letter}>
                                <div className={`tier-letter ${letter}`}>{letter}</div>
                                <div className='tier-container-edit'>
                                    {sortItems(letter)}
                                </div>
                            </div>

                        )}
                    </div>
                </>
            )
        }

    }

    //used to get items with a certain rank
    function sortItems(filter){
        const sorted = items.filter((item) => item.rank === filter);
        if (!sorted) {return;}
        return sorted.map((item) => {
            return itemToElement(item);
        })
    }

    //takes an item dict and returns it in HTML form
    function itemToElement(item){
        if (item.image !== "item"){
            return (
                <div key={item.id} className='item-container'>
                    <div className='item-edit'>
                        <div className='item-image-edit'>
                            <img className='image-el' src={`/get_image/${item.image}/`}/>
                        </div>
                        <div className='item-content-edit'>
                            <div className='item-name-edit'>{item.name}</div>
                        </div>
                    </div>
                </div>
            )
        }else{
            return (
                <div key={item.id} className='imageless-item-container'>
                    <div className='item-name'>{item.name}</div>
                </div>
            )
        }
    }
    
    // saves the list changes
    async function saveListChanges(){
        
        const res = await api.post("configure_list/", list);
        if (!res.success){
            setErrorMessage("There was an issue when trying to save the changes...")
        }
        setEditing(false);
        setImagePopup(false);
    }

    // creates new image
    async function selectNewImage(e){
        
        const res = await api.postImage(e.target.files[0]);
        if (!res.success){
            setErrorMessage("There was an issue when trying to upload your image...")
        }
        // this pretty much triggers the use effect that gets the users images
        setUpdateMyImages(!updateMyImages)
        
    }

    // get images when the user logged in owns the list
    useEffect(() => {
        if (user && listOwner && user.id === listOwner.id){

            async function getImages(){
                const res = await api.get('my_images/');
                if (res.success){
                    let new_image_HTML = []

                    new_image_HTML.push(
                        <div key={-1} className='user-image-container'>
                                <div className='user-image' onClick={() => setList({...list, thumbnail: `${list.type}`})}>
                                    <img src={`/get_image/${list.type}/`} className='image-el'/>
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
                                <div className='user-image' onClick={() => setList({...list, thumbnail: image.id})}>
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
    }, [user, listOwner, updateMyImages])

    //delete image
    async function deleteImage(id){
        const res = await api.del(`delete_image/${id}/`)
        if (res.success){
            setUpdateMyImages(!updateMyImages)
        } else {
            setErrorMessage("There was an issue when trying to delete your image...")
        }
        
    }

    function listEditPopup(){
        return(
            <>
                <div className='blackout'>
                    <div className='popup-container'>
                        {imagePopup && 
                        <div className='popup-images-container'>
                            <div className='popup-images'>
                                <label>
                                    <span>Upload:</span>
                                    <input type="file" className='upload-img-button'onChange={selectNewImage}/>
                                </label>
                                <div className='user-images'>
                                    {imageHTML}
                                </div>
                            </div>
                        </div>
                        }

                        <div className='popup-edit-l'>
                            <h1 className='popup-header'>Edit List</h1>
                            <div className='popup-specs'>
                                <div className='edit-list-image'>
                                    <img src={`/get_image/${list.thumbnail}/`} className='image-el' onClick={() => setImagePopup(!imagePopup)} />
                                </div>
                                <div className='edit-list-inputs'>
                                    <label>
                                        List Title:
                                        <input type="text" value={list.name} onChange={(e) => setList({...list, name: e.target.value})}/>
                                    </label>
                                    <label>
                                        Description:
                                        <input type="text" value={list.description} onChange={(e) => setList({...list, description: e.target.value})}/>
                                    </label>
                                    <label>
                                        Public: 
                                        <input className="edit-list-publicity" type="checkbox" checked={list.is_public} onChange={() => setList({...list, is_public: !list.is_public})}/>
                                    </label>
                                    {list.name && 
                                    <div className='edit-list-submit' onClick={saveListChanges}>
                                        <div>Save Changes</div>
                                    </div>
                                    }
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </>)

    }

    function commentToElement(comment){
        return(
            <div className='comment' key={comment.id}>
                <Link className='comment-who' to={`/view_profile/${comment.profile}`}>
                    <div className='comment-profile-image'>
                        <img src={`get_image/${comment.profile_img}/`} className='image-el' />
                    </div>
                    <div className='comment-username'>{comment.username}</div>
                </Link>
                <div className='comment-content'>{comment.content}</div>
            </div>
        )
    }

    function commentsHTML(){
        return(
            <>
                <div className='comments-container'>
                    <div className='comments'>
                        {user && userProfile &&
                            <div className='make-comment'>
                                <div className='make-comment-who'>
                                    <div className='comment-profile-image'>
                                        <img src={`get_image/${userProfile.image}/`} className='image-el' />
                                    </div>
                                    <div className='make-comment-username'>{userProfile.username}</div>
                                </div>
                                <div className='make-comment-content'>
                                    <input type="text" 
                                        placeholder="Your opinion is trash..." 
                                        value={commentContent} 
                                        onChange={(e) => setCommentContent(e.target.value)}
                                        className='make-comment-input'
                                    />
                                    <div className='make-comment-post-button' onClick={postComment}>
                                        Post
                                    </div>
                                </div>
                                
                            </div>
                        }
                        {comments && comments.map((comment) => commentToElement(comment))}
                    </div>
                </div>
            </>
        )
    }

    useEffect(() => {
        async function getComments(){
            if (list && !editing){
               const res = await api.get(`get_comments/${list.id}/`)
                if (res.success){
                    setComments(res.comments.reverse())
                } else {    
                    setErrorMessage("There was an issue when trying to retrieve the comments...")
                } 
            }
            
        }
        getComments()
    }, [updateComments, list, editing])

    

    async function postComment(){
        if (commentContent){
            const res = await api.post(`comment/${list.id}/`, {content: commentContent})
            if (res.success){
                setCommentContent("")
                setUpdateComments(!updateComments)
            }else{
                setErrorMessage("There was an issue when trying to post the comment...")
            }
        }
        
    }

    return(
        <>
            <Navbar  user={user} profile={userProfile} errorMessage={errorMessage} setErrorMessage={setErrorMessage}/>
            <div className="main-container">
                {list && items && listOwner && 

                <div className='list-view-container'>
                    <div className='list-view'>
                        <div>
                            {displayList()}
                        </div>
                        <div className='list-view-attributes-container'>
                            <div className='list-view-attributes'>
                                <h1 className='list-view-title'>{list.name}</h1>
                                <Link className='list-view-owner' to={`/view_profile/${listOwner.id}`}>
                                    <div>Owner: {listOwner.username}</div>
                                </Link>
                                <div className='list-view-description'>
                                    {list.description ? list.description : "No description"}
                                </div>
                            </div>

                            {user && listOwner.id === user.id && 
                                <div className='list-view-edit-button' onClick={() => setEditing(true)}>
                                    <div>
                                        Edit List
                                    </div>
                                </div>
                            }
                        </div> 
                    
                    </div>
                </div>
                }

                {editing && listEditPopup()}

                {commentsHTML()}
            </div>
        </>
    )
}