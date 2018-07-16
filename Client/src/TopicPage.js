import React from 'react';

export default class TopicPage extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        document.title = 'Digital Skills For All';
    }

    render() {

        console.log(this.props);
        return (
            <div>
                <h1>
                    {this.props.match.params.topicName.replace(/_/g, ' ')}
                </h1>
            </div>
        );
    }
}