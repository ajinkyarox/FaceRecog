import  EmployeeDetails  from  './EmployeeDetails';
import React,{ Component } from  'react';
const  employeeDetails  =  new  EmployeeDetails();

class  EmpList  extends  Component {

    constructor(props) {
        super(props);
        this.state  = {
            employeeDet: ''
            //nextPageURL:  ''
        };
        //this.nextPage  =  this.nextPage.bind(this);
        //this.handleDelete  =  this.handleDelete.bind(this);
    }

    render() {

        return (<div>
          {this.state.employeeDet}
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