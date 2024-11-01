import { Text, View, StyleSheet } from "react-native";
import { Link } from "expo-router";
import { Routine } from "../../types/fitnessTypes";
import RoutineCard from "../../components/RoutineCard";
import { colors } from "../../themes/colors";
import CardPlus from "../../components/CardPlus";

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
          <View style={{ marginHorizontal: "4%", marginVertical: "2%" }}>
            <RoutineCard routine={routine} />
          </View>
        ))}
        <View style={{ marginHorizontal: "4%", marginVertical: "2%" }}>
          <CardPlus />
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    // backgroundColor: "#fff",
    backgroundColor: colors.background,
  },
  text: {
    color: colors.dark,
    fontSize: 24,
    marginHorizontal: "4%",
    marginTop: "2%",
    paddingVertical: "2%",
    fontWeight: "500",
  },
});
