import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './Home'
import List from './List'

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/list" component={List} />
          <Route path="/" component={Home} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
