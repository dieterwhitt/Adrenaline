// plus sign prompt for adding new cards
// future: will need to pass link/route as prop

import { Text, View, StyleSheet, Pressable } from "react-native";
import AntDesign from "@expo/vector-icons/AntDesign";
import { colors } from "../themes/colors";

export default function CardPlus() {
  return (
    <Pressable>
      <View style={style.cardPlus}>
        <AntDesign
          name="pluscircleo"
          size={60}
          color={colors.mediumGrayBorder}
        />
      </View>
    </Pressable>
  );
}

const style = StyleSheet.create({
  cardPlus: { alignItems: "center" },
});
