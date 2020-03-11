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
        type: 'delivery',
        identifier: 'A',
        selected: false
      },
    ]
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
    let buttons = this.state.options.map((btn) => {
      if (btn.selected) {
        btn.selected = false;
        return btn;
      }
    });
    let filtered = buttons.filter((element) => {
      return element != null;
    })
    console.log(filtered);

    let pack = filtered.map((btn) => {
      if(btn.type === 'package') {
        return btn.identifier;
      }
    })
    let deli = filtered.map((btn) => {
      if(btn.type === 'delivery') {
        return btn.identifier;
      }
    })
    console.log("pack | deli " + pack + "|" + deli);
    this.sendAPIRequest(pack, deli);
  }

  sendAPIRequest(pack, delivery) {
    console.log("Sending function values: " + pack + ' -> ' + delivery);
    fetch("http://127.0.0.1:8080/routeRobot/" + pack + "/" + delivery);
  }

  render() {
    return (
        <div className="App">
          <h1>Packages:</h1>
          <ButtonList buttons={this.state.options} selectPackage={this.selectPackage}
                      selectDelivery={this.selectDelivery}/>
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