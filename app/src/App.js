import React from 'react';
import ButtonList from './Components/ButtonList';

class App extends React.Component {
  state = {
    options: [
      {
        id: 1,
        type: 'package',
        identifier: 'A',
        selected: false
      },
      {
        id: 2,
        type: 'package',
        identifier: 'B',
        selected: false
      },
      {
        id: 3,
        type: 'delivery',
        identifier: 'A',
        selected: false
      },
      {
        id: 4,
        type: 'delivery',
        identifier: 'B',
        selected: false
      }

    ],
    packageIdentifier: null,
    deliveryIdentifier: null
  };

  selectPackage = (id) => {
    this.setState({
      options: this.state.options.map(btn => {
        if(btn.id === id) {
          btn.selected = !btn.selected;
        }
        return btn;
      })
    })
  }

  selectDelivery = (id) => {
    this.setState({
      options: this.state.options.map(btn => {
        if(btn.id === id) {
          btn.selected = !btn.selected;
        }
        return btn;
      })
    })
  }

  submitRequest = () => {
    const {pack, deli} = this.state.options.map(btn => {
      var packArr = Array(1);
      var deliArr = Array(1);
      if (btn.selected) {
        if(btn.type === 'package'){
          packArr.concat(btn);
        }
        else if (btn.type === 'delivery'){
          deliArr.concat(btn);
        }
        btn.selected = false;
      }
      return {packArr, deliArr};
    })



    /*this.state.options.forEach( (btn) => {
          if (btn.selected) {
            this.buildRequest(btn.type, btn.identifier);
            btn.selected = false;
          }
        }
    )*/
    console.log("Sending: " + pack + ' -> ' + deli);
    this.sendAPIRequest(this.state.packageIdentifier, this.state.deliveryIdentifier);
  }

  buildRequest = (type, identifier) => {
    if(type === 'package') {
      this.setState({packageIdentifier: identifier});
      console.log(this.state.packageIdentifier);
    }
    else if(type === 'delivery') {
      this.setState({deliveryIdentifier: identifier});
      console.log(this.state.deliveryIdentifier);
    }
    console.log(type + " " + identifier);
  }

  sendAPIRequest(pack, delivery) {
    console.log("Sending function values: " + pack + ' -> ' + delivery);
    console.log("Sending state values: " + this.state.packageIdentifier + ' -> ' + this.state.deliveryIdentifier);
  }

  render() {
    return (
        <div className="App">
          <h1>Packages:</h1>
          <ButtonList buttons={this.state.options} selectPackage={this.selectPackage} selectDelivery={this.selectDelivery}/>
          <div>
            <h1>Submit</h1>
            <button style={submitBtnStyle} onClick={this.submitRequest}>Submit</button>
          </div>
        </div>

    );
  }
}

const submitBtnStyle = {
  background:'gray',
  color: 'black',
  border: 'solid',
  padding: '20px 20px',
  cursor: 'pointer',
}

export default App;