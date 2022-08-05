import React, { Component, useState } from 'react';
import { 
	Navbar, 
	NavbarBrand, 
	Nav, 
	NavbarToggler, 
} from 'reactstrap';
import { NavLink } from 'react-router-dom';
import classnames from 'classnames';

class Header extends Component{
	constructor(props) {
	    super(props);

	    this.toggleNav = this.toggleNav.bind(this);

	    this.state = {
		  isNavOpen: false
	    };
	}

	toggleNav() {
	    this.setState({
	      isNavOpen: !this.state.isNavOpen
	    });
    }

    
	render(){
		return(
			<React.Fragment>
				<Navbar dark expand="md">
					<div className="container">
						<NavbarToggler onClick={this.toggleNav} />
                        
					<div className="row">
						<NavbarBrand className="mr-auto">
							<img src="/logo192.png" height="30" width="41" alt="My blog" />
						</NavbarBrand>
						{/*<Collapse isOpen={this.state.isNavOpen} navbar>
							<Nav navbar>
								<NavItem>
									<NavLink className="nav-link" to="/home">
										<span className="fa fa-home fa-lg"></span> Home  
									</NavLink>
								</NavItem>
							</Nav>		
                        </Collapse>*/}
					</div>
					</div>
				</Navbar>
            </React.Fragment>
		);
	}
}

export default Header;