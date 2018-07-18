import React from 'react';
import './NavBar.css';
import TopicMenu from './TopicMenu.js';
import { Link } from "react-router-dom";

// The menu that appears at the top.
// Contains a list of skill types that each have topics associated with them.
export default class NavBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
 
        };
    }
    render() {

       

        return (
            <div class='nav-container'>
                <div class='nav-row'>
                    <div class='nav-col nav-col-1'>test
                    <div class="dropdown">
                        <div class="w-icon-dropdown-toggle"></div>
                        <img src="https://uploads-ssl.webflow.com/5b367a6f5b093e44caec1fd5/5b415480e9a78842553fbfaf_download.jpeg" width="10" class="image-2"/>
                    <div class="dropdown-content">
                    <TopicMenu /></div>
                    </div>
                    </div>
                    <div class='nav-col nav-col-9'>long test</div>
                    
                </div>
            </div>
            
        );
    }

}




