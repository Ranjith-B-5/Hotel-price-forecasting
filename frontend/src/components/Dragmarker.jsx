import React, { useCallback, useMemo, useRef, useState } from 'react'
import { MapContainer, Marker, Popup,  TileLayer, useMapEvents } from 'react-leaflet'
import globalStateContext from '../context/loc-context';


function Dragmarker(props) {
    const {loc, setLoc} = React.useContext(globalStateContext);
    const [draggable, setDraggable] = useState(false)
    const [position, setPosition] = useState(props.center)
    const markerRef = useRef(null)


  
    const eventHandlers = useMemo(
      () => ({
        dragend() {
          const marker = markerRef.current
          if (marker != null) {
            setPosition(marker.getLatLng())
            setLoc({lat:marker.getLatLng().lat, long:marker.getLatLng().lng})
          }
        },
      }),
      [],
    )
    const toggleDraggable = useCallback(() => {
      setDraggable((d) => !d)
    }, [])
  
    return (
      <Marker
        draggable={draggable}
        eventHandlers={eventHandlers}
        position={position}
        ref={markerRef}>
        <Popup minWidth={90}>
          <span onClick={toggleDraggable}>
            {draggable
              ? 'Marker is draggable'
              : 'Click here to make marker draggable'}
          </span>
        </Popup>
      </Marker>
    )
  }

export default Dragmarker