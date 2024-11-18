import { Link } from "expo-router";
import { View, Text } from "react-native";

// future login/landing page
export default function Index() {
  return (
    <View>
      <Text>Future login page.</Text>
      <Link href="/tabs/home" style={{ textDecorationLine: "underline" }}>
        Proceed to app!
      </Link>
    </View>
  );
}
