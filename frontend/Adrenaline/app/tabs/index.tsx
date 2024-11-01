import { Text, View, StyleSheet } from "react-native";
import { Link } from "expo-router";

export default function Index() {
    return (
        <View style={styles.container}>
            <Text style={styles.text}>Index.tsx</Text>
            <Link href="/tabs/profile" style={styles.button}>
                Go to Profile
            </Link>
        </View>
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
