import { Tabs } from "expo-router";
import Ionicons from "@expo/vector-icons/Ionicons";

// To do: define color themes

export default function TabLayout() {
  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: "rgb(252, 101, 96)",
        headerStyle: {
          backgroundColor: "rgb(255, 168, 204)",
        },
        headerShadowVisible: false,
        headerTintColor: "rgb(255, 255, 255)",
        tabBarStyle: {
          backgroundColor: "rgb(245, 230, 230)",
        },
      }}
    >
      <Tabs.Screen
        name="index"
        options={{
          title: "Home",
          tabBarIcon: ({ color, focused }) => (
            <Ionicons
              name={focused ? "home-sharp" : "home-outline"}
              color={color}
              size={24}
            />
          ),
        }}
      />
      <Tabs.Screen
        name="profile"
        options={{
          title: "Profile",
          tabBarIcon: ({ color, focused }) => (
            <Ionicons
              name={focused ? "person-sharp" : "person-outline"}
              color={color}
              size={24}
            />
          ),
        }}
      />
    </Tabs>
  );
}
