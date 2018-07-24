import React from 'react';

export default class SignUp extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        document.title = 'Digital Skills For All';
    }

    render () {
        console.log(this.props)
        return (
            <div class='header-section'>
                <h1>Login</h1>
            </div>
        );    
    }

}
