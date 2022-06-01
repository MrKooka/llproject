import {React,useState, useEffect} from 'react';
import axios  from 'axios';

const Profile = () => {
    const [userInfo, setUserInfo] = useState({})
    // console.log(localStorage.getItem('token'));
    
    useEffect(()=>{
        const token = localStorage.getItem('token')
        axios.get('http://127.0.0.1:8000/api/me/',{headers: {'Authorization': `Token ${token}`}}).then(data=>{
            setUserInfo({
            name:data.data.name,
            email:data.data.email,
            chatId:data.data.chat_id
            })
        })
        
    },[])
    
    
    return (
        <div>
            <h3>{userInfo.name}</h3>
            <h3>{userInfo.email}</h3>
            <h3>{userInfo.chatId}</h3>
        </div>
    );
};

export default Profile;