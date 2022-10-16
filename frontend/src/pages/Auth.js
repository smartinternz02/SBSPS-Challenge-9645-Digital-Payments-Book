import React, { useEffect, useState } from 'react'
import Layout from './Layout'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import './css/auth.css'
import client from '../axios_inst'
const Auth = () => {
  const[email, setEmail] = useState('')
  const[password, setPassword] = useState('')

  useEffect(() => {
		function checkLogin() {
			localStorage.getItem('token')
		}
		checkLogin();
	}, []);

  const handleSubmit = event => {
    event.preventDefault();
      try {
        fetch('http://127.0.0.1:8000/api/user/login/', {
           method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ "email":email,"password":password })
        }).then(function(response) {
          console.log(response.clone().json());
          return response.json();
        }).then(function(data) {
          console.log(data);
          localStorage.setItem('token', data.token.access);
        })
      } catch (e) {
        console.log(e);
      }
  };

  return (
    <Layout pageVisablity={'none'}>
      <div className='auth'>
      <Form onSubmit={handleSubmit}>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Email address</Form.Label>
        <Form.Control type="email" value={email} placeholder="Enter email" onChange={(e) => {setEmail(e.target.value);
        console.log(email)}} />
        <Form.Text className="text-muted">
          We'll never share your email with anyone else.
        </Form.Text>
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" value={password} placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicCheckbox">
        <Form.Check type="checkbox" label="Remember Me" />
      </Form.Group>
      <Button variant="primary" type="submit">
        Submit  
      </Button>
    </Form>
    </div>
    </Layout>
  )
}

export default Auth


// DATABASES = {
//   'default': {
//      'ENGINE': 'django.db.backends.postgresql',
//      'NAME': 'd6tja3a5c0ql2a',
//      'USER': 'kfgbuzbainpwds',
//      'PASSWORD': 'ebea9cca99a2af47e8a0546ef90ef226e4129c9e4f7c546a6f8670c7c79c4cba',
//      'HOST': 'ec2-23-20-140-229.compute-1.amazonaws.com',
//      'PORT': '5432',
//  }
// }