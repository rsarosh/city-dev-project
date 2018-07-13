import React from 'react';

export default class TopicPage extends React.Component {
    constructor(props) {
        super(props);

        let mobileView = false;

        if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Opera Mini/i.test(navigator.userAgent)) {
            console.log('Mobile');
            mobileView = true;
        }

        this.state = {
            'mobileView': mobileView
        };
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