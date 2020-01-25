import React,{ Component } from "react";
import EmpList from './EmpList'
import AttendanceList from './AttendanceList'
import { Route,withRouter, Redirect } from  'react-router-dom'
import {Navbar,Nav,Container} from 'react-bootstrap'
import history from './history';

const EmpLayout = () => (
    <div className="content">
        <Route path="/EmpList" exact component={EmpList} />
       
       
      </div>
  )

const AttLayout = () =>(
    <div className="content">
        
        <Route path="/AttendanceList" exact component={AttendanceList} />
       
      </div>
)
class Main extends Component{
    constructor(props){
        super(props)
        this.state={
            empflag:false,
            attflag:false
        }
    }

changeEmpNavFlag(e){
    let flag=this.state.empflag
    this.setState({empflag:!flag})
    this.setState({attflag:false})
}
changeAttNavFlag(e){
    let flag=this.state.attflag
    this.setState({empflag:false})
    this.setState({attflag:!flag})
}
navToEmpList(e){
    return <EmpLayout/>
}
navToAttList(e){
    return <AttLayout/>
}

logout(e)
{
   localStorage.setItem('loginStatus',false)
   history.push('/')
   
}
render(){

    
    return(
    <div align="center">
        <div align="right">
            <button onClick={(e)=>{this.logout(e)}}>Logout</button>
        </div>
      <Container>
      <Navbar bg="primary" variant="dark">
    
    <Nav className="mr-auto">
      <Nav.Link onClick={(e)=>{this.changeEmpNavFlag(e)}}>Employee List</Nav.Link>&nbsp; &nbsp;
      <Nav.Link onClick={(e)=>{this.changeAttNavFlag(e)}}>Attendance List</Nav.Link>
    </Nav>
    </Navbar>
    </Container>

    {this.state.empflag?(<EmpList/>):(<h3></h3>)}
    {this.state.attflag?(<AttendanceList/>):(<h3></h3>)}
    </div>
    );
}

}

export default Main