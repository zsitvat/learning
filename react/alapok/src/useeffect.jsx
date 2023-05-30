import React, { useState, useEffect } from 'react';


function UseEffect() {
    const [count, setCount] = useState(0);
    const [count2, setCount2] = useState(0);

    useEffect(() => {
        console.log("useEffect");
        document.title = `Clicked ${count} and ${count2} times`;
    }, [count,count2]);


    return (
        <div>
            <p>Clicked {count} times</p>
            <button onClick={() => setCount(count + 1)}>Click</button>
            <p>Clicked {count2} times</p>
            <button onClick={() => setCount2(count2 + 1)}>Click</button>
        </div>
    )
}

export default UseEffect;