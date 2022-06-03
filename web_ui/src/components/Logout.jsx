import React, { useEffect, useState } from 'react';
import { Row, Col } from 'react-bootstrap'
import {useNavigate} from 'react-router-dom';
import { GoogleLogout } from 'react-google-login';
import {logout} from "../store/authSlice"
import {useDispatch} from "react-redux"
import {CLIENTID} from "../settings/settings"
const Login = () => {
    const dispatcher = useDispatch()
    const clientId = CLIENTID
    const navigate = useNavigate();
    const onSuccess = (res) => {
        dispatcher(logout())
        navigate('/login')
    }
    const onErr = (res) => {
        console.log("Logout NOT success",res);
    }
    
    return (

        <div>
            <Row>
                <Col></Col>
                <Col ms={8}>
                    <GoogleLogout
                        clientId={clientId}
                        buttonText="Logout"
                        onLogoutSuccess={onSuccess}
                        onFailure={onErr}
                    ></GoogleLogout>

                </Col>
                <Col></Col>
            </Row>
        </div>
    );
};

export default Login;