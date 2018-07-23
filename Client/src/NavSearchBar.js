import React from 'react';
import './NavBar.css';
import TopicMenu from './TopicMenu';
import { Link } from "react-router-dom";


/*
export default class NavSearchBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
 
        };

       
    }
    render() {
        return (
        <div class='search-row'>
        <div class='nav-col nav-col-9 search-box'>
          search row 
        </div>
        <div class="nav-col nav-col-1">
        <input type="submit" value="Search" class="search-button" ></input>
        </div>
    </div>
    );
    }
}

*/

const NavSearchBar = ({searchData, updateSearchText}) => {
    return(
        <div class='search-row'>
        
        <input class='nav-col nav-col-9 search-box' type="search" maxlength="256" name="query" placeholder="Search for a service provider…" id="search-2" required=""/> 
        
        <div class="nav-col nav-col-1">
        <input type="submit" value="Search" class="search-button" onClick={() => updateSearchText(document.getElementById('search-2').value)}></input>
        </div>
      </div>
    )
  };

export default NavSearchBar;
