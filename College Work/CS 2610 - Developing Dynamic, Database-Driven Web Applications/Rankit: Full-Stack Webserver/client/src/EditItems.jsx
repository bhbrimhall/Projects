import { useParams} from 'react-router-dom'
import { useEffect, useState } from 'react';
import { useUser } from './utils/use_user';
import { useApi } from './utils/api';
import { useList } from './utils/use_list';
import { Navbar } from './Navbar.jsx'
import "./css/edit_items.css"

export function EditItems(){
    const {id} = useParams();
    const api = useApi();
    const [user, userProfile] = useUser("require");
    const [list, items, setItems] = useList(id, "edit");
    const [addingItem, setAddingItem] = useState(false);
    const [itemMoving, setItemMoving] = useState(null);
    const [imagePopup, setImagePopup] = useState(false);
    const [updateMyImages, setUpdateMyImages] = useState(true); // broadcast
    const [imageHTML, setImageHTML] = useState([]);
    const [name, setName] = useState("My item");
    const [errorMessage, setErrorMessage] = useState("");
    const [imageID, setImageID] = useState(null);
    const tier_list_letters = ['S', 'A', 'B', 'C', 'D', 'F']

    //displays HTML for the type of list
    function listContainer(){
        if(list.type === "tier"){
            return (
                <>
                    <h1 className='list-title-edit'>{list.name}</h1>
                    <div className='tier-list-edit'>
                        {tier_list_letters.map((letter) => 

                            <div className='tier-edit' key={letter}>
                                <div className={`tier-letter ${letter}`}>{letter}</div>
                                <div className='tier-container-edit' onDrop={() => itemDrop(letter)} onDragOver={(e) => e.preventDefault()}>
                                    {sortItems(letter)}
                                </div>
                            </div>

                        )}
                    </div>
                </>
            )
        } else if (list.type === "raw"){
            let list_length = 0;
            items.forEach((item) => {
                if (item.rank === "") {return;}
                if (item.rank > list_length){
                    list_length = item.rank;
                }
            });
            const list_ranks = [...Array(Number(list_length) + 1).keys()];    

            return (
                <>
                    <h1 className='list-title-edit'>{list.name}</h1>
                    <div className='raw-list-edit'>
                        {list_ranks.map((place) => 
                            <div key={`${place + 1}`}>
                                
                                <div className='place-edit-between' onDrop={() => itemDrop(`${place + 0.5}`)} 
                                onDragOver={(e) => e.preventDefault()}
                                data-dragging={itemMoving ? "true" : "false"}></div>
                                
                                <div className='place'>
                                    <div className={place <= 3 ? `place-number num${place + 1}` : "place-number"}>{place + 1 }</div>
                                    <div className='place-container' onDrop={() => itemDrop(`${place + 1}`)} onDragOver={(e) => e.preventDefault()}>
                                        {sortItems(`${place + 1}`)}
                                    </div>
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

    //displays HTML for the items
    function itemContainer(){
        return (
            <>
                <div className='unadded-items'>
                    <div className='del-item' onDrop={(e) => itemDrop("delete", e)} onDragOver={(e) => e.preventDefault()}>
                        <span className='material-icons'>delete_forever</span>
                    </div>
                    <div className='add-item-btn' onClick={() => {
                        setAddingItem(true);
                        setImageID('item');
                        }}>
                        <span className='material-icons'>add</span>
                    </div>
                    {sortItems("")}
                </div>
            </>
        )
    }


    //takes an item dict and returns it in HTML form
    function itemToElement(item){
            return (
                <div key={item.id} className='item-edit-container' draggable onDragStart={() => setItemMoving(item.id)}>
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


    }

    // creates new image
    async function selectNewImage(e){
        const res = await api.postImage(e.target.files[0]);
        if (res.success){
            setUpdateMyImages(!updateMyImages)
        } else {
            setErrorMessage("There was a problem when trying to upload your image...")
        }
        
    }

    // gets the users images everytime an image is deleted or created
    useEffect(() => {
        async function getImages(){
            const res = await api.get('my_images/');
            if (res.success){
                let new_image_HTML = []

                new_image_HTML.push(
                    <div key={-1} className='user-image-container'>
                            <div className='user-image' onClick={() => setImageID("item")}>
                                <img src={`/get_image/item/`} className='image-el'/>
                            </div>
                            <div className='no-image-desc-box'>
                                <div className='no-image-desc'>No image</div>
                            </div>
                        </div>
                    )
                for(const image of res.images){
                    // add the html to the list
                    new_image_HTML.push(
                        <div key={image.id} className='user-image-container'>
                            <div className='user-image' onClick={() => {
                                setImageID(`${image.id}`);
                            }}>
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
                setErrorMessage("There was a problem when trying to get your saved images...")
            }
        }
        getImages()
    }, [updateMyImages])
    

    //delete image
    async function deleteImage(id){
        const res = await api.del(`delete_image/${id}/`)
        if (res.success){
            setUpdateMyImages(!updateMyImages)
        }else{
            setErrorMessage("There was an issue when trying to delete the image...")
        }
        
    }

    //displays the HTML for adding an item
    function addItemHTML(){
        return (
            <>
                <div className='blackout'>
                    <div className='popup-container'>
                        {imagePopup && 
                            <div className='popup-images-container-s'>
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
                        <div className='popup-edit-s'>
                            <h1 className='popup-header'>Add Item</h1>
                            <div className='popup-specs'>

                                <div className='add-item-image'>
                                    <img src={`/get_image/${imageID}/`} className='image-el' onClick={() => setImagePopup(!imagePopup)} />
                                </div>


                                <div className='add-item-words-container'>
                                    <label>
                                        Title:
                                        <input type="text" value={name} onChange={(e) => setName(e.target.value)}/>
                                    </label>
                                    {name && 
                                    <div className='add-item-submit' onClick={addItemToList}>
                                        <div>Add Item</div>
                                    </div>
                                    }
                                </div>
                            
                            </div>
                        </div>
                    </div>
                </div>
            </>
        )
    }

    //adds the new item to database
    async function addItemToList(){

        const res = await api.post("add_item/", {name: name, image: imageID, list_id: list.id});
        if (res.success){
            setName("My item");
            setImageID(null);
            let new_item_list = [...items];
            new_item_list.push(res.item);
            setItems(new_item_list);
            setAddingItem(false);
        }else{
            setAddingItem(false);
            setName("My item");
            setImageID(null);
            setErrorMessage("There was an issue when trying to add your item...")
        }
    }

    // handle when user drops an item (set rank accordingly)
    async function itemDrop(where, e=null){
        if (where === "delete"){
            e.stopPropagation();
            const res = await api.del(`/delete_item/${itemMoving}/`);
            if (res.success){
                let new_item_list = [...items];
                new_item_list = new_item_list.filter((item) => item.id !== itemMoving);
                setItems(new_item_list);
            } else {
                setErrorMessage("There was an issue when deleting your item...")
            }
        } else if (where.includes(".")) {
            //item placed in between places in raw list
            const new_item_list = [...items];
            const [item] = new_item_list.filter((item) => item.id === itemMoving);
            // if the item moved was the only item in that placement
            if (new_item_list.filter((i) => i.rank === item.rank).length === 0){
                new_item_list.forEach((i) => {
                    if (Number(i.rank) > item.rank){
                        i.rank = `${Number(i.rank) -1}`;
                    }
                });
            }

            const placement = Number(where) + 0.5;

            //move the items back a placement
            new_item_list.forEach((i) => {
                if (Number(i.rank) >= placement){
                    i.rank = `${Number(i.rank) + 1}`
                }
            });

            item.rank = `${placement}`;
            setItems(new_item_list);
            const res = await api.post("/update_items/", new_item_list);
            if (!res.success){
                setErrorMessage("There was an issue when trying to update your items...")
            }
        } else {
            const new_item_list = [...items];
            const [item] = new_item_list.filter((item) => item.id === itemMoving);
            item.rank = where;
            setItems(new_item_list);
            const res = await api.post("/update_items/", new_item_list);
            if (!res.success){
                setErrorMessage("There was an issue when trying to update your items...")
            }
        }
        setItemMoving(null);
    }

    return(
        <>
            <Navbar  user={user} profile={userProfile} errorMessage={errorMessage} setErrorMessage={setErrorMessage}/>
            <div className="main-container">
                <div className='edit-list-container'>
                    <section>
                        {list && listContainer()}
                    </section>
                    <section className='item-section' onDrop={() => itemDrop("")} onDragOver={(e) => e.preventDefault()}>
                        {items && itemContainer()}
                    </section>
                </div>

                {addingItem && addItemHTML()}
            </div>
        </>
    )
}