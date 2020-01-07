import React,{ Component } from  'react';
//import Popup from "reactjs-popup";
class PopJS extends Component {
    render() {
      return (
       
        <div className='popup'>
          <div className='popup_inner'>
            <h1>{this.props.text}</h1>
          <button onClick={this.props.closePopup}>close me</button>
          </div>
        </div>
       
      );
    }
  }

  export default PopJS;