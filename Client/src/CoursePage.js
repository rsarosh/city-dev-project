import React from 'react';

export default class CoursePage extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        document.title = 'Digital Skills For All';
    }

    render() {

        console.log(this.props);
        return (
            <div>
                <h1>
                    {this.props.match.params.courseID}
                </h1>
            </div>
        );
    }
}