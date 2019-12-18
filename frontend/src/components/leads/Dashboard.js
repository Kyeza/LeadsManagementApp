import React, {Fragment} from 'react';
import Form from "./Form";
import Leads from "./Leads";

const Dashboard = () => {
    return (
        <div>
            <Fragment>
                <Form />
                <Leads />
            </Fragment>
        </div>
    );
};

export default Dashboard;
