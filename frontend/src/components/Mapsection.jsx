import React, { useCallback, useMemo, useRef, useState } from 'react'
import { MapContainer, Marker, Popup,  TileLayer, useMapEvents } from 'react-leaflet'
import Dragmarker from './Dragmarker'
import globalStateContext from "../context/loc-context";

// function LocationMarker() {
//   const [position, setPosition] = useState(null)
//   const map = useMapEvents({
//     click() {
//       map.locate()
//     },
//     locationfound(e) {
//       setPosition(e.latlng)
//       map.flyTo(e.latlng, map.getZoom())
//     },
//   })

//   return position === null ? null : (
//     <Marker position={position}>
//       <Popup>You are here</Popup>
//     </Marker>
//   )
// }



const Mapsection = () => {
  const {loc, setLoc} = React.useContext(globalStateContext);
  const center = [loc.lat, loc.long]
  console.log(loc)

  return (
    <div className='h-screen w-[50%] p-8'>
    <MapContainer className='w-full h-full' center={center} zoom={5} scrollWheelZoom={true}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {/* <Marker position={center}>
        <Popup>
          A pretty CSS3 popup. <br /> Easily customizable.
        </Popup>
      </Marker> */}
      <Dragmarker center ={center}/>
      {/* <LocationMarker /> */}
    </MapContainer>
    </div>
  )
}

export default Mapsection