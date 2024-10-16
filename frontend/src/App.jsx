import { useState, useEffect } from 'react';
import './App.css';
import Input from './components/input/Input';
import Output from './components/output/Output';
import Run from './components/button/run/Run';
import DarkLight from './components/button/darklight/DarkLight';
import Clear from './components/button/clear/Clear';

function App() {
  const [value, setValue] = useState('');
  const [isDarkMode, setIsDarkMode] = useState(false);

  // Load the dark mode preference from localStorage
  useEffect(() => {
    const storedMode = localStorage.getItem('isDarkMode');
    if (storedMode) {
      setIsDarkMode(JSON.parse(storedMode));
    }
  }, []);

  // Function to toggle dark mode
  const toggleDarkMode = () => {
    setIsDarkMode((prevMode) => {
      const newMode = !prevMode;
      localStorage.setItem('isDarkMode', JSON.stringify(newMode));
      return newMode;
    });
  };
  
  return (
    <div
      className="App"
      style={{
        backgroundColor: isDarkMode ? 'black' : 'white',
        color: isDarkMode ? 'white' : 'black',
        height: '100vh',
        transition: 'background-color 0.3s ease',
      }}
    >
      <Input value={value} setValue={setValue} /> 
      <Output/>
      <Run inputValue={value} />
      <DarkLight toggleDarkMode={toggleDarkMode} isDarkMode={isDarkMode} />
      <Clear value={value} setValue={setValue} />
    </div>
  );
}

export default App;
