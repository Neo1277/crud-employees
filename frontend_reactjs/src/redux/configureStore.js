import {createStore, combineReducers, applyMiddleware} from 'redux';
import { Employees } from './employees';
import { Countries } from './countries';
import { Areas } from './areas';
import { TypesOfIdentityDocuments } from './types_of_identity_documents';
import thunk from 'redux-thunk';
import logger from 'redux-logger';

/* Configure store for letting the data be there even if the page is reloaded */
export const ConfigureStore = () => {
    const store = createStore(
        combineReducers({
            employees: Employees,
            countries: Countries,
            areas: Areas,
            types_of_identity_documents: TypesOfIdentityDocuments
        }),
        applyMiddleware(thunk, logger)
    );

    return store;
}