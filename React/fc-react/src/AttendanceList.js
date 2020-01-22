import Attendance from './AttendanceDetails';
import React,{ Component } from  'react';
//import { Base64 } from 'js-base64';

const attendanceDetails=new Attendance();

class AttendanceList extends Component{

constructor(props){
    super(props)
    this.state = {
        attendanceDetails:[]
    };
}

getMonthlyReport(event,id){
    fetch('http://localhost:8000/getMonthlyReport', {
        method: 'POST',
        body: JSON.stringify({
          eid: id,
          
        })
        
      }).then((response) => {
          return response.json() // << This is the problem
       })
       .then((responseData) => { // responseData = undefined
        console.log(responseData.responseObject)
        var data = new Blob([this.dataURItoBlob(responseData.responseObject)], {type: 'text/xlsx'});
        var url = window.URL.createObjectURL(data);
        var tempLink = document.createElement('a');
tempLink.href = url;
tempLink.setAttribute('download', responseData.filename);
                
tempLink.click();
           //window.open(tempLink)
           
          
           
           //return Base64.decode(responseData.responseObject);
       })
     .catch(function(err) {
         console.log(err);
     })
}


dataURItoBlob(b64Data) {
   const sliceSize=512;
   const contentType='';
    const byteCharacters = atob(b64Data);
  const byteArrays = [];

  for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
    const slice = byteCharacters.slice(offset, offset + sliceSize);

    const byteNumbers = new Array(slice.length);
    for (let i = 0; i < slice.length; i++) {
      byteNumbers[i] = slice.charCodeAt(i);
    }

    const byteArray = new Uint8Array(byteNumbers);
    byteArrays.push(byteArray);
  }

  const blob = new Blob(byteArrays, {type: contentType});
  return blob;
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
                <th>ID</th>
                <th>Emp ID</th>
                <th>Attendance</th>
                <th>Date & Time</th>
                <th>Monthly Report</th>
            </tr>
            </thead>
            <tbody>

                {this.state.attendanceDetails.map(c=>
                <tr key={c.id}>
                    <td>{c.id}</td>
                    <td>{c.eid}</td>
                    <td>{c.attendance}</td>
                    <td>{c.datetime}</td>
                    <td><button onClick={(e)=>this.getMonthlyReport(e,c.eid)}>Generate Monthly Report</button></td>
                </tr>

                )}
            </tbody>
        </table>

    </div>);

}


}
export  default  AttendanceList;