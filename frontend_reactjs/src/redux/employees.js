import * as ActionTypes from './ActionTypes';

/* Set reducer to handle redux state */
export const Employees = (state = { 
    isLoading: true,
    errMess: null,
    employees:[]}, action) => {
    switch (action.type) {
        case ActionTypes.ADD_EMPLOYEES:
            return {...state, isLoading: false, errMess: null, employees: action.payload};

        case ActionTypes.EMPLOYEES_LOADING:
            return {...state, isLoading: true, errMess: null, employees: []}

        case ActionTypes.EMPLOYEES_FAILED:
            return {...state, isLoading: false, errMess: action.payload};

        default:
            return state;
    }
};