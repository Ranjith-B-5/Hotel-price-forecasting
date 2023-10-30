import React from 'react';
import { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import Button from './Button';
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
import { initializeApp } from "firebase/app";
import firebaseConfig from '../Firebase';


function Login() {
	
	
	const [ email, setEmail ] = useState('');
	const [ password, setPsswd ] = useState('');
	const firebaseApp = initializeApp(firebaseConfig);
	const firebaseAuth = getAuth(firebaseApp);
	
	function handleSubmit(e) {
		e.preventDefault(); 
		
		signInWithEmailAndPassword(firebaseAuth, email, password)
		.then((userCredential) => {
		// Signed in 
		const user = userCredential.user;
		window.location.href = '/home';
		})
		.catch((error) => {
			const errorCode = error.code;
			const errorMessage = error.message;
			console.log(errorMessage)
			alert("user not found")
		});
	}
	

	return (
		<div className="h-screen w-full bg-slate-400 pt-44">
			<form
				onSubmit={(e) => {
					console.log("hello")
					handleSubmit(e);
				}}
				>
				<div className="h-64 w-96 mx-auto bg-slate-600 rounded shadow-lg items-center">
					<div className="flex flex-col items-center p-12">
						<input
							className="m-4 w-64 h-8 rounded-md"
							type="email"
							value={email}
							placeholder="Username"
							required
							onChange={(e) => {
								setEmail(e.target.value);
							}}
						/>
						<input
							className=" w-64 h-8 rounded-md"
							type="password"
							value={password}
							placeholder="Password"
							required
							onChange={(e) => {
								setPsswd(e.target.value);
							}}
						/>
						<div className="flex flex-row justify-around w-64">
							<input
								type="submit"
								value="Login"
								className="w-24 h-12 bg-gray-800 rounded-md text-cyan-50 mt-8"
							/>
							<Link to="/signup">
								<Button text="SignUp" />
							</Link>
						</div>
					</div>
				</div>
			</form>
		</div>
	);



}

export default Login;
