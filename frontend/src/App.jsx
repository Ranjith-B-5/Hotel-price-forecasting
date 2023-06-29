import React, { useState } from 'react'
import { MapContainer, TileLayer ,useMap, Marker, Popup } from 'react-leaflet'
import Mapsection from './components/Mapsection'
import Leftsection from './components/Leftsection'
import axios from 'axios'
import globalStateContext from './context/loc-context'
import Header from './components/Header'






const App = () => {
     

  const [loc, setLoc] = useState({lat:51.509865,long:-0.118092});


  
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
      <Header></Header>
    <div className='flex flex-row flex-auto '>
  <Leftsection>
 
  </Leftsection>
  <Mapsection></Mapsection>
  </div>
  </globalStateContext.Provider>
  )
}

export default App
