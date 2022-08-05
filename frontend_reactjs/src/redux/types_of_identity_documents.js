import * as ActionTypes from './ActionTypes';

/* Set reducer to handle redux state */
export const TypesOfIdentityDocuments = (state = { 
    isLoading: true,
    errMess: null,
    types_of_identity_documents:[]}, action) => {
    switch (action.type) {
        case ActionTypes.ADD_TYPES_OF_IDENTITY_DOCUMENTS:
            return {...state, isLoading: false, errMess: null, types_of_identity_documents: action.payload};

        case ActionTypes.TYPES_OF_IDENTITY_DOCUMENTS_LOADING:
            return {...state, isLoading: true, errMess: null, types_of_identity_documents: []}

        case ActionTypes.TYPES_OF_IDENTITY_DOCUMENTS_FAILED:
            return {...state, isLoading: false, errMess: action.payload};

        default:
            return state;
    }
};