import React, { useEffect, useState } from 'react';
import { Navbar, Container, Nav, NavDropdown, Form } from 'react-bootstrap'
import { Link } from "react-router-dom";
import {useSelector} from "react-redux"
const MyNav = () => {
    const user = useSelector(state => state.auth.user);
    const isAuthenticated = user.isAuthenticated
    
    return (
        <div>
            <Navbar bg="light" expand="lg">
                <Container>
                    <Link to="/"><Navbar.Brand>MyDictionary</Navbar.Brand></Link>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                        <li className="nav-item active">
                            <Link to="/add" className="nav-link">Add</Link>
                        </li>
                        <li className="nav-item active">
                            <Link to="/train" className="nav-link">Train</Link>
                        </li>
                        <li className="nav-item active">
                            <Link to="/list" className="nav-link" >List</Link>
                        </li>
                        
                        {!isAuthenticated &&
                        <li className="nav-item active">
                            <Link to="/login" className="nav-link">Login</Link>
                        </li>
                        }
                        {isAuthenticated &&
                        <li className="nav-item active">
                            <Link to="/profile" className="nav-link" >Profile</Link>
                        </li>
                        }
                        {isAuthenticated &&
                        <li className="nav-item active">
                        <Link to="/logout" className="nav-link">Logout</Link>
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