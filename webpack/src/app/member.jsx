import "isomorphic-fetch"

import React from 'react';
import { render } from 'react-dom';

class App extends React.Component {
    constructor () {
        super();
        this.state = {
          error: null,
          isLoaded: false,
          members: [],
        };
    }

    componentDidMount() {
      fetch("/api/Member/")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              isLoaded: true,
              members: result[0].List,
            });
          },
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        )
    }

    render() {
      const { error, isLoaded, members } = this.state;

      if (error) {
        return <div>Error: {error.message}</div>;
      } else if (!isLoaded) {
        return (<div>Loading...</div>);
      } else {
        return (
          <div>
              <h1>Hello World!</h1>
          </div>
        );
      }
    }
}

render(<App/>,window.document.getElementById('app'));
