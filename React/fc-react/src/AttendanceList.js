import Attendance from './AttendanceDetails';
import React,{ Component } from  'react';

const attendanceDetails=new Attendance();

class AttendanceList extends Component{

constructor(props){
    super(props)
    this.state = {
        attendanceDetails:[]
    };
}
componentDidMount() {
    var  self  =  this;
    attendanceDetails.getAttendanceDetails().then(function (result) {
        console.log(result)
        self.setState({ attendanceDetails:  result})
    });
}
render(){
    return(
    <div align="center">
        <table  className="table">
        <thead  key="thead">
            <tr>
                <th>Emp ID</th>
                <th>Attendance</th>
                <th>Date</th>
            </tr>
            </thead>
            <tbody>

                {this.state.attendanceDetails.map(c=>
                <tr key={c.eid}>
                    <td>{c.eid}</td>
                    <td>{c.attendance}</td>
                    <td>{c.datetime}</td>
                </tr>

                )}
            </tbody>
        </table>

    </div>);

}


}
export  default  AttendanceList;