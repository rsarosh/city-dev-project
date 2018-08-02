import React, { Component } from 'react';
import { Navbar, Button } from 'react-bootstrap';
import './ProfilePage.css';

class ProfilePage extends Component {
  componentWillMount() {
    this.setState({ profile: {} });
    const { userProfile, getProfile } = this.props.auth;
    if (!userProfile) {
      getProfile((err, profile) => {
        this.setState({ profile });
      });
    } else {
      this.setState({profile: userProfile });
    }
  }

  editName() {
	
  }
  editEmail() {
	  
  }
  
  render() {
    const { isAuthenticated } = this.props.auth;
	console.log(this.state.profile);
    return (
      <div>
	    <div class="profile-header">
			
		</div>
		<br/>
		<br/>
		<div class="profile-info">
			<h1>Profile</h1>
			<p><b>Username:</b> {this.state.profile.nickname}</p>
			<p><b>Email:</b> {this.state.profile.name}</p>
			<br/>
			<br/>
			<h1>Edit Profile</h1>
			<button onClick={this.editName}>Edit username</button>
			<button onClick={this.editEmail}>Edit email</button>
		</div>
      </div>
    );
  }
}

export default ProfilePage;