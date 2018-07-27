
import React, { Component } from 'react';
import loading from '../img/dog.png';

class Callback extends Component {
  render() {
    const style = '';

    return (
      <div style={style}>
        <img src={loading} alt="loading"/>
      </div>
    );
  }
}

export default Callback;