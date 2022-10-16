import React, { useState } from 'react'
import Layout from './Layout'
import Nav from 'react-bootstrap/Nav';
import './css/purchaseHistory.css'
import { Card, Table } from "react-bootstrap";

import ListGroup from 'react-bootstrap/ListGroup';

function PurchaseHistory() {
  const [status, setStatus] = useState('All')

  return (
    <Layout pageName={'Purchase History'} pageDesc={'View all of your Purchase records here'}>
    <div className='status_nav'>
      <Nav className='justify-content-center' variant="pills" defaultActiveKey="All" onSelect={(selectedKey) => setStatus(selectedKey)}>
      <Nav.Item>
        <Nav.Link eventKey="All">All</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="Paid">Paid</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="Pending">Pending</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="Due" variant="secondry">
          Due
        </Nav.Link>
      </Nav.Item>
    </Nav>
    </div>
    <div className='cart_container'>
    <div className='cart'>

      <Card >
      <Card.Body>
        {/* <h3 style={{textAlign: 'center', textWeight: 'bold'}}>Paid</h3> */}
        <Table striped bordered hover >
          <thead>
            <tr>
              <th>Product</th>
              <th>Quantity</th>
              <th>Price</th>
              <th>Amount</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>OG</td>
              <td>3</td>
              <td>130</td>
              <td>390</td>
            </tr>
            <tr>
              <td>Water Bottle</td>
              <td>3</td>
              <td>20</td>
              <td>60</td>
            </tr>
            <tr>
              <td>Bus</td>
              <td>5</td>
              <td>150</td>
            </tr>
            <tr>
              <th>Date</th>
              <th colSpan={'2'} style={{textAlign: 'center'}}>Status</th>
              <th>Total</th>
            </tr>
            <tr>
              <th>4th July 2021</th>
              <th colSpan={'2'} style={{textAlign: 'center'}}>Paid</th>
              <th>6,555</th>
            </tr>
            
          </tbody>
        </Table>      
        </Card.Body>
          </Card> </div>

          <div className='cart'>

<Card >
<Card.Body>
  {/* <h3 style={{textAlign: 'center', textWeight: 'bold'}}>Paid</h3> */}
  <Table striped bordered hover >
    <thead>
      <tr>
        <th>Product</th>
        <th>Quantity</th>
        <th>Price</th>
        <th>Amount</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>OG</td>
        <td>3</td>
        <td>130</td>
        <td>390</td>
      </tr>
      <tr>
        <td>Water Bottle</td>
        <td>3</td>
        <td>20</td>
        <td>60</td>
      </tr>
      <tr>
        <td>Bus</td>
        <td>5</td>
        <td>150</td>
      </tr>
      <tr>
        <th>Date</th>
        <th colSpan={'2'} style={{textAlign: 'center'}}>Status</th>
        <th>Total</th>
      </tr>
      <tr>
        <th>4th July 2021</th>
        <th colSpan={'2'} style={{textAlign: 'center'}}>Paid</th>
        <th>6,555</th>
      </tr>
      
    </tbody>
  </Table>      
  </Card.Body>
    </Card> </div><div className='cart'>

<Card >
<Card.Body>
  {/* <h3 style={{textAlign: 'center', textWeight: 'bold'}}>Paid</h3> */}
  <Table striped bordered hover >
    <thead>
      <tr>
        <th>Product</th>
        <th>Quantity</th>
        <th>Price</th>
        <th>Amount</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>OG</td>
        <td>3</td>
        <td>130</td>
        <td>390</td>
      </tr>
      <tr>
        <td>Water Bottle</td>
        <td>3</td>
        <td>20</td>
        <td>60</td>
      </tr>
      <tr>
        <td>Bus</td>
        <td>5</td>
        <td>150</td>
      </tr>
      <tr>
        <th>Date</th>
        <th colSpan={'2'} style={{textAlign: 'center'}}>Status</th>
        <th>Total</th>
      </tr>
      <tr>
        <th>4th July 2021</th>
        <th colSpan={'2'} style={{textAlign: 'center'}}>Paid</th>
        <th>6,555</th>
      </tr>
      
    </tbody>
  </Table>      
  </Card.Body>
    </Card> </div><div className='cart'>

<Card >
<Card.Body>
  {/* <h3 style={{textAlign: 'center', textWeight: 'bold'}}>Paid</h3> */}
  <Table striped bordered hover >
    <thead>
      <tr>
        <th>Product</th>
        <th>Quantity</th>
        <th>Price</th>
        <th>Amount</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>OG</td>
        <td>3</td>
        <td>130</td>
        <td>390</td>
      </tr>
      <tr>
        <td>Water Bottle</td>
        <td>3</td>
        <td>20</td>
        <td>60</td>
      </tr>
      <tr>
        <td>Bus</td>
        <td>5</td>
        <td>150</td>
      </tr>
      <tr>
        <th>Date</th>
        <th colSpan={'2'} style={{textAlign: 'center'}}>Status</th>
        <th>Total</th>
      </tr>
      <tr>
        <th>4th July 2021</th>
        <th colSpan={'2'} style={{textAlign: 'center'}}>Paid</th>
        <th>6,555</th>
      </tr>
      
    </tbody>
  </Table>      
  </Card.Body>
    </Card> </div>
          </div>
      </Layout>
      
    
  )
}

export default PurchaseHistory