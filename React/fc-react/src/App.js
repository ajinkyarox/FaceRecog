import React from 'react';
import {Navbar,Nav,Container} from 'react-bootstrap';
import './App.css';
import EmpList from './EmpList'
import AttendanceList from './AttendanceList'
import { BrowserRouter } from  'react-router-dom'
import { Route } from  'react-router-dom'

const BaseLayout = () => (
  <div className="content">
      <Route path="/EmpList" exact component={EmpList} />
      <Route path="/AttendanceList" exact component={AttendanceList} />
    </div>
)

function App() {
  
  return (
    <div>
      <h1>FaceRecog</h1>
      
      <BrowserRouter>
      <Container>
      <Navbar bg="primary" variant="dark">
    
    <Nav className="mr-auto">
      <Nav.Link href="/EmpList">Employee List</Nav.Link>&nbsp; &nbsp;
      <Nav.Link href="/AttendanceList">Attendance List</Nav.Link>
    </Nav>
    </Navbar>
    </Container>

        <BaseLayout/>
      </BrowserRouter>
      

    </div>
  );
}

export default App;
