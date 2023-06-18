import React, { useState } from "react";
import Inputcoord from "./Inputcoord";
import Subbotton from "./Subbotton";
import globalStateContext from "../context/loc-context";
import axios from "axios";
import Dropdownbox from "./Dropdownbox";

const Leftsection = () => {
  const {loc, setLoc} = React.useContext(globalStateContext);
  // const [latitude, setLat] = useState(loc.lat);
  // const [longitude, setLong] = useState(loc.long);
  const [accommodates, setAcc] = useState(1);
  const [proptype, setPropType] = useState({'value': 'Apartment', 'label': 'Apartment'});
  const [bedrooms, setBedrooms] = useState({'value': 1, 'label': 1});
  const [predprice,setPredPrice] = useState(0)

  function handleSubmit(e) {
    console.log("sending data")
    e.preventDefault();
    setLoc({lat : loc.lat,long: loc.long});
    axios.post('http://localhost:5000', {
      location: loc, Bedrooms: bedrooms.value, PropertyType: proptype.value, Accommodates:accommodates})
      .then((res) =>
      {
        console.log(res.data.pp[0])
        setPredPrice(Math.round(res.data.pp[0]))
        
      })

    console.log(loc);
  }

  const handleDropdownChangeone = (option) => {
    setPropType(option)

  };

  const handleDropdownChangetwo = (option) => {
    setBedrooms(option);
  };


  return (
    <div className="h-screen w-[50%] bg-gray-200 ">
      <form
        onSubmit={(e) => {
          handleSubmit(e);
        }}
      >
        <div className="flex flex-col items-center">
          <div className="m-4 p-4">
            <div className="flex flex-row">
          <p className="font-bold ml-2 mt-4 mr-4">Latitude:</p>
          <input
            contentEditable='true'
            type="text"
            value={loc.lat}
            className="h-10 w-40 m-2  border-solid rounded-sm border-b-slate-800"
            placeholder="Enter the latitude"
            // onChange={(e) => {
            //   setLat(e.target.value);
            // }}
          />
          </div>
          <div className="flex flex-row">
          <p className="font-bold ml-2 mt-4">Longitude:</p>
          <input
            contentEditable='true'
            type="text"
            value={loc.long}
            className="h-10 w-40 m-2  border-solid rounded-sm border-b-slate-800"
            placeholder="Enter the longitude"
            // onChange={(e) => {
            //   setLong(e.target.value);
            // }}
          />
          </div>
          </div>
          <div className="flex flex-row">
          <Dropdownbox label="Property Type " id="1" func={handleDropdownChangeone}></Dropdownbox>
          <Dropdownbox label="Bedrooms " id="2" func={handleDropdownChangetwo}></Dropdownbox>
          <div className="flex flex-col">
          <p className="font-semibold">Accommodates :</p>
          <input
            contentEditable='true'
            type="text"
            value={accommodates}
            className="h-10 w-40 mt-1 pl-2  border-solid rounded-sm border-b-slate-800"
            placeholder="Enter the accommodates"
            onChange={(e) => {
              setAcc(e.target.value);
            }}
          />
          </div>
          </div>
          <input
            type="submit"
            value="Predict"
            onSubmit={handleSubmit}
            className=" bg-green-600  h-10 w-20 rounded-sm hover:scale-90"
          />
          <p className="mt-8 text-xl">The predicted price is: {predprice}</p>
        </div>
      </form>
    </div>
  )
}

export default Leftsection;
