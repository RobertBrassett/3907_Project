import React from 'react';
import Package from './Package';
import Delivery from './Delivery';
import PropTypes from 'prop-types';

class ButtonList extends React.Component {

    render() {
        return this.props.buttons.map((btn) => {
            if (btn.type === 'package') {
                return (
                    <p>
                        <Package btn={btn} selectPackage={this.props.selectPackage}/>
                    </p>
                )
            }

            if (btn.type === 'delivery') {
                return (
                    <p>
                        <Delivery btn={btn} selectDelivery={this.props.selectDelivery}/>
                    </p>
                )
            }
        });
    }
}

ButtonList.propTypes = {
    buttons: PropTypes.array.isRequired
}

export default ButtonList;
