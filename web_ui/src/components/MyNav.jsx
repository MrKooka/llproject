import React, { useState } from 'react';
import { Navbar, Container, Nav, NavDropdown, Form } from 'react-bootstrap'
import { Link } from "react-router-dom";

const MyNav = () => {
    
    return (
        <div>
            <Navbar bg="light" expand="lg">
                <Container>
                    <Navbar.Brand href="#home">MyDictionary</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                            <Link to="/add"><Nav.Link href="#home">Add</Nav.Link></Link>
                            <Link to="/train"><Nav.Link href="#home">Train</Nav.Link></Link>
                            <Link to="/list"><Nav.Link href="#home">List</Nav.Link></Link>
                            <Link to="/login"><Nav.Link href="#home">Login</Nav.Link></Link>
                        </Nav>
                        <Form.Group>
                            <Form.Control type="text"  />
                        </Form.Group>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </div>
    );
};

export default MyNav;