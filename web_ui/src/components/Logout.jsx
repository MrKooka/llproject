import React, { useEffect, useState } from 'react';
import { Row, Col } from 'react-bootstrap'

import { GoogleLogout } from 'react-google-login';
const Login = () => {
    const clientId = "383926561924-0kr85vallh5j759q23i127s0mqor1ihg.apps.googleusercontent.com"
    const onSuccess = (res) => {
        console.log("Logout success");
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
                    ></GoogleLogout>

                </Col>
                <Col></Col>
            </Row>
        </div>
    );
};

export default Login;