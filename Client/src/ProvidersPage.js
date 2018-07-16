import React from 'react';

export default class ProvidersPage extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        document.title = 'Digital Skills For All';
    }

    render() {
        
        return (
            <div>
                <h1>
                    Providers page
                </h1>
            </div>
        );
    }
}