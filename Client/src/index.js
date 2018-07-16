// import React from 'react';
// import ReactDOM from 'react-dom';
// import './index.css';
// import App from './App';
// import registerServiceWorker from './registerServiceWorker';

// ReactDOM.render(<App />, document.getElementById('root'));
// registerServiceWorker();

import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route } from "react-router-dom";
import MainPage from './MainPage';
import TopicPage from './TopicPage';
import CoursePage from './CoursePage';

import 'bootstrap/dist/css/bootstrap.css';

import './index.css';

// Application view with routes

ReactDOM.render((
  <Router>
    <div>
      {/* <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/about">About</Link>
        </li>
        <li>
          <Link to="/topics">Topics</Link>
        </li>
      </ul>
      <hr /> */}

      <Route exact path="/" component={MainPage} />
      <Route path="/main" component={MainPage} />
      <Route path="/topics/:topicName" component={TopicPage} />
      <Route path="/courses/:courseID" component={CoursePage} />
    </div>
  </Router>
), document.getElementById('root'))