import React, { useEffect, useState } from 'react';
import { Form, Button, Row, Col } from 'react-bootstrap'
import axios from 'axios'
import GoogleLogin from 'react-google-login';
import { gapi } from "gapi-script"
import JSON from 'json5'

const Login = () => {
    const [token, setToken] = useState('')
    const [userId, setUserId] = useState('')

    const clientId = "383926561924-0kr85vallh5j759q23i127s0mqor1ihg.apps.googleusercontent.com"
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            // console.log('cookies dsf:',cookies);
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    // console.log('csrftoken: ',getCookie('csrftoken'));
    const onSuccess = (res)=>{
        // console.log("Login success! Current user: ", res.profileObj);
        
        
    if(gapi.auth.getToken()){
        
        const accesstoken = gapi.auth2.getAuthInstance().currentUser.get().getAuthResponse().id_token
        const csrftoken = getCookie('csrftoken')
        axios({
            method:'post',
            url: "http://127.0.0.1:8000/api/google/", 
            headers:{
                "Content-Type":"application/json;charset=UTF-8",
                'X-CSRFToken': csrftoken,

            },
            data:{
                email: res.profileObj.email,
                token: accesstoken
            }
        }).then(data => {
                console.log(data)
                localStorage.setItem('token',data.data.access_token)
                localStorage.setItem('userId',data.data.user_id)
                setToken(data.data.access_token)
                setUserId(data.data.user_id)
                console.log(token);
                console.log(userId);
            })
            
            console.log(res.profileObj.email);
        }
    }

    const onFailure = (res)=>{
        console.log("login failed: res: ", res);

    }
    return (
        
        <div>
            <Row>
                <Col></Col>
                <Col ms={8}>
                    <GoogleLogin
                        clientId={clientId}
                        buttonText="Login"
                        onSuccess={onSuccess}
                        onFailure={onFailure}
                        cookiePolicy={'single_host_origin'}
                        isSignedIn={true}
                    ></GoogleLogin>

                </Col>
                <Col></Col>
            </Row>
        </div>
    );
};

export default Login;