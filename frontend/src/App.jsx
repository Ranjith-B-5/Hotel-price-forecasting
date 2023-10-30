import React, { useState } from 'react'
import Mainpage from './components/Mainpage'
import Login from './components/Login'
import { Routes, Route } from "react-router-dom";
import Signup from './components/Signup'



const App = () => {
     




  
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
    <Routes>
      <Route path="/" element={<Login></Login>}/>
      <Route path="/home" element = {<Mainpage></Mainpage>}/>
      <Route path ="/signup" element={<Signup/>}/>
    </Routes>
  )
}

export default App
