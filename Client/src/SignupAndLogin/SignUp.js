import React from 'react';
import {Button, Glyphicon, HelpBlock, FormGroup, FormControl, ControlLabel} from "react-bootstrap";
import './SignUp.css';

/*
*
* SignUp.js contains to two pages one for registration form
* and confirmation page.
*
* Registration page is rendered in first due the state variable 
* 'newUser'. If newUser is set to null it won't render the confiramtion page.
* The registration page also handles form validation for email, password, & 
* password confirmation.
*
* this.state.newUser is updated in the function handleSubmit for the 
* registration page. 
*
*/

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
            emailError: true,
            passwordError: true
            
        };
    }

    //Make sure the email input the user is proper email format
    emailRequirments() {
        //DELETE THIS ONCE COMPLETED CONFIRMATION FOR EMAIL.
        //return(this.state.email > 0);
        const email = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return email.test(String(this.state.email).toLowerCase());
    }

    passwordRequirements() {
        //DELETE THIS ONCE COMPLETED CONFIRMATION FOR EMAIL.
        //return(this.state.password > 0);

        const password = this.state.password;
        //Represents that it must have one uppercase lettet, be at least 8 characters, & alphnumeric.
        const requirments = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{7,}$/;
        return(requirments.test(password));
    }

    //Requirment for most variables that's in the form. 
    validateForm() {
        const firstName = this.state.firstName.length;
        return (
            this.state.firstName.length > 0 &&
            this.state.lastName.length > 0 &&
            this.emailRequirments() &&
            this.state.password.length > 7 &&
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
        if(this.state.email === "" && this.emailRequirments())
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

    //Event handler for changes made in the email form/input
    handleEmailChange = event => {
        this.setState({email: event.target.value});
        if(this.emailRequirments())
            this.setState({emailError: true})
        else
            this.setState({emailError: false})
    }

     //Event handler for changes made in the password form/input box.
     handlePasswordChange = event => {
        this.setState({password: event.target.value});
        if(this.passwordRequirements())
            this.setState({passwordError: true})
        else
            this.setState({passwordError: false})
    }

    //does nothing just returns the password.
    encryptPassword() {
        return this.state.password;
    }

    //action for Sign up button is pressed.
    //**User Authentication need to be added here
    handleSubmit = async event => {

        this.setState({isLoading: true});
        //When new user is updated to anything expect null page is 
        //rerendered to confirmation page.
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
                        onChange={this.handleEmailChange.bind(this)}
                        onClick={this.handleEmailChange.bind(this)}
                        placeholder="Enter email"
                        autoComplete="off"
                    />
                    {this.state.emailError ? null:<HelpBlock>Example email format: james@example.com </HelpBlock>}
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
                        onChange={this.handlePasswordChange}
                        placeholder="Enter password"
                        autoComplete="off"
                    />
                    {this.state.passwordError ? null:
                        <HelpBlock >Use at least 8 characters (Must be alphnumeric, and include 1 Uppercase letter) . </HelpBlock>
                    }
                </FormGroup>
                <FormGroup controlId="confirmPassword">
                    <ControlLabel>Confirm Password</ControlLabel>
                    <FormControl
                        autoFocus
                        type="password"
                        value={this.state.confirmPassword}
                        onChange={this.handleChange}
                        placeholder="Enter password again"
                        autoComplete="off"
                    />
                    {!(this.state.passwordError && this.state.password != this.state.confirmPassword) ? 
                        null:<HelpBlock>Password does not match. </HelpBlock>}
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
