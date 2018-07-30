import React from 'react';
import {Button, Glyphicon, HelpBlock, FormGroup, FormControl, ControlLabel} from "react-bootstrap";

/*Basic info on it: https://alligator.io/react/axios-react/
*
*if axios doesn't work install: npm install axios
*if still getting warning of somethings install also:
*   npm install ajv
*   npm install jquery popper.js
*/
//import axios from 'axios';

import './SignUp.css';

export default class SignUp extends React.Component {
    constructor(props) {
        super(props);
        //State 
        this.state = {
            isLoading: false,
            firstName: "",
            lastName: "",
            email: "",
            age: "",
            password: "",
            confirmPassword: "",
            newUser: null,
            confirmationCode: "",
            emailError: false,
            passwordError: false,
            
        };
    }

    //Make sure the email input the user is proper email format
    emailRequirments() {
        //DELETE THIS ONCE COMPLETED CONFIRMATION FOR EMAIL.
        //return(this.state.email > 0);
        const email = this.state.email;
        return(email.length > 0 &&
            email.includes('@'));
    }

    passwordRequirements() {
        //DELETE THIS ONCE COMPLETED CONFIRMATION FOR EMAIL.
        //return(this.state.password > 0);

        const password = this.state.password;
        const alphnumeric = /[A-za-z0-9]/;
        return(alphnumeric.test(password) &&
            password.length > 7);
    }

    //Requirment for most variables that's in the form. 
    validateForm() {
        const firstName = this.state.firstName.length;
        return (
            this.state.firstName.length > 0 &&
            this.state.lastName.length > 0 &&
            this.emailRequirments() &&
            this.passwordRequirements() > 0 &&
            this.state.age.length > 0 &&
            this.state.password === this.state.confirmPassword
        );
    }

    //Requirements for the confirmation form.
    validateConfirmationForm() {
        return this.state.confirmationCode.length > 0;
    }

    //
    handleChangeForEmailError() {
        if(this.state.email == "" && this.emailRequirments())
            this.setState({emailError:false})
        else
            this.setState({emailError:true})
    } 

    //Event handler for changes made in any of the states.
    handleChange = event => {
        this.setState({
            [event.target.id]: event.target.value
        });
    }

    //action for Sign up button is pressed.
    //**User Authentication need to be added here
    handleSubmit = async event => {
        event.preventDefault();
        //axios.post('/api/users', {user: this.state})
        this.setState({isLoading: true});
        this.setState({newUser:"test"})
        this.setState({isLoading: false})
    }

    //action for when confirmation button is submited.
    handleConfirmationSubmit = async event => {
        event.preventDefault();

        this.setState({isLoading: true})
    }

    //Confirmation Form UI
    renderConfirmationForm() {
        console.log(this.state);
        return (
            <div className="confirmation-submit-page">
                <form onSubmit={this.handleConfirmationSubmit}>
                    <FormGroup controlId="confirmationCode">
                        <HelpBlock>Please Verify Email</HelpBlock>
                    </FormGroup>
                    <br/>
                    <FormGroup controlId="resend-help-message">
                        <HelpBlock>If email hasn't sent click on "Resend".</HelpBlock>
                    </FormGroup>
                    {/*add submit button*/}
                    <Button
                    className="send-again-button"
                    type="submit"
                    bsStyle="primary"
                    //disabled={}
                    //onClick={}
                    > 
                        Resend
                    </Button>
                </form>
            </div>
        );
    }

    //Sign up form UI
    renderForm() {
        //Debugging support
        //console.log(this.state)
        //console.log(this.state.isLoading)

        const {isLoading} = this.state.isLoading;
        return (
            <div className="start-up-signup-box">
                {/*Signup form contains: First name, last name, 
                email, age, zip code, password, confirm password*/}
                
                <FormGroup controlId={"firstName"}>
                    <ControlLabel>First Name</ControlLabel>
                    <FormControl
                        autoFocus
                        type="firstName"
                        value={this.state.firstName}
                        onChange={this.handleChange}
                        placeholder="Enter first name"
                    />
                </FormGroup>
                <FormGroup controlId="lastName">
                    <ControlLabel>Last Name</ControlLabel>
                    <FormControl
                        autoFocus
                        type="lastName"
                        value={this.state.lastName}
                        onChange={this.handleChange}
                        placeholder="Enter last name"
                    />
                </FormGroup>
                {/*using controlID to two different if for different states 
                    determined by emailError if it's error a red border is shown.*/}
                <FormGroup controlId={this.state.emailError ? 'error' : "email"}>
                    <ControlLabel>Email</ControlLabel>
                    <FormControl
                        autoFocus
                        type="email"
                        value={this.state.email}
                        onChange={this.handleChange}
                        placeholder="Enter email"
                    />
                    {this.emailRequirments() ? null:<HelpBlock controlId='emailError'>Email format: user@gmail.com</HelpBlock>}
                </FormGroup>
                <FormGroup controlId="age">
                    <ControlLabel>Age</ControlLabel>
                    <FormControl
                        autoFocus
                        type="text"
                        value={this.state.age}
                        onChange={this.handleChange}
                        placeholder="Enter age"
                    />
                </FormGroup>
                <FormGroup controlId="password">
                    <ControlLabel>Password</ControlLabel>
                    <FormControl
                        autoFocus
                        type="password"
                        value={this.state.password}
                        onChange={this.handleChange}
                        placeholder="Enter password"
                    />
                    {this.passwordRequirements() ? null:<HelpBlock controlId='emailError'>Password must be alphnumeric and include 1 Uppercase letter. </HelpBlock>}
                </FormGroup>
                <FormGroup controlId="confirmPassword">
                    <ControlLabel>Confirm Password</ControlLabel>
                    <FormControl
                        autoFocus
                        type="password"
                        value={this.state.confirmPassword}
                        onChange={this.handleChange}
                    />
                    {this.state.password == this.state.confirmPassword ? 
                        null:<HelpBlock controlId='emailError'>Password does not match. </HelpBlock>}
                </FormGroup>
                {/*Button is disabled till'this.state' variable all fits the requirements
                in the validateForm function. Once clicked on it gets updated to the
                confirmation page*/}
                <Button
                    className="sign-in-button"
                    type="submit"
                    bsStyle="primary"
                    disabled={!this.validateForm() || isLoading}
                    onClick={this.handleSubmit}
                > 
                    {isLoading && <Glyphicon glyph="refresh" className="spinning"/>}
                    {!isLoading ? 'Sign Up':'Loading...'}
                </Button>
            </div> 
        );    
    }

    //render everything on to the page.
    render() {
        return (
            <div className="signup-options">
                {/*if newUser is null the sign up page is rendered, once user
                sign up successfull they will be redirected to confirmation page.*/}
                {this.state.newUser === null
                ? this.renderForm() : 
                this.renderConfirmationForm()}
            </div>
        );
    }
}
