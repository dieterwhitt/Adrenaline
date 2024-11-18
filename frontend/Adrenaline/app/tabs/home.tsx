// home page or something

import { Text, View, ScrollView, StyleSheet } from "react-native";
import { Link } from "expo-router";
import { Routine } from "../../types/fitnessTypes";
import RoutineCard from "../../components/RoutineCard";
import { colors } from "../../themes/colors";
import CardPlus from "../../components/CardPlus";
import Constants from "expo-constants";

import { useState, useEffect } from "react";

const api_url = Constants.manifest.extra.BACKEND_URL;

const sampleRoutines: Routine[] = [
  {
    id: 1,
    name: "Routine 1",
    description: "My first Routine!",
    split: "Push-Pull-Legs",
    creation_date: "2024-10-01",
    workouts: [],
  },
];

// in the future, store tokens in secure storage after login
// re-log whenever token changes (validate token fails)
const token = Constants.manifest.extra.TEST_TOKEN;

export default function Home() {
  const [routines, setRoutines] = useState<Routine[]>([]);
  // for displaying loading (spinning wheel probably) and error messages.
  const [loading, setLoading] = useState<Boolean>(true);
  const [error, setError] = useState<Boolean>(false);

  // useEffect to list routines
  useEffect(() => {
    async function get_routines() {
      const response = await fetch(`${api_url}/routine/`, {
        method: "GET",
        headers: {
          Authorization: `Token ${token}`,
        },
      });
      // check error flag
      if (!response.ok) {
        setError(false);
        return;
      }
      // finish loading
      setLoading(false);
    }

    // call async
    get_routines();
  }, []);

  return (
    <ScrollView style={styles.scrollView}>
      <Text style={styles.text}>My Routines</Text>
      <View>
        {routines.map((routine) => (
          // parentheses - implicitly returns
          // todo: add key= to view
          <View style={{ marginHorizontal: "4%", marginVertical: "2%" }}>
            <RoutineCard routine={routine} />
          </View>
        ))}
        <View style={{ marginHorizontal: "4%", marginVertical: "2%" }}>
          <CardPlus />
        </View>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  scrollView: {
    flex: 1,
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
