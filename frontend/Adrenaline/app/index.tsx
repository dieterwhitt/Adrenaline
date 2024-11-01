import { Link } from "expo-router";
import { View, Text } from "react-native";

// future login page
export default function Index() {
  return (
    <View>
      <Text>Future login page.</Text>
      <Link href="/tabs/" style={{ textDecorationLine: "underline" }}>
        Proceed to app!
      </Link>
    </View>
  );
}
