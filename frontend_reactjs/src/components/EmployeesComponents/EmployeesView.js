import React, { Component }  from 'react';
import { Link } from "react-router-dom";
import { Loading } from '../LoadingComponent';
import { 
	Breadcrumb, 
	BreadcrumbItem,
	Button,
	Table,
	FormGroup, 
	Input, 
} from 'reactstrap';

// https://stackoverflow.com/a/60745732/9655579
export const removeExtraSpace = (string) => string.trim().split(/ +/).join(' ');

export class PaginationComponent extends Component {

    constructor(props){
        super(props);

        this.handlePagination = this.handlePagination.bind(this);
        this.handleSearch = this.handleSearch.bind(this);
        this.handleSearchWord = this.handleSearchWord.bind(this);

	    this.state = {
          search: null
	    };
    }

    /**
     * 
     * Send parameters to do the post request and clear fields in the view
     */

	 handlePagination(event) {
        event.preventDefault();
         //alert(event.target.href)
         
        this.props.fetchEmployees(
            event.target.href,
            this.state.search
        );
        

    }    
    /**
     * 
     * Send parameters to do the post request and clear fields in the view
     */

	 handleSearch(event) {
        event.preventDefault();

        if (!this.search.value || 
            this.search.value.trim().length === 0) {
            alert('field cannot be empty');
        }else{

            var search = removeExtraSpace(this.search.value);
            
            this.setState({
                search: search
            })
            
            this.props.fetchEmployees(
                event.target.href,
                search
            );


        }
        
    }    

    /**
     * Event to get the search value to change
     * the state and be able to pass the
     * parameters to the method to make the search
     */
    handleSearchWord(event) {
        event.preventDefault();

        this.setState({
            search: event.target.value
        })
    }

    /**
     * Render form with their respective validations
     */
     render(){
        
        return(
            
            <div className="container">
                <div className="row">             
                    <div className="col-3">
                        <FormGroup>
                            <Input onChange={this.handleSearchWord} type="text" id="search" name="search"
                                innerRef={(input) => this.search = input} />
                        </FormGroup></div>  
                    <div className="col-2">
                        <Button onClick={this.handleSearch} type="submit" value="submit" color="primary">Search</Button>
                    </div>
                </div>
            <nav aria-label="Page navigation example">
                <ul class="pagination">
                    
                {this.props.previous_link===null || this.props.previous_link==='' ? 
                    <li class="page-item">
                        <a class="page-link disabled-link" 
                            href="/">
                            Previous
                        </a>
                    </li>
                :  
                    <li class="page-item">
                        <a class="page-link" 
                        onClick={this.handlePagination} 
                        href={this.props.previous_link}>
                            Previous
                        </a>
                    </li>
                }

                {this.props.next_link==null || this.props.next_link=='' ? 
                    <li class="page-item">
                        <a class="page-link disabled-link" 
                            href="/">
                            Next
                        </a>
                    </li>
                :
                    <li class="page-item">
                        <a class="page-link" 
                        onClick={this.handlePagination} 
                        href={this.props.next_link}>
                            Next
                        </a>
                    </li>
                }


                    <li class="page-item amount-registers">
                        Amount registers {this.props.amount_registers}
                    </li>
                </ul>
            </nav>
            </div>
        );
     }
}

/**
 * Show status if the page is Loading shows spinner else shows error or the page content
 */
 export const EmployeesView = (props) => {
	console.log(props);
	
	if (props.employees.isLoading) {
		
        return(
            <Loading />
        );
    }
    else if (props.employees.errMess) {
        return(
            <h4>{props.employees.errMess}</h4>
        );
    }
	else { 
		/**
		 * Iterate over object that is in the store
		 */
		return(
			<div className="container">
				<br />
				<div className="row">
					<div className="col">
						<Breadcrumb>
							<BreadcrumbItem><Link to='/home'>Home</Link></BreadcrumbItem>
							<BreadcrumbItem active>Empleados</BreadcrumbItem>
						</Breadcrumb>
					</div>
				</div>				
				<h2 align="center">Employees</h2>
                {/**
                 * Font awesome icons:
                 * https://fontawesome.com/v4/icons/
                 */}
				<Link to='/add_employee' >
					<Button color="primary">
                        <span className="fa fa-plus-square">&nbsp;</span>  
                           Add employee
                    </Button>
                </Link>				

				<div className="row row-content">
					<Table responsive>
						<thead>
							<tr>
							<th>Type of identity document</th>
							<th>Identity Document</th>
							<th>Last Name</th>
							<th>Second Surname</th>
							<th>First name</th>
							<th>Middle_names</th>
							<th>Email</th>
							<th>Country employment</th>
							<th>Date of entry</th>
							<th>Date and time created</th>
							<th>Date and time updated</th>
							<th>State</th>
							<th>Action</th>
							</tr>
						</thead>
						<tbody>
					{props.employees.employees.results.map((field, i) => { 
						
						return(
							<tr>
                                <td>{field.type_of_identity_document}</td>
                                <td>{field.identity_document}</td>
								<td>{field.last_name}</td>
								<td>{field.second_surname }</td>
								<td>{field.first_name}</td>
								<td>{field.middle_names}</td>
								<td>{field.email}</td>
								<td>{field.country.name}</td>
								<td>{field.date_of_entry}</td>
								<td>{field.created_at}</td>
								<td>{field.updated_at}</td>
								<td>
                                {field.status == '1' ?
                                        <>Activ</>
                                    :
                                        <>Inactive</>
                                }
                                </td>
								<td>
									<Link to={`/edit_employee/${field.third_party_id}`} >
										<Button color="success">
                                            <span className="fa fa-pencil"></span>
                                        </Button>
									</Link>
									<Link to={`/delete_employee/${field.third_party_id}`} >
										<Button color="danger">
                                            <span className="fa fa-trash"></span>
                                        </Button>
                                    </Link>
                                </td>
							</tr>
						);
					}) }
						</tbody>
					</Table>

				</div>

                <PaginationComponent fetchEmployees={props.fetchEmployees} previous_link={props.employees.employees.previous} 
                                    next_link={props.employees.employees.next}  
                                    amount_registers={props.employees.employees.count}   />

			</div>
        );
	}
}
