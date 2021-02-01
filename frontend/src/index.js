import React from "react";
import ReactDOM from "react-dom";
import "bootstrap/dist/css/bootstrap.min.css"; // add this
import { Route, BrowserRouter as Router, Switch } from "react-router-dom";
import App from "./App";
import Register from "./components/register";

const routing = (
	<Router>
		<React.StrictMode>
			<Switch>
				<Route exact path="/" component={App} />
				<Route exact path="/register" component={Register} />
			</Switch>
		</React.StrictMode>
	</Router>
);

// import * as serviceWorker from './serviceWorker';

ReactDOM.render(routing, document.getElementById("root"));
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
// serviceWorker.unregister();
