import React from 'react';
import Button from '@material-ui/core/Button';
import axios from 'axios'
import './wordclock.css';

interface Props {}

interface State {
  
};

export default class WordClock extends React.Component<Props, State> {
  state: State = {
    
  };



  render () {
    return (
      <div>
        <Button variant="contained" onClick={() => axios.post('http://localhost:8080/wordclock')}>
        Start
        </Button>
        <Button variant="contained" onClick={() => axios.post('http://localhost:8080/stop')}>
        Stop
        </Button>
      </div>
    );
  }
}
