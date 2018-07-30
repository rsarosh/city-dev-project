import React, { Component } from 'react';
import { Navbar, Button } from 'react-bootstrap';
//import './Login.css';

class ProfilePage extends Component {


  getName() {
	  
  }
  
  render() {
    const { isAuthenticated } = this.props.auth;

	console.log(isAuthenticated());
	
    return (
      <div>
		Name: 
		Email:
		Password:
      </div>
    );
  }
}

export default ProfilePage;