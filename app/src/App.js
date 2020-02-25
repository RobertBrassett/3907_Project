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
    this.state.options.forEach( (btn) => {
          if (btn.selected) {
            console.log(btn.selected);
            btn.selected = false;
            console.log(btn.selected);
          }
        }
    )

    console.log("Send submit was successful");
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
