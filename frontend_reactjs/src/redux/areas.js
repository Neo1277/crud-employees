import * as ActionTypes from './ActionTypes';

/* Set reducer to handle redux state */
export const Areas = (state = { 
    isLoading: true,
    errMess: null,
    areas:[]}, action) => {
    switch (action.type) {
        case ActionTypes.ADD_AREAS:
            return {...state, isLoading: false, errMess: null, areas: action.payload};

        case ActionTypes.AREAS_LOADING:
            return {...state, isLoading: true, errMess: null, areas: []}

        case ActionTypes.AREAS_FAILED:
            return {...state, isLoading: false, errMess: action.payload};

        default:
            return state;
    }
};