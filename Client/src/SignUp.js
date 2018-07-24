import React from 'react';
import {Button, Glyphicon, HelpBlock, FormGroup, FormControl, ControlLabel} from "react-bootstrap";

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
            zipcode: "",
            password: "",
            confirmPassword: "",
            newUser: null,
            confirmationCode: "",
        };
    }

    //Make sure the email input the user is proper email format
    validateEmail() {
        const email = this.state.email;
        if(email.length > 0 &&
            email.includes('@')) {
                return true;
        }
        return false;
    }

    //Requirment for most variables that's in the form. 
    validateForm() {
        const firstName = this.state.firstName.length;
        return (
            this.state.firstName.length > 0 &&
            this.state.lastName.length > 0 &&
            this.validateEmail() &&
            this.state.password.length > 0 &&
            this.state.age.length > 0 &&
            //Zip-code should be length of 6
            this.state.zipcode.length > 4 &&
            this.state.password === this.state.confirmPassword
        );
    }

    validateConfirmationForm() {
        return this.state.confirmationCode.length > 0;
    }

    //Event handler for changes made in any of the states.
    handleChange = event => {
        this.setState({
            [event.target.id]: event.target.value
        });
    }

    handleSubmit = async event => {
        event.preventDefault();

        this.setState({isLoading: true});
        this.setState({newUser:"test"})
        this.setState({isLoading: false})
    }

    handleConfirmationSubmit = async event => {
        event.preventDefault();

        this.setState({isLoading: true})
    }

    //Confirmation Form UI
    renderConfirmationForm() {
        return (
            <div className="confirmation-submit-page">
                <form onSubmit={this.handleConfirmationSubmit}>
                    <FormGroup controlId="confirmationCode">
                        <ControlLabel>Confirmation Code</ControlLabel>
                        <FormControl
                            type="tel"
                            value={this.state.confirmationCode}
                            onChange={this.handleChange}
                        />
                        <HelpBlock>Please check email for confirmation code</HelpBlock>
                    </FormGroup>

                    {/*add submit button*/}
                    <Button
                    className="sign-in-button"
                    type="submit"
                    bsStyle="primary"
                    //disabled={}
                    //onClick={}
                > 
                Confirm
                </Button>
                </form>
            </div>
        );
    }

    //Sign up form UI
    renderForm() {
        //Debugging support
        console.log(this.state)
        //console.log(!this.validateForm())
        console.log(this.state.isLoading)

        const {isLoading} = this.state.isLoading;
        return (
            <div className="start-up-signup-box">
                {/*Signup form contains: First name, last name, 
                email, age, zip code, password, confirm password*/}
                
                <FormGroup controlId="firstName">
                    <ControlLabel>First Name</ControlLabel>
                    <FormControl
                        autoFocus
                        type="firstName"
                        value={this.state.firstName}
                        onChange={this.handleChange}
                    />
                </FormGroup>
                <FormGroup controlId="lastName">
                    <ControlLabel>Last Name</ControlLabel>
                    <FormControl
                        autoFocus
                        type="lastName"
                        value={this.state.lastName}
                        onChange={this.handleChange}
                    />
                </FormGroup>
                <FormGroup controlId="email">
                    <ControlLabel>Email</ControlLabel>
                    <FormControl
                        autoFocus
                        type="email"
                        value={this.state.email}
                        onChange={this.handleChange}
                    />
                </FormGroup>
                <FormGroup controlId="age">
                    <ControlLabel>Age</ControlLabel>
                    <FormControl
                        autoFocus
                        type="number"
                        value={this.state.age}
                        onChange={this.handleChange}
                    />
                </FormGroup>
                <FormGroup controlId="zipcode">
                    <ControlLabel>Zip Code</ControlLabel>
                    <FormControl
                        autoFocus
                        type="text"
                        value={this.state.zipcode}
                        onChange={this.handleChange}
                    />
                </FormGroup>
                <FormGroup controlId="password">
                    <ControlLabel>Password</ControlLabel>
                    <FormControl
                        autoFocus
                        type="password"
                        value={this.state.password}
                        onChange={this.handleChange}
                    />
                </FormGroup>
                <FormGroup controlId="confirmPassword">
                    <ControlLabel>Confirm Password</ControlLabel>
                    <FormControl
                        autoFocus
                        type="password"
                        value={this.state.confirmPassword}
                        onChange={this.handleChange}
                    />
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
