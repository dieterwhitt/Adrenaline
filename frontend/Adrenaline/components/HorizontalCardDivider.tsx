// horizontal card divider
// for demo, will have more options for thickness etc.
import { colors } from "../themes/colors";
import { View } from "react-native";

export default function HorizontalCardDivider() {
  return (
    <View
      style={{
        // marginVertical: "1%",
        marginHorizontal: "5%",
        borderColor: colors.grayBorder,
        borderWidth: 1,
      }}
    ></View>
  );
}
