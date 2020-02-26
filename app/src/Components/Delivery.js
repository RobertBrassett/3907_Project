import React from 'react';
import PropTypes from 'prop-types';

class Delivery extends React.Component {

    getStyle = () => {
        return {
            background: this.props.btn.selected ? 'gray' : 'white',
            color: 'black',
            border: 'solid',
            padding: '20px 100px',
            cursor: 'pointer',
        }
    }

    render() {
        const {id, identifier} = this.props.btn;

        return (
            <div>
                <button style={this.getStyle()} onClick={this.props.selectDelivery.bind(this, id)}>
                    {identifier}
                </button>
            </div>
        );
    }
}

Delivery.propTypes = {
    button: PropTypes.object.isRequired
}

export default Delivery;