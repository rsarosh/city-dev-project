import React from 'react';
import './NavBar.css';
import TopicMenu from './TopicMenu';
import NavSearchBar from './NavSearchBar';
import { Link } from "react-router-dom";

// The menu that appears at the top.
// Contains a list of skill types that each have topics associated with them.
export default class NavBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            searchData: null
        };
       /*
        this.props.theData = "none";
        this.onChange = this.onChange.bind(this)

        function myCallback(theData1){
            this.props.theData = theData1; 
            
        }*/
    }
    render() {

        return (
            <div class='nav-container'>
                <div class='nav-row'>
                    <div class='nav-col nav-col-1'><a href="/"><div class="site-name">Digital Skills for All</div></a>
                    <div class="dropdown">
                        <div class="w-icon-dropdown-toggle">
                    <img src="https://uploads-ssl.webflow.com/5b367a6f5b093e44caec1fd5/5b415480e9a78842553fbfaf_download.jpeg" width="10" class="image-book"/></div>
                    <div class="dropdown-content">
                    <TopicMenu /></div>
                    </div>
                    </div>
                    <div class='nav-col nav-col-9'> </div>
                    
                </div>
                
                <div class='nav-row'>
                
                <NavSearchBar updateSearchText={(searchData) => this.setState({searchData})}/>
                {this.state.searchData}
                </div>
            </div>
            
        );
    }

}
/*
const NavSearchBar = ({count, increaseCount}) => {
    return(
      <button onClick={() => increaseCount(count + 1)}>+</button>
    )
  };
*/