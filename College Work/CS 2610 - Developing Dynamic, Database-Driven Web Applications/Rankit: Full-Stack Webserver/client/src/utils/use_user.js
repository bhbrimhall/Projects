import { useEffect , useState} from "react";
import { useApi } from "./api";

export function useUser(reason="available"){
    const [user, setUser] = useState(null);
    const [profile, setProfile] = useState(null);
    const api = useApi();

    useEffect(() => {
        async function getUser(){
            const res = await api.get("get_user/")
      
            if (res.success){
                setUser(res.user);
                setProfile(res.profile)
            }else if(reason === "require"){
                window.location.replace("/registration/sign_in/")
            }
        }
        
        getUser();
    }, []);
    if (reason === "nav"){
        return [user, profile, setProfile]
    }
    return [user, profile]
}