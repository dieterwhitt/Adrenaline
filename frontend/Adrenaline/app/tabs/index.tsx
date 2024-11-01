import { Text, View, StyleSheet } from "react-native";
import { Link } from "expo-router";
import { Routine } from "../../types/fitnessTypes";
import RoutineCard from "../../components/RoutineCard";

const sampleRoutines: Routine[] = [
  {
    id: 1,
    name: "Routine 1",
    description: "My first Routine!",
    split: "Push-Pull-Legs",
    creation_date: "2024-10-01",
    data: ["Monday: Push", "Wednesday: Pull", "Friday: Legs"],
  },
];

export default function Index() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>My Routines</Text>
      <View>
        {sampleRoutines.map((routine) => (
          // parentheses - implicitly returns
          <RoutineCard routine={routine} />
        ))}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    // backgroundColor: "#fff",
    backgroundColor: "rgb(255, 245, 250)",
  },
  text: {
    color: "rgb(59, 0, 7)",
    fontSize: 24,
    marginHorizontal: "4%",
    marginTop: "2%",
    paddingVertical: "2%",
    fontWeight: "500",
  },
  button: {
    fontSize: 20,
    textDecorationLine: "underline",
    color: "rgb(37, 41, 46)",
  },
});
