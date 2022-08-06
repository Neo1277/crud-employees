import React, { Component }  from 'react';
import { Link } from "react-router-dom";
import { Loading } from '../LoadingComponent';
import { 
	Breadcrumb, 
	BreadcrumbItem,
	Button,
	Form, 
	FormGroup, 
	Input, 
    Label, 
} from 'reactstrap';

/**
 * Delete employee component
 */
 export class DeleteEmployeeComponent extends Component {

    constructor(props){
        super(props);

        this.handleDelete = this.handleDelete.bind(this);

    }

    /**
     * 
     * Send parameters to do the delete employee request and clear fields in the view
     */

    handleDelete(event) {
        event.preventDefault();
        /**
         * Show message to confirm before delete register from 
         * the database
         */
        var menssage = 'Are you sure you want to delete the employee? Yes / No';
        if (window.confirm(menssage)) {
            this.props.deleteEmployee(
                this.props.employee.third_party_id
            );
        } else {
            
            console.log('Do not delete');
        }
        

    }    

    /**
     * Render form with their respective validations
     */
    render(){
        
        if (this.props.countries.isLoading) {
		
            return(
                <Loading />
            );
        }
        else if (this.props.countries.errMess) {
            return(
                <h4>{this.props.errMess}</h4>
            );
        }
        else { 
            return(
                <div className="container">
                    
                    <br />
                    <div className="row">
                        <div className="col">
                            <Breadcrumb>
                                <BreadcrumbItem><Link to='/home'>Home</Link></BreadcrumbItem>
                                <BreadcrumbItem active>Delete employee</BreadcrumbItem>
                            </Breadcrumb>
                        </div>
                    </div>		
                    <br />
                    <div className="row row-content">
                        <div className="col-12">
                            <h4>Delete Employee</h4>
                        </div>
                        <div className="col-12 col-md-9">

                            <Form onSubmit={this.handleDelete}>
                                <FormGroup>
                                    <Label for="types_of_identity_documents_id">Type of identity document</Label>
                                    <Input type="select" name="types_of_identity_documents_id" 
                                    id="types_of_identity_documents_id" innerRef={(input) => this.types_of_identity_documents_id = input}
                                    value={this.props.employee.types_of_identity_documents_id}>
                                    {this.props.types_of_identity_documents.types_of_identity_documents.map((field, i) => { 
                                        return(
                                            <>
                                                <option value={field.id}>{field.description}</option>
                                            </>
                                        );
                                    }) }
                                    </Input>
                                </FormGroup>
                                <FormGroup>
                                    <Label htmlFor="identity_document">Identity Document</Label>
                                    <Input type="text" id="identity_document" name="identity_document"
                                        innerRef={(input) => this.identity_document = input}
                                        value={this.props.employee.identity_document} />
                                </FormGroup>
                                <FormGroup>
                                    <Label htmlFor="last_name">Primer apellido</Label>
                                    <Input type="text" id="last_name" name="last_name"
                                        innerRef={(input) => this.last_name = input} 
                                        value={this.props.employee.last_name} />
                                </FormGroup>
                                <FormGroup>
                                    <Label htmlFor="second_surname">Second Surname</Label>
                                    <Input type="text" id="second_surname" name="second_surname"
                                        innerRef={(input) => this.second_surname = input} 
                                        value={this.props.employee.second_surname} />
                                </FormGroup>
                                <FormGroup>
                                    <Label htmlFor="first_name">First name</Label>
                                    <Input type="text" id="first_name" name="first_name"
                                        innerRef={(input) => this.first_name = input} 
                                        value={this.props.employee.first_name}  />
                                </FormGroup>
                                <FormGroup>
                                    <Label htmlFor="middle_names">Middle_names</Label>
                                    <Input type="text" id="middle_names" name="middle_names"
                                        innerRef={(input) => this.middle_names = input} 
                                        value={this.props.employee.middle_names} />
                                </FormGroup>
                                <FormGroup>
                                    <Label htmlFor="email">Email</Label>
                                    <Input type="email" id="email" name="email"
                                        innerRef={(input) => this.email = input}
                                        value={this.props.employee.email}  />
                                </FormGroup>
                                <FormGroup>
                                    <Label for="country">Country employment</Label>
                                    <Input type="select" name="country" 
                                    id="country" innerRef={(input) => this.country = input} 
                                    value={this.props.employee.country.code}>
                                    {this.props.countries.countries.map((field, i) => { 
                                        /*{
                                            if (i==0){
                                                this.setState({
                                                    abreviacion: field.abreviacion
                                                });
                                            }
                                        }*/
                                        return(
                                            <>
                                                <option value={field.code}>{field.name} - {field.code}</option>
                                            </>
                                        );
                                    }) }
                                    </Input>
                                </FormGroup>
                                <FormGroup>
                                    <Label for="area_id">Area</Label>
                                    <Input type="select" name="area_id" 
                                    id="area_id" innerRef={(input) => this.area_id = input}
                                    value={this.props.employee.area_id}>
                                    {this.props.areas.areas.map((field, i) => { 
                                        return(
                                            <>
                                                <option value={field.id}>{field.description}</option>
                                            </>
                                        );
                                    }) }
                                    </Input>
                                </FormGroup>
                                <FormGroup>
                                    <Label htmlFor="date_of_entry">Date of entry</Label>
                                    <Input type="datetime-local" id="date_of_entry" name="date_of_entry"
                                        innerRef={(input) => this.date_of_entry = input}  
                                        value={this.props.employee.date_of_entry} />
                                </FormGroup>
                                
                                <Button type="submit" value="submit" color="danger">Delete</Button>
                            </Form>
                        </div>
                    </div>
                </div>
            );
        }
    }

}
