import  EmployeeDetails  from  './EmployeeDetails';
import React,{ Component } from  'react';
import { Button} from 'react-bootstrap';


const  employeeDetails  =  new  EmployeeDetails();



class  EmpList  extends  Component {

    constructor(props) {
        super(props);
        
        this.state  = {
            employeeDet: []
            //nextPageURL:  ''
        };
        //this.nextPage  =  this.nextPage.bind(this);
        //this.handleDelete  =  this.handleDelete.bind(this);
    }
     addNewEmployee() {
        console.log('Add New Employee');
      
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
        <Button variant="contained" color="primary" onClick={this.addNewEmployee}>Add</Button>
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