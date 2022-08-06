import * as ActionTypes from './ActionTypes';
import { 
  baseUrlApiRest, 
  employees, 
  save_employees, 
  update_employees, 
  delete_employees, 
  retrieve_new_email,
  countries,
  areas,
  types_of_identity_documents
} from '../shared/baseUrl';

export const fetchEmployees = (link = null, search = null) => (dispatch) => {

  dispatch(employeesLoading(true));
  
  /**
   * Validations to check that the parameters of searching
   * and the link with pagination are not empty, if they are
   * empty then do the GET request with the url without no parameters
   * https://stackoverflow.com/a/61726089/9655579
   */
  
  if (link==null || link=='') {
    
    link = baseUrlApiRest +   employees;

  } 

  if (typeof search != "undefined" && search) {
    link = link + '?search='+search;
  }
  
  
  return fetch(link, {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    },
    credentials: "same-origin"
  })
  .then(response => {
    if (response.ok) {
      return response;
    } else {
      var error = new Error('Error ' + response.status + ': ' + response.statusText);
      error.response = response;
      throw error;
    }
  })
  .then(response => response.json())
  .then(employees => dispatch(addEmployees(employees)))
  .catch(error => dispatch(employeesFailed(error.message)));

}

/* Call action type from employees reducer */
export const employeesLoading = () => ({
    type: ActionTypes.EMPLOYEES_LOADING
});

/* Call action type from employees reducer */
export const employeesFailed = (errmess) => ({
    type: ActionTypes.EMPLOYEES_FAILED,
    payload: errmess
});

/* Call action type from employees reducer */
export const addEmployees = (employees) => ({
    type: ActionTypes.ADD_EMPLOYEES,
    payload: employees
});

/**
 * Register Employee
 */
 export const registerEmployee = (employee_data) => (dispatch) => {
   
  return fetch(baseUrlApiRest +  save_employees, {
      method: "POST",
      body: JSON.stringify(employee_data),
      headers: {
        "Content-Type": "application/json"
      },
      credentials: "same-origin"
  })
  .then(response => {
      if (response.ok) {
        return response;
      } else {
        var error = new Error('Error ' + response.status + ': ' + response.statusText);
        error.response = response;
        throw error;
      }
    },
    error => {
          throw error;
    })
  .then(response => response.json())
  .then(response => { 
    console.log('Register Employee', response); 
    alert('Employee registered successfully!\n'); 
    /*window.location.reload(false);*/
    window.location.href = '/home'; 
  })
  .catch(error =>  { 
    console.log('Register Employee', error.message); 
    alert('Employee could not be registered\nError: '+error.message); 
  });
};

/**
 * Edit Employee
 */
 export const editEmployee = (employee_data) => (dispatch) => {
  
  var third_party_id = employee_data.third_party_id + '';

  //alert(postId);
  return fetch(baseUrlApiRest +  update_employees + '/' + third_party_id, {
      method: "PUT",
      body: JSON.stringify(employee_data),
      headers: {
        "Content-Type": "application/json"
      },
      credentials: "same-origin"
  })
  .then(response => {
      if (response.ok) {
        return response;
      } else {
        var error = new Error('Error ' + response.status + ': ' + response.statusText);
        error.response = response;
        throw error;
      }
    },
    error => {
          throw error;
    })
  .then(response => response.json())
  .then(response => { 
    console.log('Edit Employee', response); 
    alert('Employee edited successfully!\n'); 
    /*window.location.reload(false);*/
    window.location.href = '/home'; 
  })
  .catch(error =>  { 
    console.log('Edit Employee', error.message); 
    alert('Employee could not be edited\nError: '+error.message); 
  });
};

/**
 * Delete Employee
 */
 export const deleteEmployee = (third_party_id) => (dispatch) => {
  
  var third_party_id_string = third_party_id + '';

  //const bearer = 'Bearer ' + localStorage.getItem('token');
  
  return fetch(baseUrlApiRest +  delete_employees + '/' + third_party_id_string, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json"
      },
      credentials: "same-origin"
  })
  .then(response => {
      if (response.ok) {
        return response;
      } else {
        var error = new Error('Error ' + response.status + ': ' + response.statusText);
        error.response = response;
        throw error;
      }
    },
    error => {
          throw error;
    })
  .then(response => { 
    console.log('Employee deleted successfully'); 
    alert('Employee deleted successfully!\n'); 
    /*window.location.reload(false);*/
    window.location.href = '/home'; 
  })
  .catch(error =>  { 
    console.log('Delete Employee', error.message); 
    alert('Employee could not be deleted\nError: '+error.message); 
  });
};


/* Request to Laravel API and show error or proceed to dispatch the data  */
export const fetchCountries = () => (dispatch) => {

  dispatch(countriesLoading(true));

  return fetch(baseUrlApiRest + countries, {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    },
    credentials: "same-origin"
  })
  .then(response => {
    if (response.ok) {
      return response;
    } else {
      var error = new Error('Error ' + response.status + ': ' + response.statusText);
      error.response = response;
      throw error;
    }
  })
  .then(response => response.json())
  .then(countries => dispatch(addCountries(countries)))
  .catch(error => dispatch(countriesFailed(error.message)));
}

/* Call action type from countries reducer */
export const countriesLoading = () => ({
  type: ActionTypes.COUNTRIES_LOADING
});

/* Call action type from countries reducer */
export const countriesFailed = (errmess) => ({
  type: ActionTypes.COUNTRIES_FAILED,
  payload: errmess
});

/* Call action type from countries reducer */
export const addCountries = (countries) => ({
  type: ActionTypes.ADD_COUNTRIES,
  payload: countries
});

/* Request to Laravel API and show error or proceed to dispatch the data  */
export const fetchAreas = () => (dispatch) => {

  dispatch(areasLoading(true));

  return fetch(baseUrlApiRest + areas, {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    },
    credentials: "same-origin"
  })
  .then(response => {
    if (response.ok) {
      return response;
    } else {
      var error = new Error('Error ' + response.status + ': ' + response.statusText);
      error.response = response;
      throw error;
    }
  })
  .then(response => response.json())
  .then(areas => dispatch(addAreas(areas)))
  .catch(error => dispatch(areasFailed(error.message)));
}

/* Call action type from areas reducer */
export const areasLoading = () => ({
  type: ActionTypes.AREAS_LOADING
});

/* Call action type from areas reducer */
export const areasFailed = (errmess) => ({
  type: ActionTypes.AREAS_FAILED,
  payload: errmess
});

/* Call action type from areas reducer */
export const addAreas = (areas) => ({
  type: ActionTypes.ADD_AREAS,
  payload: areas
});


/* Request to Laravel API and show error or proceed to dispatch the data  */
export const fetchTypesOfIdentityDocuments = () => (dispatch) => {

  dispatch(typesofidentitydocumentsLoading(true));

  return fetch(baseUrlApiRest + types_of_identity_documents, {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    },
    credentials: "same-origin"
  })
  .then(response => {
    if (response.ok) {
      return response;
    } else {
      var error = new Error('Error ' + response.status + ': ' + response.statusText);
      error.response = response;
      throw error;
    }
  })
  .then(response => response.json())
  .then(types_of_identity_documents => dispatch(addTypesOfIdentityDocuments(types_of_identity_documents)))
  .catch(error => dispatch(typesofidentitydocumentsFailed(error.message)));
}

/* Call action type from types of identity documents reducer */
export const typesofidentitydocumentsLoading = () => ({
  type: ActionTypes.TYPES_OF_IDENTITY_DOCUMENTS_LOADING
});

/* Call action type from types of identity documents reducer */
export const typesofidentitydocumentsFailed = (errmess) => ({
  type: ActionTypes.TYPES_OF_IDENTITY_DOCUMENTS_FAILED,
  payload: errmess
});

/* Call action type from types of identity documents reducer */
export const addTypesOfIdentityDocuments = (types_of_identity_documents) => ({
  type: ActionTypes.ADD_TYPES_OF_IDENTITY_DOCUMENTS,
  payload: types_of_identity_documents
});


/**
 * Request to validate email, the function promises continues 
 * inside the componets that call this function due to this
 * function return a value and this must be captured
 */
 export const retrieveNewEmail = (
                                  last_name, 
                                  first_name, 
                                  country_code, 
                                  third_party_id = null
                                  ) => (dispatch) => {

  if (third_party_id==null || third_party_id=='') {
    third_party_id = '';
  }else {
    third_party_id = '/' + third_party_id
  }
  var parameters_link = '/' + last_name + '/' + first_name + '/' + country_code + third_party_id;
  
  return fetch(baseUrlApiRest +  retrieve_new_email + parameters_link, {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    },
    credentials: "same-origin"
  });
};
