import React, { useState } from 'react'
import { MapContainer, TileLayer ,useMap, Marker, Popup } from 'react-leaflet'
import Mapsection from './components/Mapsection'
import Leftsection from './components/Leftsection'
import axios from 'axios'
import globalStateContext from './context/loc-context'





const App = () => {
     

  const [loc, setLoc] = useState({lat:37.0902,long:-95.7129});


  
    // function sendPosition(latlng)
    // {
    //   console.log("sending data")
    //   axios.post('http://localhost:8000', {
		// 		data: "data"	})
    //     .then((res) =>
    //     {
    //       console.log(res)
    //     })
    // }

    // sendPosition();

  return (
    <globalStateContext.Provider value={{loc , setLoc}}>
    <div className='flex flex-row flex-auto '>
  <Leftsection></Leftsection>
  <Mapsection></Mapsection>
  </div>
  </globalStateContext.Provider>
  )
}

export default App
