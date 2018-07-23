import React from 'react';
import './SideFilter.css';
import { Link } from "react-router-dom";

// The menu that appears at the top.
// Contains a list of skill types that each have topics associated with them.
export default class SideFilter extends React.Component {
    constructor(props) {
        super(props);


    }
    render() {

        return (
            <div>
                
                <div class="white-wrapper">
                <h1>Filters</h1>
                <div class="w-form">
                <form id="email-form" name="email-form" data-name="Email Form">
                <label for="location">Location:</label>
                <input type="text" class="w-input" maxlength="256" name="location" data-name="location" placeholder="Location..." id="location"></input>
                <label for="email-2">Level:</label>
                <select id="field" name="field" multiple="" class="w-select">
                <option value="">Select one...</option>
                <option value="First">Essentials</option>
                <option value="Second">General</option>
                <option value="Third">Specialist</option>
                </select><br/>
                <label for="email-2">Age:</label>
                <select id="field-2" name="field-2" multiple="" class="w-select">
                <option value="">Select one or more...</option>
                <option value="First">Adult</option>
                <option value="Second">Young Adult</option>
                <option value="Third">Youth</option>
                </select>
                <label for="email-2">Cost:</label>
                <select id="field-2" name="field-2" multiple="" class="w-select">
                <option value="">Select one or more...</option>
                <option value="First">Free</option>
                <option value="First">$</option>
                <option value="Second">$$</option>
                <option value="Third">$$$</option>
                </select>
                <label for="email-2">Filter:</label>
                <select id="field-2" name="field-2" class="w-select">
                <option value="">Select one...</option>
                <option value="First">First Choice</option>
                <option value="Second">Second Choice</option>
                <option value="Third">Third Choice</option>
                </select>
                <label for="email-2">Filter:</label>
                <select id="field-2" name="field-2" class="w-select">
                <option value="">Select one...</option>
                <option value="First">First Choice</option>
                <option value="Second">Second Choice</option>
                <option value="Third">Third Choice</option>
                </select>
                <label for="name-2">Filter:</label>
                </form>
                <div class="w-form-done">
                <div>Thank you! Your submission has been received!</div>
                </div>
                <div class="w-form-fail">
                <div>Oops! Something went wrong while submitting the form.</div>
                </div>
                </div>
                <form action="/search" class="w-form">
                <input type="search" class="w-input" maxlength="256" name="query" placeholder="Filter…" id="search" required=""></input>
                <input type="submit" value="Search" class="round_buttons w-button"></input>
                </form>
                </div>
                
            </div>
        );
    }
}


