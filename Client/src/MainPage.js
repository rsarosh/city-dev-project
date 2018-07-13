import React from 'react';
import TopicMenu from './TopicMenu';

export default class MainPage extends React.Component {
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

        return (
            <div>
                <TopicMenu />
                <GetStarted />
            </div>

        );
    }
}

// Get started! Explore skills such as:
class GetStarted extends React.Component {
    render() {
        return <div>
            <div>
                Get started! Explore skill such as:
            </div>
        </div>;
    }
}