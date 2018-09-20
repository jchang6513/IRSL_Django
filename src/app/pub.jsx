import React from 'react';
import { render } from 'react-dom';
import TagsInput from 'react-tagsinput'
import {createFilter} from 'react-search-input';

const KEYS_TO_FILTERS = ['no', 'year', 'author', 'title']

class App extends React.Component {
    constructor () {
        super();
        this.state = {
          error: null,
          isLoaded: false,
          plist: [],
          inters: [],
          domes: [],
          books: [],
          tags: [],
          placeholder: 'Search...',
        };
    }

    componentDidMount() {
      fetch("/api/publications/")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              isLoaded: true,
              plist: result[0].List,
            });
          },
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        )
      fetch("/api/international/")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              isLoaded: true,
              inters: result,
            });
          },
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        )
      fetch("/api/domestic/")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              isLoaded: true,
              domes: result,
            });
          },
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        )
      fetch("/api/book/")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              isLoaded: true,
              books: result,
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

    handleChange = (tags) => {
      this.setState({tags})
      if (tags.length == 0) {
        this.setState({placeholder: 'Search...'})
      } else {
        this.setState({placeholder: 'Add a tag'})
      }
    }

    RenderInput = (props) => {
      let {onChange, value, addTag, ...other} = props
      let widthMultiplier = 20
      let initialWidth = 100
      let valueWidth = Math.max(initialWidth, value.length * widthMultiplier)
      return (
        <input type='text' onChange={onChange} value={value} style={{width: valueWidth + "px"}} {...other} />
      )
    }

    render() {
      const { error, isLoaded, inters, domes, books } = this.state;

      const fInters = inters.filter(createFilter(this.state.tags.join(' '), KEYS_TO_FILTERS))
      const fDomes  = domes.filter(createFilter(this.state.tags.join(' '), KEYS_TO_FILTERS))
      const fBooks  = books.filter(createFilter(this.state.tags.join(' '), KEYS_TO_FILTERS))

      if (error) {
        return <div>Error: {error.message}</div>;
      } else if (!isLoaded) {
        return (<div>Loading...</div>);
      } else {
        return (
          <div id="scrollArea" class="clusterize-scroll">
            <div className="row">
              <div className="col-lg-8 col-sm-12 mb-2">
                <div>
                <span class="glyphicon glyphicon-search" aria-hidden="true"></span>
                </div>
                <TagsInput
                  value={this.state.tags}
                  onChange={this.handleChange}
                  className='react-tagsinput'
                  addKeys={[13,32]}
                  onlyUnique={true}
                  inputProps={{className: 'react-tagsinput-input',placeholder: this.state.placeholder}}
                  renderInput={this.RenderInput}
                />
              </div>
              <div className="col-lg-4 col-sm-12 mb-3 pt-3 text-right align-middle">
                <h3><a href={this.state.plist} target="_blank">Publication List</a></h3>
              </div>
            </div>

            <br/>
            <h3>國際期刊</h3>
            <div id="contentArea" class="clusterize-content">
              {fInters.map(paper => {
                return (
                  <div class="clusterize-no-data">
                    <br/>
                    <p> {paper.year}.{paper.no} </p>
                    {paper.paper ? (
                      <a href={paper.paper} target="_blank"><p>{paper.author}</p><p>{paper.title}</p></a>
                    ) : (
                      <div><p>{paper.author}</p><p>{paper.title}</p></div>
                    )}
                    <hr class="s1"/>
                  </div>
                );
              })}
            </div>

            <br/>
            <h3>國內期刊</h3>
            <div id="contentArea" class="clusterize-content">
              {fDomes.map(paper => {
                return (
                  <div class="clusterize-no-data">
                    <br/>
                    <p> {paper.year}.{paper.no} </p>
                    {paper.paper ? (
                      <a href={paper.paper} target="_blank"><p>{paper.author}</p><p>{paper.title}</p></a>
                    ) : (
                      <div><p>{paper.author}</p><p>{paper.title}</p></div>
                    )}
                    <hr class="s1"/>
                  </div>
                );
              })}
            </div>

            <br/>
            <h3>專書</h3>
            <div id="contentArea" class="clusterize-content">
              {fBooks.map(paper => {
                return (
                  <div class="clusterize-no-data">
                    <br/>
                    <p> {paper.year}.{paper.no} </p>
                    {paper.paper ? (
                      <a href={paper.paper} target="_blank"><p>{paper.author}</p><p>{paper.title}</p></a>
                    ) : (
                      <div><p>{paper.author}</p><p>{paper.title}</p></div>
                    )}
                    <hr class="s1"/>
                  </div>
                );
              })}
            </div>
          </div>
        );
      }
    }
}

render(<App/>,window.document.getElementById('app'));
