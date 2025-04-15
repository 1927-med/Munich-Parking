/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 */
import React from 'react';
import { View, Image, Button, StyleSheet, Alert } from 'react-native';

const logo = require('./Munich.png');

const App: React.FC = () => {
  return (
    <View style={styles.container}>
      <Image source={logo} style={styles.logo} />
      <View style={styles.buttonContainer}>
        <Button title="Sign Up" color="green" onPress={() => Alert.alert('Sign Up pressed')} />
        <View style={{ marginTop: 10 }} />
        <Button title="Log In" color="green" onPress={() => Alert.alert('Log In pressed')} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'black',
    alignItems: 'center',
    justifyContent: 'center',
  },
  logo: {
    width: 200,
    height: 200,
    resizeMode: 'contain',
    marginBottom: 50,
  },
  buttonContainer: {
    width: '80%',
    alignItems: 'center',
  },
});

export default App;
