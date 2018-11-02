import React from 'react';
import { render } from 'react-dom';
import { Accordion, AccordionItem } from 'react-sanfona';

class App extends React.Component {
    constructor () {
        super();
        this.state = {
          error: null,
          isLoaded: false,
          classes: [],
          courses: [],
        };
    }

    componentDidMount() {
      fetch("/api/class/")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              isLoaded: true,
              classes: result,
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
      fetch("/api/course/")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              isLoaded: true,
              courses: result,
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
      const { error, isLoaded, classes, courses } = this.state;
      let imap = 0
      if (error) {
        return <div>Error: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Loading...</div>;
      } else {
        return (
          <Accordion allowMultiple={true}>
            {classes.map(cl => {
              imap ++
              return (
                <AccordionItem title={cl.name} expanded={imap === 1}>
                  <div className="row m-0">
                      <div className="col-lg-6 col-md-6 col-sm-12 pb-4">
                          <h5>Lecture</h5>
                          {cl.lectures.map(course => {
                              return (
                                	<table class="course_table">
                                			<tr>
                                  				<td class="course_left">{course.date}</td>
                                          {course.handout ? (
                                              <td class="course_right"><a href={course.handout} target="_blank">{course.title}</a></td>
                                          ) : (
                                              <td class="course_right">{course.title}</td>
                                          )}
                                			</tr>
                                	</table>
                              );
                          })}
                      </div>
                      <div className="col-lg-6 col-md-6 col-sm-12 pb-4">
                          <h5>Apendix</h5>
                          {cl.appendices.map(course => {
                            return (
                              	<table class="course_table">
                              			<tr>
                                        {course.handout ? (
                                            <td class="course_right"><a href={course.handout} target="_blank">{course.title}</a></td>
                                        ) : (
                                            <td class="course_right">{course.title}</td>
                                        )}
                              			</tr>
                              	</table>
                            );
                          })}
                      </div>
                  </div>
                </AccordionItem>
              );
            })}
          </Accordion>
        );
      }
    }

}

render(<App/>,window.document.getElementById('app'));
