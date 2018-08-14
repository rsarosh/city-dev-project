import React, { Component } from 'react';
import { Navbar, Button } from 'react-bootstrap';
import './DatabasePage.css';

class DatabasePage extends Component {
	state = {providers: []}
	
	constructor(props) {
        super(props);
    }

	componentWillMount() {
		var that = this;
		/* 
		 Sends a GET request to the backend of the path localhost:3001/providers-list 
		 The backend for this is handles within Backend/routes/providersList
		*/
		fetch('/providers-list')
		 .then(res => res.json())
		 .then(function(res){
			var providers = [];
			for(var i = 0; i < res.length; i ++){
				providers.push(res[i].Provider);
			}
			that.setState( {providers: providers} ); // add the provider list to the state
		 });
	}
  
	render() {
		return (
		  <div>
			<div class="profile-header">
				
			</div>
			<br/>
			<br/>
			<div class="providers-list">
				{this.state.providers.map((name) => (
				<CourseListing name={name} />
				))}
			</div>
		  </div>
		);
	}
}

class CourseListing extends Component {
	state = {opened: false, courses: []};
	
	constructor(props) {
		super(props);
	}
	
	loadCourses(){
		if(!this.state.opened) {
			var that = this;
			
			// Send out a request to the server for the courses
			fetch('/course-list?name='+this.props.name)
			 .then(res => res.json())
			 // Process the request into the state
			 .then(function(res){
				var courses = [];
				for(var i = 0; i < res.length; i ++){
					courses.push(res[i].Title);
				}
				that.setState( { courses: courses });
			 });
			
			// Lastly, set the state to opened
			this.setState({opened: true});
		}
		else {
			// Unload the courses from memory
			this.courses = [];
			
			// Set the state to closed
			this.setState({opened: false});
		}
	}
	
	render() {
		return (
			<div className="courses">
			<h1 onClick={this.loadCourses.bind(this)}> {this.props.name} </h1>
				{ this.state.opened && 
					<ol className="course-list">
						{this.state.courses.map((name) => (
							<li>{name}</li>
						))}
					 </ol>
				}
			</div>		
		)
	}
}

export default DatabasePage;