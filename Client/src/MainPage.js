import React from 'react';
import TopicMenu from './TopicMenu';
import NavBar from './NavBar';
import './MainPage.css';
import SearchResults from './SearchResults';
import { Link } from "react-router-dom";

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
                <NavBar />
                <div className="overall-content">
                    <GetStarted skills={skillNames} />
                    <SearchResults />
                </div>
            </div>

        );
    }
}

// Get started! Explore skills such as:
class GetStarted extends React.Component {
    render() {

        let skillLinks = this.props.skills.map(function (skill) {
            return <span key={skill} className="skill-link">
                <Link to={"/topics/" + skill.replace(/ /g, "_")}>{skill}</Link>
            </span>;
        })

        return <div className="main-page-get-started">
            <div>
                <div className="main-page-get-started-header">Get started! Explore skills such as:</div>
                <div>
                    {skillLinks}
                </div>
            </div>
        </div>;
    }
}