import { useState } from 'react';
import axios from 'axios';

const ChatComponent = () => {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent default form submission

    try {
      // Your actual API Gateway endpoint
      const apiEndpoint = 'https://mw8mqqv2sk.execute-api.us-east-1.amazonaws.com/dev'; 

      const result = await axios.post(apiEndpoint, {
        input: input,  // Sending user input in the request body
      });

      setResponse(result.data.response); // Extract response from data
      setError(''); // Clear any previous errors
    } catch (err) {
      console.error('Error fetching response:', err);
      setError('An error occurred while fetching the response. Please try again.');
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask ChatKGB something..."
          required
        />
        <button type="submit">Ask ChatKGB</button>
      </form>
      {response && (
        <div>
          <h3>Response:</h3>
          <p>{response}</p>
        </div>
      )}
      {error && (
        <div>
          <h3>Error:</h3>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
};

export default ChatComponent;
