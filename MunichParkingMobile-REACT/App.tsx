/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 */
import React from 'react';
import logo from './Munich.png';

const App: React.FC = () => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', backgroundColor: 'black' }}>
      <img src={logo} alt="Logo" style={{ width: '200px', height: 'auto', marginTop: '50px' }} />
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <button style={{ backgroundColor: 'green', color: 'white', padding: '10px 20px', marginTop: '50px' }}>Sign Up</button>
        <button style={{ backgroundColor: 'green', color: 'white', padding: '10px 20px', marginTop: '10px' }}>Log In</button>
      </div>
    </div>
  );
};

export default App;
