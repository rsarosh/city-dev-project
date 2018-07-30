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
import SignUp from './SignupAndLogin/SignUp';
//import Login from './SignupAndLogin/Login';
import Login from './Login'; //uses Auth0
import ProfilePage from './ProfilePage';
import Callback from './Callback/Callback';
import Auth from './Auth/Auth';
import history from './history';
import App from './App';
import 'bootstrap/dist/css/bootstrap.css';

import './index.css';

// Application view with routes
const auth = new Auth();

const handleAuthentication = (nextState, replace) => {
  if (/access_token|id_token|error/.test(nextState.location.hash)) {
    auth.handleAuthentication();
  }
}


ReactDOM.render((
  <Router history={history} component={MainPage}>
    <div>
      <Route path="/callback" render={(props) => {
          handleAuthentication(props);
          return <MainPage {...props} /> 
        }}/>
       <Route exact path="/" render={(props) => <MainPage auth={auth} {...props} />} />
       <Route path="/home" render={(props) => <MainPage auth={auth} {...props} />} />
       <Route path="/main" render={(props) => <MainPage auth={auth} {...props} />} />
       <Route path="/sign-up" render={(props) => <SignUp auth={auth} {...props} />} />
       <Route path="/log-in" render={(props) => <Login auth={auth} {...props} />} />
       <Route path="/topics/:topicName" render={(props) => <TopicPage auth={auth} {...props} />} />
       <Route path="/courses/:courseID" render={(props) => <CoursePage auth={auth} {...props} />} />
	   <Route path="/profile" render={(props) => <ProfilePage auth={auth} {...props} />} />
    </div>
  </Router>
), document.getElementById('root'))