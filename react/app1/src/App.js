import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';

function App() {

  const [comments, setComments] = React.useState([]);
  const [type, setType] = React.useState("comments");

  React.useEffect(() => {
    fetch('http://jsonplaceholder.typicode.com/comments' + type)
    .then(response => response.ok ? response.json() : Promise.reject(response))
    .then(data => {
        setComments(data);
    });
}, [type]);

  return (
  <div className="container">
    <div className="row m-5 border p-5">
      <Form setType={setType}/>
      <ListArrowFunction comments={comments} />
      </div>
    </div>
  );
}

function List({comments}) {
 /*let elements = [];

 for(let element of props.comments) {
  elements.push(
      <li className="list-group-item">
        {element.body}
      </li>
      );
  }
  return (<ul>{elements}</ul>);*/

  return (
  <ul>
    {comments.map(element => (
      <li key={element.id} className="list-group-item">
        {element.body}
      </li>
    ))}
  </ul>);
} 

const ListArrowFunction = ({comments}) => (
   <ul>
     {comments.map(element => (
       <li key={element.id} className="list-group-item">
         {element.body}
       </li>
     ))}
   </ul>
);
 
const Form = ({setType}) => (
  <form className='w-100' onSubmit={(event) =>{
    event.preventDefault();
    setType(event.target.elements.contentType.value);
  }}>
    <select 
      name="contentType"
      className="form-control"
    >
      <option value="comments">Comments</option>
      <option value="posts">Posts</option>
    </select>
    <button 
    className='btn btn-primary mb-2'
    type='submit'>
      Kiválaszt
    </button>
  </form>
)

export default App;