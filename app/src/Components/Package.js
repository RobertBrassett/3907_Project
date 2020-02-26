import React from 'react';
import PropTypes from 'prop-types';

class Package extends React.Component {

    getStyle = () => {
        return {
            background: this.props.btn.selected ? 'gray' : 'white',
            color: 'black',
            border: 'solid',
            padding: '20px 100px',
            borderRadius: '50%',
            cursor: 'pointer',
        }
    }

    render() {
        const {id, identifier} = this.props.btn;

        return (
            <div>
                <button style={this.getStyle()} onClick = {this.props.selectPackage.bind(this, id)}> {' '}
                    {identifier}
                </button>
            </div>
        );
    }
}

Package.propTypes = {
    button: PropTypes.object.isRequired
}

export default Package;
