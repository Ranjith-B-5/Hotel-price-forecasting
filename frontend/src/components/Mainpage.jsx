import React from 'react'
import { MapContainer, TileLayer ,useMap, Marker, Popup } from 'react-leaflet'
import Mapsection from './Mapsection'
import Leftsection from './Leftsection'
import axios from 'axios'
import globalStateContext from '../context/loc-context'
import Header from './Header' 
import { useState } from 'react'

const Mainpage = () => {
  const [loc, setLoc] = useState({lat:51.509865,long:-0.118092});
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

export default Mainpage