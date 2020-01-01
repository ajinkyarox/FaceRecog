import React from 'react';
//import logo from './logo.svg';
import './App.css';
import EmpList from './EmpList'
import { BrowserRouter } from  'react-router-dom'
import { Route } from  'react-router-dom'

const BaseLayout = () => (
  <div className="content">
      <Route path="/EmpList" exact component={EmpList} />
    </div>
)

function App() {
  return (
    <div>
      <h1>FaceRecog</h1>
      <h2>
      <BrowserRouter>
        <BaseLayout/>
      </BrowserRouter>
      </h2>

    </div>
  );
}

export default App;
