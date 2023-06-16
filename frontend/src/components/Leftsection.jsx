import React, { useState } from "react";
import Inputcoord from "./Inputcoord";
import Subbotton from "./Subbotton";
import globalStateContext from "../context/loc-context";
import axios from "axios";

const Leftsection = () => {
  const {loc, setLoc} = React.useContext(globalStateContext);
  const [latitude, setLat] = useState(loc.lat);
  const [longitude, setLong] = useState(loc.long);

  function handleSubmit(e) {
      console.log("sending data")
    e.preventDefault();
    setLoc({lat : latitude,long: longitude});
    axios.post('http://localhost:5000', {
      location: loc	})
      .then((res) =>
      {
        console.log(res)
      })

    console.log(loc);
  }

  return (
    <div className="h-screen w-[50%]  bg-black ">
      <form
        onSubmit={(e) => {
          handleSubmit(e);
        }}
      >
        <div className="flex flex-col items-center">
          <input
            contentEditable='true'
            type="text"
            value={latitude}
            className="h-10 w-40 m-2"
            placeholder="Enter the latitude"
            onChange={(e) => {
              setLat(e.target.value);
            }}
          />
          <input
            contentEditable='true'
            type="text"
            value={longitude}
            className="h-10 w-40 m-2"
            placeholder="Enter the longitude"
            onChange={(e) => {
              setLong(e.target.value);
            }}
          />
          <input
            type="submit"
            value="Predict"
            onSubmit={handleSubmit}
            className=" bg-green-600  h-10 w-20 rounded-sm"
          />
        </div>
      </form>
    </div>
  );
};

export default Leftsection;
