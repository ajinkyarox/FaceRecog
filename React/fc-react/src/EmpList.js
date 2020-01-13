import  EmployeeDetails  from  './EmployeeDetails';
import React,{ Component } from  'react';
import { Button} from 'react-bootstrap';
import Popup from "reactjs-popup";

const  employeeDetails  =  new  EmployeeDetails();



class  EmpList  extends  Component {

    constructor(props) {
        super(props);
        
        this.state  = {
            employeeDet: [],
            showPopup: false,
            firstname: '',lastname: ''
            
        };
        this.handleFirstNameChange = this.handleFirstNameChange.bind(this);
this.handleLastNameChange=this.handleLastNameChange.bind(this);
this.handleSubmit = this.handleSubmit.bind(this);
        //this.nextPage  =  this.nextPage.bind(this);
        //this.handleDelete  =  this.handleDelete.bind(this);
    }
    togglePopup() {
        this.setState({
          showPopup: false 
        });
      }

      handleFirstNameChange(event) {
        this.setState({firstname: event.target.value});
      }
    
      handleLastNameChange(event){
        this.setState({lastname: event.target.value});
      }
    
      handleSubmit(event) {
        console.log("POSTING")
        fetch('http://localhost:8000/addEmployee', {
      method: 'POST',
      body: JSON.stringify({
        firstname: this.state.firstname,
        lastname: this.state.lastname,
      })
      
    }).then((response) => {
        return response.json() // << This is the problem
     })
     .then((responseData) => { // responseData = undefined
         alert(responseData.status);
         window.location.reload(true);
         return responseData;
     })
   .catch(function(err) {
       console.log(err);
   })
    console.log("POST")
   
   // 
      }

     

    render() {

        return ( <div>
        <table  className="table">
            <thead  key="thead">
            <tr>
                <th>Emp ID</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Update/Delete</th>
            </tr>
            </thead>
            <tbody>
                {this.state.employeeDet.map( c  =>
                <tr  key={c.id}>
                    <td>{c.id}  </td>
                    <td>{c.firstname}</td>
                    <td>{c.lastname}</td>
                    <td>
                        <Button variant="contained" color="primary">Update</Button> &nbsp;
                        <Button variant="contained" color="primary">Delete</Button>
                    </td>
                </tr>)}
            </tbody>
        </table>
    
        
        
       
        
        <Popup trigger={<button onClick={this.togglePopup.bind(this)}>Add Employee</button>} position="right center">
        <div>
        <label>
          Fisrt Name:
          <input type="text" value={this.state.firstname} onChange={this.handleFirstNameChange} />
        </label>
        <br></br>
        <label>
          Last Name:
          <input type="text" value={this.state.lastname} onChange={this.handleLastNameChange} />
        </label>
        <br></br>
<button onClick={this.handleSubmit}>Add</button>
      </div>
          </Popup>
      
    </div>);
    }
    componentDidMount() {
        var  self  =  this;
        employeeDetails.getEmployees().then(function (result) {
            console.log(result)
            self.setState({ employeeDet:  result})
        });
    }
}
export  default  EmpList;