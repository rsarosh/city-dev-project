import React from 'react';
import './TopicMenu.css';

// The menu that appears at the top.
// Contains a list of skill types that each have topics associated with them.
export default class TopicMenu extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            
            'OpenedSkillTypeTabIndex': 0
            /* The index of the tab that is opened.
               Will be changed when hovering over a different tab
                0: Essential (default)
                1: General
                2: Specialist
            */
        };
    }

    render() {

        return (
            <div>
                <h1>TopicMenu Component</h1>
                {/* Left column containing skill type tabs */}
                <div className="topic-menu-skill-type-column">
                    <TopicMenuSkillTypeTab name="Essential" />
                    <TopicMenuSkillTypeTab name="General" />
                    <TopicMenuSkillTypeTab name="Specialist" />
                </div>
                {/* Right area containing the different topics */}
                <div className="topic-menu-topic-area">
                    <TopicMenuColumn name="Subjects" />
                    <TopicMenuColumn name="Software" />
                    <TopicMenuColumn name="Learning Paths" />
                </div>
            </div>
        );
    }
}

// Allows the user to switch between active tabs
class TopicMenuSkillTypeTab extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return <div>{this.props.name}</div>;
    }
}

// 3 different columns, 
class TopicMenuColumn extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return <div>{this.props.name}</div>;
    }
}

class TopicMenuLink extends React.Component {
    render() {
        return <div>I'm B</div>;
    }
}