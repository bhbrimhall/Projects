import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { useUser } from './utils/use_user';
import { Navbar } from './Navbar.jsx'
import "./css/homepage.css"
import { useApi } from './utils/api.js';


export function Homepage() {
  // "light" is used because a non-signed in user can visit the homepage
  const [user, userProfile] = useUser("light");
  const api = useApi()
  const [featuredLists, setFeaturedLists] = useState([]);
  const [errorMessage, setErrorMessage] = useState("");

  function listHTML(list){
    return (
    <div key={list.id} className='featured-list-display'>
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
                <Link to={`/view_profile/${list.profile}/`} className='list-profile-btn'>
                  <div>{list.username}</div>
                </Link>
            </div>
        </div>
    </div>
    )        
}


  useEffect(() => {
    async function getFeaturedLists(){
      const res = await api.get("get_featured_lists/")
      if (res.success){
        setFeaturedLists(res.lists.reverse())
      } else {
        setErrorMessage("Unable to get featured lists")
      }
    }
    getFeaturedLists()
  }, [])

  return (
    <>
      <Navbar  user={user} profile={userProfile} errorMessage={errorMessage} setErrorMessage={setErrorMessage}/>
      <div className="main-container">
        <main className='main'>
          <div className='rankit'>
            Rankit
          </div>

          <div className='main-description'>
            The website of opinions and favorites. Share yours with the internet, or flame others for theirs!
          </div>

          <div className='main-links'>
            <Link className='main-btn' to='/my_lists/create_new'>
              <div>Create List</div>
            </Link>
            <a className='main-btn' href="/registration/sign_up/">
              <div>Create Account</div>
            </a>
          </div>

          <section className='featured-lists-container'>
            <h3>Featured Lists:</h3>
            <div className='featured-lists'>
              {featuredLists && featuredLists.map((list) => listHTML(list))}
            </div>
          </section>
        </main>
      </div>
    </>
  )
}