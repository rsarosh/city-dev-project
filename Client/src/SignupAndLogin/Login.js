import React from 'react';
import {Button, Glyphicon, HelpBlock, FormGroup, FormControl, ControlLabel} from "react-bootstrap";

export default class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isLoading: false,
            email: '',
            password: "",
            
        };
    }

    //Make sure the email input the user is proper email format
    emailRequirements() {
        //DELETE THIS ONCE COMPLETED CONFIRMATION FOR EMAIL.
        //return(this.state.email > 0);
        return true;
    }

    passwordRequirements() {
        //DELETE THIS ONCE COMPLETED CONFIRMATION FOR EMAIL.
        //return(this.state.password > 0);

        return true;
    }

    //Requirment for most variables that's in the form. 
    validateForm() {
        return (
            this.emailRequirements() &&
            this.passwordRequirements()
        );
    }

    //Requirements for the confirmation form.
    validateConfirmationForm() {
        return this.state.confirmationCode.length > 0;
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



    //Sign up form UI
    renderForm() {
        //Debugging support
        //console.log(this.state)
        //console.log(this.state.isLoading)

        const {isLoading} = this.state.isLoading;
        return (
            <div className="start-up-signup-box">
               
                
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
                </FormGroup>
                {/*Button is disabled till'this.state' variable all fits the requirements
                in the validateForm function. Once clicked on it gets updated to the
                confirmation page*/}
                <Button
                    className="log-in-button"
                    type="submit"
                    bsStyle="primary"
                    disabled={!this.validateForm() || isLoading}
                    onClick={this.handleSubmit}
                > 
                    {isLoading && <Glyphicon glyph="refresh" className="spinning"/>}
                    {!isLoading ? 'log in':'Loading...'}
                </Button>
            </div> 
        );    
    }

    //render everything on to the page.
    render() {
        return (
            <div className="signup-options">
                {this.renderForm()}
            </div>
        );
    }

}
