import React from 'react'
import svgimg from '../assets/logout-svgrepo-com.svg'
const Header = () => {
  return (
    <div className='w-full h-12 bg-slate-700 font-bold text-lg text-white pt-2 pl-4 font flex flex-row justify-between'>
        <div >Foretell</div>
        <img src={svgimg} className='p-1 pb-2 pr-4 hover:scale-75'></img>
        </div>
  )
}

export default Header