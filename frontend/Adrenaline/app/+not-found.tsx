import { View, StyleSheet } from "react-native";
import { Link, Stack } from "expo-router";

export default function NotFoundScreen() {
  return (
    <>
      <Stack.Screen options={{ title: "Oops! Not Found" }} />
      <View style={styles.container}>
        <Link href="/tabs/home" style={styles.button}>
          Go back to Home screen!
        </Link>
      </View>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    // backgroundColor: "#fff",
    backgroundColor: "rgb(255, 245, 250)",
    alignItems: "center",
    justifyContent: "center",
  },
  text: {
    color: "rgb(37, 41, 46)",
  },
  button: {
    fontSize: 20,
    textDecorationLine: "underline",
    color: "rgb(37, 41, 46)",
  },
});
