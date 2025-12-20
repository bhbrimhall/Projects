import { useApi } from "./api.js";
import { useEffect, useState } from "react";

export function useList(id, purpose){
    const api = useApi();
    const [list, setList] = useState();
    const [items, setItems] = useState();
    const [listOwner, setListOwner] = useState();

    async function getList() {
        if (purpose === "edit"){
            const res = await api.get(`edit_list/${id}/`)

            if (res.success){
                setList(res.list)
                setItems(res.items)
            } else {
                // handle when something goes wrong
            }

        } else if (purpose === "view"){
            const res = await api.get(`view_list/${id}/`)

            if (res.success){
                setList(res.list)
                setItems(res.items)
                setListOwner(res.user)
            } else {
                // handle when something goes wrong
            }
        }
    }

    useEffect(() => {
        getList()
    }, [])

    if (purpose === "edit"){
        return [list, items, setItems];
    } else if (purpose === "view"){
        return [list, items, listOwner, setList];
    }


}