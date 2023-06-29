import React from 'react'
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
  


  
function Dropdownbox(props) {

    if(props.id === '1')
    {
      var options = ['Apartment' , 'House' , 'Townhouse' , 'Condominium' , 'Serviced apartment']
    }
    else
    {
    var options = ['1', '2', '3','4'];
    }
    const defaultOption = options[0];
  return (
    <div>
    <p className='font-medium mb-1'>{props.label+":"}</p>
    <Dropdown className="w-36 rounded-sm mr-10 mb-10" options={options}  value={defaultOption} placeholder="Select an option" onChange={props.func}/>
    </div>
  )
}

export default Dropdownbox