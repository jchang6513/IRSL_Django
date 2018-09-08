import React from 'react';
import { render } from 'react-dom';
import { UserCard } from 'react-ui-cards';

class App extends React.Component {
    constructor () {
        super();
        this.state = {
          error: null,
          isLoaded: false,
          links: []
        };
    }

    componentDidMount() {
      fetch("/api/link/")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              isLoaded: true,
              links: result,
            });
          },
          // Note: it's important to handle errors here
          // instead of a catch() block so that we don't swallow
          // exceptions from actual bugs in components.
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        )
    }

    render() {
      const { error, isLoaded, links } = this.state;
      if (error) {
        return <div>Error: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Loading...</div>;
      } else {
        return (
          <div className="row d-flex justify-content-around">
            {links.map(link => (
                  <UserCard
                    cardClass='flex'
                    href={link.link}
                    header={link.img}
                    name={link.chinese}
                    positionName={link.english}
                  />
            ))}
          </div>
        );
      }
    }

}

render(<App/>,window.document.getElementById('app'));
