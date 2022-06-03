import {createSlice} from "@reduxjs/toolkit"

const authSlice = createSlice({
    name: 'todo',
    initialState:{
        user:{
            isAuthenticated:false
        }
    },
    reducers:{
        login(state, action){
          state.user = {...action.payload,isAuthenticated:true}
        },

        logout(state, action) {
            state.user = {isAuthenticated:false}
        },
        register(state, action) {}
    }
});
export const {login,   logout, register} = authSlice.actions;
export default authSlice.reducer;