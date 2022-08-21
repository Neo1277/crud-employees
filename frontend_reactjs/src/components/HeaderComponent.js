import React, { Component, useState } from 'react';
import { 
	Navbar, 
	NavbarBrand, 
	Nav, 
	NavbarToggler, 
	Collapse,
	NavItem
} from 'reactstrap';
import { NavLink } from 'react-router-dom';

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
                        
						{/*<NavbarBrand className="mr-auto">
							<span className="fa fa-superpowers fa-lg"></span>
						</NavbarBrand>*/}
						<Collapse isOpen={this.state.isNavOpen} navbar>
							<Nav navbar>
								<NavItem>
									<NavLink className="nav-link" to="/home">
										<span className="fa fa-home fa-lg"></span> Home  
									</NavLink>
								</NavItem>
							</Nav>		
                        </Collapse>
					</div>
				</Navbar>
            </React.Fragment>
		);
	}
}

export default Header;