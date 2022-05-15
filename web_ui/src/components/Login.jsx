import React, { useEffect, useState } from 'react';
import { Form, Button, Row, Col } from 'react-bootstrap'
import axios from 'axios'
import GoogleLogin from 'react-google-login';
const Login = () => {
    const clientId = "383926561924-0kr85vallh5j759q23i127s0mqor1ihg.apps.googleusercontent.com"
    const onSuccess = (res)=>{
        console.log("Login success! Current user: ", res.profileObj);
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