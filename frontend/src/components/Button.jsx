import React from "react";

function Button(props)
{
    return(
        <button className="w-24 h-12 bg-gray-800 rounded-md text-cyan-50 mt-8">{props.text}</button>
    )
}

export default Button;