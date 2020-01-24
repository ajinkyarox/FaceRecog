import React,{ Component } from "react";
import EmpList from './EmpList'
import AttendanceList from './AttendanceList'
import { Route,withRouter, Redirect } from  'react-router-dom'
import {Navbar,Nav,Container} from 'react-bootstrap'

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
    this.setState({attflag:flag})
}
changeAttNavFlag(e){
    let flag=this.state.attflag
    this.setState({empflag:flag})
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
    return <Redirect to='/' />
}
render(){

    
    return(
    <div align="center">
        <div align="left">
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