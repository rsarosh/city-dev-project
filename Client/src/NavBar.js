import React from 'react';
import './NavBar.css';
import TopicMenu from './TopicMenu';
import NavSearchBar from './NavSearchBar';
import { Link } from "react-router-dom";
import Login from './Login';
import auth0 from 'auth0-js';

// The menu that appears at the top.
// Contains a list of skill types that each have topics associated with them.
export default class NavBar extends React.Component {

	constructor(props) {
        super(props);
        this.state = {
            searchData: null
        };
	
       /*
        this.props.theData = "none";
        this.onChange = this.onChange.bind(this)

        function myCallback(theData1){
            this.props.theData = theData1; 
            
        }*/
    }
	
    render() {
		const { isAuthenticated } = this.props.auth;
		
        return (
            <div class='nav-container'>
                <div class='nav-row'>
                    <div class='nav-col'><a href="/"><div class="site-name">Digital Skills for All</div></a>
                    <div class='account-info'>
					
					{
						isAuthenticated() && (
							<div class='account-login-signup-link'><UserProfileAndLogout/></div>
						)
					}
					{
						!isAuthenticated() && (
							<div class='account-login-signup-link'><UserLoginAndSignUp/></div>
						)
					}
					<Link to='/db-handle' class='button'>DB Test</Link>
					</div>
                    <div class="dropdown">
                        <div class="w-icon-dropdown-toggle">
                    <img src="https://uploads-ssl.webflow.com/5b367a6f5b093e44caec1fd5/5b415480e9a78842553fbfaf_download.jpeg" width="10" class="image-book"/></div>
                    <div class="dropdown-content">
                    <TopicMenu /></div>
                    </div>
                    </div>
                    <div class='nav-col nav-col-9'> </div>
                    
                </div>
                
                <div class='nav-row'>
                
                <NavSearchBar updateSearchText={(searchData) => this.setState({searchData})}/>
                {this.state.searchData}
                </div>
            </div>
            
        );
    }


}

//Main page link to login and sign
class UserLoginAndSignUp extends React.Component {
    render() {
        const signUpHref = '/sign-up';
        const loginHref = '/log-in';

        return (
            <div>
                
                    
                        <Link to={signUpHref} class='button'>Sign up</Link>
                    
                    
                        <Link to={loginHref} class='button'>Log in/out</Link> 
                    
            </div>
        );
    }
   
}

class UserProfileAndLogout extends React.Component {
	render(){
		const logoutHref = '/log-in';
		const profileHref = '/profile';
		return (
			<div>
				<Link to={logoutHref} class='button'>Log out</Link> 
				<Link to={profileHref} class='button'>Profile</Link>
			</div>
		);
	}
}