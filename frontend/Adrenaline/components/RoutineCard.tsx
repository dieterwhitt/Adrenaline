import { Text, View, StyleSheet, Pressable } from "react-native";
import { Routine, Workout } from "../types/fitnessTypes";
import HorizontalCardDivider from "./HorizontalCardDivider";
import { colors } from "../themes/colors";

// takes a routine type.
// for demo: just mapping data over ul. will need to read workouts soon tho.
export default function RoutineCard({ routine }: { routine: Routine }) {
  return (
    <Pressable style={routineCardStyle.card}>
      <View style={routineCardStyle.headerRow}>
        <Text style={routineCardStyle.header}>{routine.name}</Text>
        <Text style={routineCardStyle.subheader}>{routine.split}</Text>
      </View>
      <View>
        <Text style={routineCardStyle.body}>{routine.description}</Text>
        <HorizontalCardDivider />
        <View style={routineCardStyle.body}>
          <RoutineSmallDropdown routine={routine} />
        </View>
      </View>
    </Pressable>
  );
}

function RoutineSmallDropdown({ routine }: { routine: Routine }) {
  if (routine.workouts.length === 0) {
    return <Text style={{ fontStyle: "italic" }}>No workouts added</Text>;
  } else {
    return routine.workouts.map((workout: Workout) => (
      <Text>• {workout.name}</Text>
    ));
  }
}

function RoutineExpandedDropdown({ routine }: { routine: Routine }) {}

const routineCardStyle = StyleSheet.create({
  card: {
    backgroundColor: colors.lightHighlightBackground,
    borderColor: colors.grayBorder,
    borderRadius: 8,
    borderWidth: 2,
  },
  headerRow: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    marginHorizontal: "4%",
    marginVertical: "2%",
  },
  header: {
    fontSize: 20,
    color: colors.primary,
    fontWeight: "600",
  },
  subheader: {
    fontSize: 16,
    color: colors.orange,
    fontWeight: "600",
    textAlign: "right",
  },
  body: {
    fontSize: 14,
    marginHorizontal: "4%",
    marginVertical: "2%",
    color: colors.dark,
    fontWeight: "400",
  },
});
