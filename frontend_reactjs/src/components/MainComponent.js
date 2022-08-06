import React, { Component } from 'react';

import { 
  EmployeesView
} from './EmployeesComponents/EmployeesView';
import { 
  AddEmployeeComponent
} from './EmployeesComponents/AddEmployeesView';
import { 
  EditEmployeeComponent
} from './EmployeesComponents/EditEmployeesView';
import { 
  DeleteEmployeeComponent
} from './EmployeesComponents/DeleteEmployeesView';

import Header from './HeaderComponent';
import Footer from './FooterComponent';
import { Switch, Route, Redirect, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import { 
  fetchEmployees, 
  registerEmployee,
  editEmployee,
  deleteEmployee,
  fetchCountries,
  fetchAreas,
  fetchTypesOfIdentityDocuments,
  retrieveNewEmail
} from '../redux/ActionCreators';

/* Set data gotten from Django API with redux to the Component's props */
const mapStateToProps = state => {
  return{
    employees: state.employees,
    countries: state.countries,
    areas: state.areas,
    types_of_identity_documents: state.types_of_identity_documents
  }
}

/* Set functions from ActionCreators redux to the Cpmponent's props and dispatch */
const mapDispatchToProps = (dispatch) => ({

  fetchEmployees: (link, search) => { dispatch(fetchEmployees(link, search))},
  registerEmployee: (employee_data) => dispatch(registerEmployee(employee_data)),
  editEmployee: (employee_data) => dispatch(editEmployee(employee_data)),
  deleteEmployee: (third_party_id) => dispatch(deleteEmployee(third_party_id)),

  retrieveNewEmail: (
    last_name, 
    first_name, 
    country_code, 
    third_party_id
  ) => dispatch(retrieveNewEmail(
      last_name, 
      first_name, 
      country_code, 
      third_party_id
  )),

  fetchCountries: () => { dispatch(fetchCountries())},

  fetchAreas: () => { dispatch(fetchAreas())},

  fetchTypesOfIdentityDocuments: () => { dispatch(fetchTypesOfIdentityDocuments())},

});


class Main extends Component {

  //Execute this before render
  componentDidMount() {
    this.props.fetchEmployees();
    this.props.fetchCountries();
    this.props.fetchAreas();
    this.props.fetchTypesOfIdentityDocuments();
  }

  render(){
    
    
    const EmployeeWithId = ({match}) => {
      return(
        <EditEmployeeComponent employee={this.props.employees.employees.results.filter((employee) => employee.third_party_id === match.params.id)[0]} 
                              editEmployee={this.props.editEmployee} 
                              countries={this.props.countries} areas={this.props.areas} 
                              types_of_identity_documents={this.props.types_of_identity_documents}
                              retrieveNewEmail={this.props.retrieveNewEmail} 
        />
      );
    };

    const DeleteEmployeeWithId = ({match}) => {
      return(
        <DeleteEmployeeComponent employee={this.props.employees.employees.results.filter((employee) => employee.third_party_id === match.params.id)[0]} 
                              deleteEmployee={this.props.deleteEmployee} 
                              countries={this.props.countries} areas={this.props.areas} 
                              types_of_identity_documents={this.props.types_of_identity_documents}
        />
      );
    };

    /**
     * Set routes to open the different pages calling the components
     * And redirect to home if the url that the user type in the browser
     * does not match with any url from here
     */

    return (
      <div>
        <Header />
          <Switch>
            <Route path='/home' component={() => <EmployeesView employees={this.props.employees} fetchEmployees={this.props.fetchEmployees} />} />
            <Route path='/add_employee' component={() => <AddEmployeeComponent registerEmployee={this.props.registerEmployee} 
                                                                countries={this.props.countries} areas={this.props.areas} 
                                                                types_of_identity_documents={this.props.types_of_identity_documents}
                                                                retrieveNewEmail={this.props.retrieveNewEmail} /> } />
            
            <Route path="/edit_employee/:id" component={EmployeeWithId} />
            <Route path="/delete_employee/:id" component={DeleteEmployeeWithId} />
            <Redirect to="/home" />
          </Switch>
        <Footer />
      </div>
    );
  }
}

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(Main));

