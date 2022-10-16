import React, { useState } from 'react'
import './css/layout.css'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

const Layout = (props) => {
  const[loggedIn, setLoggedIn] = useState(false);
  return (
    <div className='layout'>
      <Navbar bg="dark" variant='dark' expand="lg">
      <Container>
        <Navbar.Brand className='justify-content-start flex-grow-1 pe-3 m-2' href="/">Mercurius Book</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="justify-content-end flex-grow-1 pe-3">
            <Nav.Link className='m-2' href="/purchase-history">Purchases</Nav.Link>
            <Nav.Link className='m-2' href="/payment-history">Payments</Nav.Link>
            {loggedIn ? <Nav.Link className='m-2' href="/logout">Logout</Nav.Link> : <Nav.Link className='m-2' href="/auth">Login/Signup</Nav.Link>}

          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
   <div className='child_info' style={{display: `${props.pageVisablity}` }}>
   <Card className="text-center" >
      <Card.Header>{props.pageName}</Card.Header>
      {/* PUT GOOD TYPOGRAPHY */}
      <Card.Body>
        {/* <Card.Title>{props.title}</Card.Title> */}
        <Card.Text>
          {/* {props.description} */}
          {props.pageDesc}
        </Card.Text>
        <Button variant="primary">Help</Button>
      </Card.Body>
    </Card>

   </div>
    <div className='layout_child'>{props.children}</div>
    </div>
  )
}

export default Layout