import { fetchEmployees } from '../../redux/ActionCreators';
import * as ActionTypes from '../../redux/ActionTypes';
import configureMockStore from 'redux-mock-store'
import thunk from 'redux-thunk'

const middlewares = [ thunk ];
const mockStore = configureMockStore(middlewares);

const mockResponse = (status, statusText, response) => {
    return new window.Response(response, {
      status: status,
      statusText: statusText,
      headers: {
        'Content-type': 'application/json'
      }
    });
};

it('calls request and success actions if the fetch response was successful', () => {
    const initialState = {}
    const store = mockStore(initialState)

    // Other way of mocking response: '{"ids":{"provider":1}}'

    window.fetch = jest.fn().mockImplementation(() =>
      Promise.resolve(
            mockResponse(200, null, 
                JSON.stringify({
                    "results": [
                        {
                            "identity_document": "112235856456",
                            "third_party_id": "11",
                            "last_name": "BERMUDEZ",
                            "second_surname": "ALOS",
                            "first_name": "FARINA",
                            "middle_names": "ALEJANDRA",
                        }
                    ]            
                })
            )
        )
    );

    
    // Other way of pass expected response: payload: {"ids": {"provider": 1}}
  
    return store.dispatch(fetchEmployees())
      .then(() => {
        const expectedActions = store.getActions();
        expect(expectedActions.length).toBe(2);
        expect(expectedActions).toContainEqual({type: ActionTypes.EMPLOYEES_LOADING});
        expect(expectedActions).toContainEqual({type: ActionTypes.ADD_EMPLOYEES ,
            payload: {
                results: [
                    {
                        "identity_document": "112235856456",
                        "third_party_id": "11",
                        "last_name": "BERMUDEZ",
                        "second_surname": "ALOS",
                        "first_name": "FARINA",
                        "middle_names": "ALEJANDRA",
                    }
                ]      
            }
         });
      })
});

/**
 * Tutorial unit tests in react:
 * https://medium.com/@ferrannp/unit-testing-with-jest-redux-async-actions-fetch-9054ca28cdcd
 */