import React from 'react';
import TopicMenu from './TopicMenu';
import SearchResults from './SearchResults';

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

        const skillNames = ['Typing', 'Web Development', 'Accounting', 'Microsoft Office', 'UX', 'Game Design', 'Mobile Developer', 'IT', 'Graphic Design', 'Microsoft Excel', 'System Administration', 'Microsoft Word']

        return (
            <div>
                <TopicMenu />
                <GetStarted skills={skillNames}/>
                <SearchResults />
            </div>

        );
    }
}

// Get started! Explore skills such as:
class GetStarted extends React.Component {
    render() {

        let skillLinks = this.props.skills.map(function (skill) {
            return <div key={skill}>{skill}</div>;
        })

        return <div>
            <div>
                Get started! Explore skills such as:
                <div>
                    {skillLinks}
                </div>
            </div>
        </div>;
    }
}

class GetStartedSkill extends React.Component {
    render() {
        return <div>
            <div>
                {this.props.name}
            </div>
        </div>;
    }
}