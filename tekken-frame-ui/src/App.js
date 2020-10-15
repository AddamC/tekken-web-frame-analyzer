import React from 'react';
import { AppBar, Button, ThemeProvider, Drawer } from '@material-ui/core'
import { BrowserRouter as Router, Route } from 'react-router-dom';

// const theme = withStyles

class App extends React.Component {
  constructor(props) {
    super();
    this.state = {
      characters: [],
      marginLeft: 200
    }
  }

  componentDidMount() {
    const url = "http://localhost:3001/characters/list"
    fetch(url)
      .then(response => {
        return response.json()
      })
      .then(json => {
        this.setState({ characters: json.data })
      })
  }

  render() {
    return (

      <Router>
        {/* <ThemeProvider theme={theme}> */}
        <AppBar>
          <Drawer style={{width: `${this.state.marginLeft}px`}} open={true} variant="persistent">
            <Button>Frame Data</Button>
            <Button>2</Button>
            <Button>3</Button>
          </Drawer>
        </AppBar>

        <div style={{marginLeft: this.state.marginLeft}}>
          <h1>teste</h1>
          {this.state.characters.map(c => {
            return (<h1 key={c._id}>{c.name}</h1>)
          })}
        </div>
        <Route path="/" exact>
        </Route>

        <Route path="/frame-data">
          {/* <CharacterList></CharacterList> */}
        </Route>
        {/* </ThemeProvider> */}
      </Router>
    )
  }
}

export default App;