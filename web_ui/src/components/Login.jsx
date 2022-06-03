import React, { useEffect, useState } from 'react';
import { Form, Button, Row, Col } from 'react-bootstrap'
import {useNavigate} from 'react-router-dom';
import getCookie from '../utils/browser/getCookie';
import GoogleLogin from 'react-google-login';
import { gapi } from "gapi-script"
import PostService from "../api/postService"
import {useDispatch} from 'react-redux'
import {login} from "../store/authSlice"
import {CLIENTID} from "../settings/settings"

const Login = () => {
    const navigate = useNavigate();
    const dispatcher = useDispatch()
    const clientId = CLIENTID
    const onSuccess = (res)=>{
    if(gapi.auth.getToken()){
        const accesstoken = gapi.auth2.getAuthInstance().currentUser.get().getAuthResponse().id_token
        const email = res.profileObj.email
        const name = res.profileObj.name
        let csrftoken = getCookie('csrftoken')
        PostService.loginAPI(email, accesstoken, name, csrftoken).then(result =>{
            const user = {
                accesstoken:result.data.access_token,
                userId: result.data.user_id,
                email: email
            }
            dispatcher(login(user))
            navigate('/profile')
        })

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