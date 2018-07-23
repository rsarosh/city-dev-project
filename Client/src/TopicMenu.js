import React from 'react';
import './TopicMenu.css';
import { Link } from "react-router-dom";

// The menu that appears at the top.
// Contains a list of skill types that each have topics associated with them.
export default class TopicMenu extends React.Component {
    constructor(props) {
        super(props);

        this.state = {

            'OpenedSkillTypeTab': 0
            /* The index of the tab that is opened.
               Will be changed when hovering over a different tab
                0: Essential (default)
                1: General
                2: Specialist
            */
        };

        this.switchTabOnHover = this.switchTabOnHover.bind(this);
    }

    // When a tab is hovered, switch the active tab to the hovered tab
    switchTabOnHover(tabIndex) {
        this.setState({
            'OpenedSkillTypeTab': tabIndex
        });
    }



    render() {

        const that = this;

        // Right area content for:
        // 0: Essential
        // 1: General
        // 2: Specialist
        const topics = {

            0: {
                'Learning Paths': ['Start a small business'],
                'Skills': ['Digital Marketing', 'Accounting'],
                'Software': ['Microsoft Excel', 'Salesforce']
            },
            1: {
                'Learning Paths': ['Officia Ipsam Quas Aut', 'Aperiam Eligendi'],
                'Skills': ['Digital Marketing', 'Graphic Design'],
                'Software': ['Photoshop', 'Illustrator']
            },
            2: {
                'Learning Paths': ['Esse Velit', 'Labore lure Magnam'],
                'Skills': ['Web Development', 'Data Analysis', 'Graphic Design'],
                'Software': ['Photoshop', 'Microsoft Word', 'Microsoft Excel', 'Salesforce', 'Illustrator']
            },
        };

        return (
            <div>
                {/* <h1>TopicMenu Component</h1> */}
                {/* Left column containing skill type tabs */}
                <div className="topic-menu-skill-type-column">
                    <TopicMenuSkillTypeTab onMouseOver={function () { that.switchTabOnHover(0) }} name="Business" active={this.state.OpenedSkillTypeTab === 0} />
                    <TopicMenuSkillTypeTab onMouseOver={function () { that.switchTabOnHover(1) }} name="Creative" active={this.state.OpenedSkillTypeTab === 1} />
                    <TopicMenuSkillTypeTab onMouseOver={function () { that.switchTabOnHover(2) }} name="Technology" active={this.state.OpenedSkillTypeTab === 2} />
                </div>
                {/* Right area containing the different topics */}
                <div className="topic-menu-topic-area">
                    <div id="topicAreaForTab_0" className={' ' + (this.state.OpenedSkillTypeTab !== 0 ? 'hidden' : '')}>
                        <TopicMenuColumn name="Learning Paths" links={topics[0]['Learning Paths']} />
                        <TopicMenuColumn name="Skills" links={topics[0]['Skills']} />
                        <TopicMenuColumn name="Software" links={topics[0]['Software']} />
                    </div>
                    <div id="topicAreaForTab_1" className={' ' + (this.state.OpenedSkillTypeTab !== 1 ? 'hidden' : '')}>
                        <TopicMenuColumn name="Learning Paths" links={topics[1]['Learning Paths']} />
                        <TopicMenuColumn name="Skills" links={topics[1]['Skills']} />
                        <TopicMenuColumn name="Software" links={topics[1]['Software']} />
                    </div>
                    <div id="topicAreaForTab_2" className={' ' + (this.state.OpenedSkillTypeTab !== 2 ? 'hidden' : '')}>
                        <TopicMenuColumn name="Learning Paths" links={topics[2]['Learning Paths']} />
                        <TopicMenuColumn name="Skills" links={topics[2]['Skills']} />
                        <TopicMenuColumn name="Software" links={topics[2]['Software']} />
                    </div>
                </div>
            </div>
        );
    }
}

// Allows the user to switch between active tabs
class TopicMenuSkillTypeTab extends React.Component {

    // constructor(props) {
    //     super(props);
    // }

    render() {
        return <div onMouseOver={this.props.onMouseOver} className={'topic-menu-skill-type-tab' + (this.props.active === true ? ' active-topic-menu-skill-type-tab' : '')}>
            {this.props.name}
        </div>;
    }
}

// 3 different columns, 
class TopicMenuColumn extends React.Component {
    // constructor(props) {
    //     super(props); 
    // }

    render() {
        let links = this.props.links.map(function (link) {
            return <li key={link}><Link to={"/topics/" + link.replace(/ /g,"_")}>{link}</Link></li>;
        })

        return <div className="topic-menu-column">
            <div className="topic-menu-column-header">{this.props.name}</div>
            <ul>
                {links}
            </ul>
        </div>;
    }
}