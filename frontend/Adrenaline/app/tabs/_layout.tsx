import { Tabs } from "expo-router";

export default function TabLayout() {
    return (
        <Tabs>
            <Tabs.Screen
                name="index"
                options={{
                    title: "Home",
                    headerStyle: {
                        backgroundColor: "rgb(255, 168, 204)",
                    },
                }}
            />
            <Tabs.Screen
                name="profile"
                options={{
                    title: "Profile",
                    headerStyle: {
                        backgroundColor: "rgb(255, 168, 204)",
                    },
                }}
            />
        </Tabs>
    );
}
