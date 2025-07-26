// React Native - App.js
import React from 'react';
import { View, Text, Button, Alert } from 'react-native';

export default function App() {
  return (
    <View style={{padding: 50}}>
      <Text>📱 Hiva Mobile Panel</Text>
      <Button title="ورود" onPress={() => Alert.alert("ورود با موفقیت")} />
    </View>
  );
}
