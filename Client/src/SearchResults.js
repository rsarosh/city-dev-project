import React from 'react';
import './SearchResults.css';
import SideFilter from './SideFilter.js';
import { Link } from "react-router-dom";

export default class SearchResults extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        document.title = 'Digital Skills For All';
    }

    render() {

        // A fake database of courses - 1st level keys are IDs
        // Images come from the Public folder/img
        const fakeCourseDatabase = {
            0: {
                name: 'El Centro',
                date: '7/2/2018',
                skillLevel: 'Specialist Skills',
                image: '/img/Lighthouse.jpg',
                description: 'Arista, percolator, cream, aromatic, fair trade, breve body instant lungo blue mountain cappuccino. Americano aroma mug espresso latte crema milk redeye acerbic. Galão robusta instant, decaffeinated, so fair trade wings.'
            },
            1: {
                name: 'Seattle Public Libraries',
                date: '7/2/2018',
                skillLevel: 'Specialist Skills',
                image: '/img/Mountain.jpg',
                description: 'Single shot cultivar beans as chicory caffeine. Medium brewed, milk extra that froth pumpkin spice mocha. Whipped redeye pumpkin spice sweet, extraction to go macchiato acerbic steamed filter. Robusta grounds decaffeinated.'
            },
            2: {
                name: 'Goodwill',
                date: '7/2/2018',
                skillLevel: 'General Skills',
                image: '/img/Canyon.jpg',
                description: 'Computing,'
            }
        }

        // Replace this with getting the IDs of different courses later
        let searchResults = [0, 1, 2];

        let searchResultComponents = searchResults.map(function(searchResult) {
            return <div key={searchResult}><SearchResult db={fakeCourseDatabase} id={searchResult}/></div>
        })

        return (
            <div>
                <h1 className="search-results-heading">
                    Search Results for [WORD]
                </h1>
                <SideFilter/>
                <div className="search-results-container">
                    {searchResultComponents}
                </div>
            </div>
        );
    }
}

// Every search result
class SearchResult extends React.Component {

    render() {

        let data = this.props.db[this.props.id];
        let coursePageLink = "/courses/" + this.props.id + "/" + data.name.replace(/ /g,"_");

        return <div className="search-result">
            <div className="search-result-image-container">
            <Link to={coursePageLink}><img className="search-result-image" src={data.image} alt={data.name}/></Link>
            </div>
            <div className="search-result-description-container">
                <h2 className="search-result-title">{data.name}</h2>
                <div className="skill-and-date">{data.date}&nbsp;&nbsp;&nbsp;{data.skillLevel}</div>
                <div className="description">
                    {data.description} <Link to={coursePageLink}>Read more...</Link>
                </div>
            </div>
        </div>;
    }
}