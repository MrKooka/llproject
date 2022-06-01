import React, { useEffect, useState } from 'react';
import { Row, Col } from 'react-bootstrap'
import {useNavigate} from 'react-router-dom';
import { GoogleLogout } from 'react-google-login';
const Login = () => {
    const [isAuth, setIsAuth] = useState()
    const clientId = "383926561924-0kr85vallh5j759q23i127s0mqor1ihg.apps.googleusercontent.com"
    const navigate = useNavigate();
    const onSuccess = (res) => {
        localStorage.removeItem('token')
        localStorage.removeItem('userId')
        navigate('/login')
        setIsAuth(false)
        console.log("Logout success");
    }
    const onErr = (res) => {
        console.log("Logout NOT success",res);
        console.log(localStorage);
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