import { Text, View, StyleSheet } from "react-native";

export default function ProfileScreen() {
    return (
        <View style={styles.container}>
            <Text style={styles.text}>Profile Screen</Text>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "rgb(255, 245, 250)",
        alignItems: "center",
        justifyContent: "center",
    },
    text: {
        color: "rgb(37, 41, 46)",
    },
});
