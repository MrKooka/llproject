import React, { useEffect, useState } from 'react';
import { Navbar, Container, Nav, NavDropdown, Form } from 'react-bootstrap'
import { Link } from "react-router-dom";

const MyNav = () => {
    const [isAuthenticated, setIsAuthenticated] = useState(false)
    const isAuthenticatedFunction = ()=>{
        if (localStorage.getItem('userId')){
            setIsAuthenticated(true)
        }
        console.log(localStorage.getItem('userId'));
        
    }
    useEffect(() => {
        isAuthenticatedFunction()
        const userId = localStorage.getItem('userId')
        if (userId) {
            setIsAuthenticated(true)
        }
        console.log(isAuthenticated);
    }, [])

    return (
        <div>
            <Navbar bg="light" expand="lg">
                <Container>
                    <Link to="/"><Navbar.Brand>MyDictionary</Navbar.Brand></Link>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                        <li class="nav-item active">
                            <Link to="/add"><a class="nav-link">Add</a></Link>
                        </li>
                        <li class="nav-item active">
                            <Link to="/train"><a class="nav-link">Train</a></Link>
                        </li>
                        <li class="nav-item active">
                            <Link to="/list"><a class="nav-link">List</a></Link>
                        </li>
                        
                        {!isAuthenticated &&
                        <li class="nav-item active">
                            <Link to="/login"><a class="nav-link">Login</a></Link>
                        </li>
                        }
                        {isAuthenticated &&
                        <li class="nav-item active">
                            <Link to="/profile"> <a class="nav-link">Profile</a></Link>
                        </li>
                        }
                        {isAuthenticated &&
                        <li class="nav-item active">
                        <Link to="/logout"><a class="nav-link" >Logout</a></Link>
                        </li>
                        }
                      
                        </Nav>
                        <Form.Group>
                            <Form.Control type="text" />
                        </Form.Group>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </div>
    );
};

export default MyNav;