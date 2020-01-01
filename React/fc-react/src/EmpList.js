import  EmployeeDetails  from  './EmployeeDetails';
import React,{ Component } from  'react';
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

    render() {

        return ( <div>
        <table  className="table">
            <thead  key="thead">
            <tr>
                <th>Emp ID</th>
                <th>First Name</th>
                <th>Last Name</th>
                
            </tr>
            </thead>
            <tbody>
                {this.state.employeeDet.map( c  =>
                <tr  key={c.emp_id}>
                    <td>{c.emp_id}  </td>
                    <td>{c.firstname}</td>
                    <td>{c.lastname}</td>
                    
                    
                </tr>)}
            </tbody>
        </table>
        
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